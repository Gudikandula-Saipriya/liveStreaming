from flask import Flask, jsonify
import boto3
import json

app = Flask(__name__)

s3 = boto3.client('s3')
BUCKET = 'realtime-stream-processing'

@app.route('/')
def home():
    return "IoT Streaming Project Running 🚀"

@app.route('/data')
def get_data():
    objects = s3.list_objects_v2(Bucket=BUCKET, Prefix='processed/')
    
    data_list = []

    if 'Contents' in objects:
        for obj in objects['Contents']:
            key = obj['Key']
            if key.endswith('.json'):
                file_obj = s3.get_object(Bucket=BUCKET, Key=key)
                content = file_obj['Body'].read().decode('utf-8')
                data_list.append(json.loads(content))

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
