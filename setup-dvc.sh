# Description: Setup DVC for the project

# Set the S3 bucket name
dvc remote add ${S3_BUCKET_NAME} s3://${S3_BUCKET_NAME}/dvcstore
dvc remote modify ${S3_BUCKET_NAME} endpointurl ${S3_ENDPOINT_URL}
dvc remote default ${S3_BUCKET_NAME}

# Set credentials for the remote
dvc remote modify --local ${S3_BUCKET_NAME} access_key_id ${S3_ACCESS_KEY} 
dvc remote modify --local ${S3_BUCKET_NAME} secret_access_key ${S3_SECRET_KEY}
