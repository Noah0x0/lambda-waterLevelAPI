import json
import urllib.parse
import boto3
import datetime

bucket = 'test-uodu-s3'
target = 'waterLevel'

client = boto3.client('s3')

def get_latest_keyname(prefix):
    # 国・都道府県・川名別の一覧を取得
    list = client.list_objects(
        Bucket=bucket,
        Prefix=prefix
    )
    
    # 最も更新日が新しいものを取得
    if 'Contents' in list:
        keys = {}
        for content in list['Contents']:
            keys[content['Key']] = content['LastModified']
    target_key = max(keys, key=(lambda x: keys[x]))
    
    return target_key

def get_waterlevel(target_key):
    response = client.get_object(Bucket=bucket, Key=target_key)

    body = response['Body'].read().decode('utf-8')
    #json_str = json.loads(body)
        
    return body

def set_response_body(status_code, body):
    headers = {}
    headers['Content-Type'] = 'application/json'

    res_body = {}
    res_body['statusCode'] = status_code
    res_body['headers'] = headers
    res_body['body'] = body
    
    return res_body

def lambda_handler(event, context):
    print(event)
    # prefix用に年月取得
    now = datetime.datetime.now()
    year = str(now.strftime('%Y'))
    month = str(now.strftime('%m'))
    
    params = event['queryStringParameters']
    # パラメータが不正な場合のデフォルトを荒川に
    if (set(params) >= {'country', 'prefectures', 'river'}):
        country = params['country'] if len(params['country']) != 0 else 'japan'
        prefectures = params['prefectures'] if len(params['prefectures']) != 0 else 'tokyo'
        river = params['river'] if len(params['river']) != 0 else 'arakawa'
        prefix = target + '/' + country + '/' + prefectures + '/' + river + '/' + year + '/' + month + '/'
    else:
        prefix = 'waterLevel/japan/tokyo/arakawa/' + year + '/' + month + '/'
    
    try:
        # 最新のファイル名を取得
        target_key = get_latest_keyname(prefix)
        # ファイル名をkeyとしてS3からデータ取得
        json_str = get_waterlevel(target_key)
        
        return set_response_body(200, json_str)
    except Exception as e:
        print(e)
        return set_response_body(400, 'Bad Request')
