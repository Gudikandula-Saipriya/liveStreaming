import boto3
import json
import time
import random

kinesis = boto3.client('kinesis', region_name='ap-south-1')

STREAM_NAME = 'realtime-stream-process'

while True:
    data = {
        "device_id": "sensor-" + str(random.randint(1, 5)),
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 80)
    }

    print("Sending:", data)

    kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey=data["device_id"]
    )

    time.sleep(60)
