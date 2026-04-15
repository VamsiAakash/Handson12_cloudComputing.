import boto3

def lambda_handler(event, context):
    glue_client = boto3.client('glue', region_name='us-east-1')
    
    # Get the bucket and file name from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"File uploaded: s3://{bucket}/{key}")
    print("Triggering Glue job...")
    
    response = glue_client.start_job_run(
        JobName='process_reviews_job'
    )
    
    print(f"Glue job started! JobRunId: {response['JobRunId']}")
    
    return {
        'statusCode': 200,
        'body': f"Glue job triggered successfully! JobRunId: {response['JobRunId']}"
    }
