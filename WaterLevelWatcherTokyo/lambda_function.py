import datetime
import urllib.request
import boto3
import bs4
import re
import json

# 保存先のS3
S3_BUCKET = 'test-uodu-s3'
PREFIX = 'waterLevel/tokyo/arakawa/'
client = boto3.client('s3', region_name='ap-northeast-1')

def request_waterlevel():
    url = "http://www.river.go.jp/kawabou/ipSuiiKobetu.do?obsrvId=2128100400006&gamenId=01-1003&stgGrpKind=survOnly&fldCtlParty=no&fvrt=yes&timeType=10"
    #html = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml')
    html = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    return html

def html_parse(html):
    now = datetime.datetime.now()
    now.strftime("%Y-%m-%dT%H:%M:%S")

    riverName = format_text(html.find("td", class_="tb1td2").string)
    # 川の高さデータが参照先のページにないため、モック、一旦荒川の氾濫危険水位を
    height = "7.70"
    date = format_text(html.select("td.tb1td1Right")[-1].string)
    words = date.split(" ")
    yearmonth = words[0].split("/")
    timestamp = now.strftime("%Y") + "-" + yearmonth[0] + "-" + yearmonth[1] + "T" + words[1] + ":00"
    water_level = format_text(html.select("td.tb1td2Right")[-1].string)
    trend = format_text(html.select("td.tb1td1")[-1].string)
    # 危険度もないため、モック
    data_lovel = ""
    observatory = format_text(html.find("td", class_="tb1td2Left").get_text("|", strip=True))

    json_dict = {}
    json_dict['riverName'] = riverName
    json_dict['height'] = height
    json_dict['timestamp'] = timestamp
    json_dict['waterLevel'] = water_level
    json_dict['dataTrend'] = trend
    json_dict['dataLevel'] = data_lovel
    json_dict['observatory'] = observatory

    return json_dict

def format_text(text):
    text =re.sub('\r', "", text)
    text =re.sub('\n', "", text)
    text =re.sub('\t', "", text)
    return text

def put_s3(json_dict):
    words = json_dict['timestamp'].split("T")
    year = words[0].split("-")[0]
    month = words[0].split("-")[1]
    day = words[0].split("-")[2]
    time = words[1]
    key = PREFIX+"/"+year+"/"+month+"/"+day+"/"+time+".json"
    print(key)

    response = client.put_object(
        ACL='public-read',
        Body=json.dumps(json_dict),
        Bucket=S3_BUCKET,
        Key=key)

    return response

def lambda_handler(event, context):
    # ToDo:河川を引数で渡す
    html = request_waterlevel()
    
    # htmlをパースし、必要な情報をjsonに
    json_dict = html_parse(html)

    result = put_s3(json_dict)

    return result
