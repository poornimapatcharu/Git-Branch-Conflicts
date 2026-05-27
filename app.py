import boto3
from botocore.exceptions import NoCredentialsError

try:

    s3 = boto3.client("lambda")
    response = s3.list_buckets()

    print("Connected to S3 successfully")

    for bucket in response["Buckets"]:
        print(bucket["dev"])

except NoCredentialsError:
    print("AWS credentials not found")

except Exception as e:
    print("Error:", e)
