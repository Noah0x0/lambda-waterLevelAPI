# lambda-waterLevelAPI

## Overview
現在の河川の水位を返します。  
水位データは10分毎に更新されます。

## Request
Method : GET  
Endpoint : /production/water-level  
Parameter : ComingSoon  

## Response

以下の Json を返します。
~~~
{
   "riverName": "浅野川",
   "height": "5.50",
   "timestamp": "2017-08-11-14-30",
   "waterLevel": "0.48",
   "latestDate": {
     "obsTime": "14時30分",
     "4_10": {
      "dataStr": "0.48",
      "cssStr": "stageLevel0",
      "dataTrend": "↑",
      "dataLevel": 0
    }
  }
}
~~~

riverName : 川の名前  
height : 川の防波堤の高さ  
timestamp : 観測時点の日時  
waterLevel : 観測時点の水位  
latestDate : 最新情報  
