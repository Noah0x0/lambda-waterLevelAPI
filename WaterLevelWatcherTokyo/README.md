# lambda-waterLevelWatcher

## Overview
「川の防災情報」サイトから河川の水位情報を取得し、S3へJSONを保存する。
10分に1度作成される。

## JSON Format
以下の形式で保存しています。
~~
{
  "riverName":"荒川",
  "height": "7.70",
  "timestamp": "20170814T15:00:00",
  "waterLevel": "0.73",
  "dataTrend": "→",
  "dataLevel": "",
  "observatory":"岩淵水門（上）"
}
~~
