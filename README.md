# lambda-waterLevelAPI

## Overview
現在の河川の水位データを返します。  
水位データは10分毎に更新されます。

## Request
Method : GET  
Endpoint : /production/water-level/japan/tokyo/arakawa  
Path Parameter :   
1. japan : 国名を指定 ex)japan, taiwan
2. tokyo : 都道府県を指定 ex)tokyo, taipei
3. arakawa : 河川名を指定 ex)arakawa, danshui

## Response

以下の Json を返します。
~~~
{
  "riverName":"荒川",
  "height":"5.50",
  "timestamp":"2017-08-18T23:00:00Z",
  "waterLevel":"0.73",
  "dataTrend":"→",
  "dataLevel":0,
  "observatory":"東京都北区志茂5丁目 (新荒川大橋下流350m)"
}
~~~

riverName : 河川名前  
height : 川の防波堤の高さ  
timestamp : 観測時点の日時(UTC)  
waterLevel : 観測時点の水位  
dataTrend : 直前のデータより水位が上昇・下降したかどうか  
dataLevel : 水位の危険度  
observatory : 観測地点
