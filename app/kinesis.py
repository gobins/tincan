import boto3, os
import logging
import time
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

try:
    kinesis = boto3.client('kinesis',
                        endpoint_url="http://localhost:4568",
                        use_ssl=False,
                        aws_access_key_id="test",
                        aws_secret_access_key="test",
                        region_name="ap-southeast-2") 

    resp = kinesis.list_streams()

    stream_name = "mystream"
    partition_key = "secret"
    if stream_name not in resp["StreamNames"]:
        logging.info("creating stream...")
        kinesis.create_stream( StreamName=stream_name, ShardCount=3)
        time.sleep(5)
    data = os.urandom(16)

    response = kinesis.put_record(
        StreamName=stream_name,
        Data=data,
        PartitionKey=partition_key,
    )

    logging.info("data stored in shard: " + response["ShardId"])

except ClientError as e:
    logging.error(e)




