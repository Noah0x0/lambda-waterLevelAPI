import json
import urllib.parse
import boto3

print('Loading function')

client = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'test-uodu-s3'
    key = 'waterLevel.json'
    try:
        response = client.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read().decode('utf-8')
        json_dict = json.loads(body)
        
        result_dict = {}
        result_dict['riverName'] = json_dict['masterData']['riverName']
        result_dict['height'] = json_dict['customData']['stageAlarmLv7']
        result_dict['latestDate'] = json_dict['timeLineData'][-1]
        
        # print(result_dict)

        return result_dict
    except Exception as e:
        print(e)
        # print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        return 'InternalServerError'
