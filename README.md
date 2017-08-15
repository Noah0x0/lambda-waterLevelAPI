# lambda-waterLevelAPI

## Overview
現在の河川の水位を返します。  
水位データは10分毎に更新されます。

## Request
Method : GET  
Endpoint : /production/water-level?country="japana"&prefectures="tokyo"&river="arakawa"  
Parameter :   
1. country : 国名
2. prefectures : 都道府県
3. river : 河川名

## Response

以下の Json を返します。
~~~
{
  "riverName":"浅野川",
  "height":"5.50",
  "timestamp":"08月12日 15時30分",
  "waterLevel":"0.73",
  "dataTrend":"→",
  "dataLevel":0,
  "observatory":"金沢市沖橋(諸江)"
}
~~~

riverName : 川の名前  
height : 川の防波堤の高さ  
timestamp : 観測時点の日時  
waterLevel : 観測時点の水位  
dataTrend : 直前のデータより水位が上昇・下降したかどうか
dataLevel : 水位の危険度
observatory : 観測地点
