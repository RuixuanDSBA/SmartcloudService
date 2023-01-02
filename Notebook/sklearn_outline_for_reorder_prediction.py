import boto3
import pandas as pd
from sagemaker import get_execution_role
from sagemaker.sklearn.estimator import SKLearn

# Set up clients for SageMaker and S3
sagemaker = boto3.client('sagemaker')
s3 = boto3.client('s3')

# Set up variables for the model training
bucket_name = 'my-bucket'
data_key = 'data/customer_data.csv'
model_output_path = 's3://{}/model'.format(bucket_name)
role = get_execution_role()

# Load the training data from S3
data = pd.read_csv('s3://{}/{}'.format(bucket_name, data_key))

# Split the data into features and target
X = data.drop('repurchased', axis=1)
y = data['repurchased']

# Set up the SKLearn Estimator
sklearn = SKLearn(
    entry_point='train.py',
    role=role,
    train_instance_count=1,
    train_instance_type='ml.m4.xlarge',
    output_path=model_output_path
)

# Train the model
sklearn.fit({'train': X, 'target': y})

# Deploy the model
sklearn_predictor = sklearn.deploy(
    initial_instance_count=1,
    instance_type='ml.m4.xlarge'
)

# Make a prediction
sklearn_predictor.predict(X[:10])
