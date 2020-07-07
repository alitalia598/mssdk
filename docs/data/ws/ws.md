## import mssdk as ms实时监控

### Websocket-外汇

接口: watch_jinshi_fx

目标地址: https://datacenter.jin10.com/market

描述: 获取商品、外汇、股市、美股、国债、指数实时行情数据, 如需要存储数据请修改 **on_message** 接口

限量: 主动推送

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -    |  -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| -     | -   | -        | 基于 websocket 的接口  |  

接口示例

```python
import mssdk as ms
ms.watch_jinshi_fx()
```

数据示例

```
42["price",{"c":"USDSEK","n":"美元/瑞典克朗","t":2,"lp":9.63381,"ch":-0.00548,"chp":-0.06}]
42["price",{"c":"USDTRY","n":"美元/土耳其里拉","t":2,"lp":5.7359,"ch":-0.0064}]
42["price",{"c":"CADCHF","n":"加元/瑞郎","t":2,"lp":0.74865,"ch":0.00076,"chp":0.1}]
42["price",{"c":"AUDUSD","n":"澳元/美元","t":2,"lp":0.68114,"ch":-0.00052,"chp":-0.08}]
42["price",{"c":"UKX","n":"英国富时100指数","t":3,"lp":7309,"ch":6.1}]
42["price",{"c":"AUDNZD","n":"澳元/纽元","t":2,"lp":1.06348,"ch":-0.00134,"chp":-0.13}]
42["price",{"c":"AUDNZD","n":"澳元/纽元","t":2,"lp":1.06369,"ch":-0.00113,"chp":-0.11}]
42["price",{"c":"XAUUSD","n":"现货黄金","t":1,"lp":1459.18,"ch":-8.74,"chp":-0.6}]
42["price",{"c":"AUDNZD","n":"澳元/纽元","t":2,"lp":1.06346,"ch":-0.00136,"chp":-0.13}]
42["price",{"c":"USDCAD","n":"美元/加元","t":2,"lp":1.3217,"ch":-0.00035,"chp":-0.03}]
42["price",{"c":"AUDNZD","n":"澳元/纽元","t":2,"lp":1.06347,"ch":-0.00135}]
42["price",{"c":"AUDNZD","n":"澳元/纽元","t":2,"lp":1.06369,"ch":-0.00113,"chp":-0.11}]
```

### Websocket-行情

接口: watch_jinshi_quotes

目标地址: https://datacenter.jin10.com/price_wall

描述: 获取股市、外汇、商品、工行、农行实时行情数据, 如需要存储数据请修改 **on_message** 接口

限量: 主动推送

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -    |  -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| -     | -   | -        | 基于 websocket 的接口  |  

接口示例

```python
import mssdk as ms
ms.watch_jinshi_quotes()
```

数据示例

```
42["rec_advanced",["USDZAR",17.3842,17.53028,17.25585,17.2754,22120]]
42["rec_advanced",["EURTRY",7.7123,7.71875,7.66637,7.69485,22613]]
42["rec_advanced",["DXY",97.226,97.597,97.163,97.35,22420]]
42["rec_advanced",["COPPER",2.6415,2.663,2.62888,2.644,8655]]
42["rec_advanced",["GBPCHF",1.1764,1.18245,1.17586,1.1766,26319]]
42["rec_advanced",["USDCAD",1.36361,1.36662,1.36076,1.36426,23895]]
42["rec_advanced",["EURCAD",1.53422,1.53538,1.5268,1.53177,31955]]
42["rec_advanced",["EURNZD",1.75421,1.75743,1.74322,1.74677,28648]]
```

### 阿尔戈斯全网监控

接口: watch_argus

目标地址: https://www.quantinfo.com/Argus/

描述: 获取期货、股票、期权、大宗商品、外汇等价格波动及相关资讯

限量: 发起请求后返回数据，注意访问频率

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -    |  -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| count     | int   | Y        | 使用了多少条新闻  |  
| time     | str   | Y        |  最后一条新闻时间  |  
| label     | int   | Y        | 分类ID  |  
| name     | str   | Y        | 分类名称  |  
| predict     | float   | Y        | 上涨概率，大于0.5倾向于上涨  |  

接口示例

```python
import mssdk as ms
watch_argus_df = ms.watch_argus()
print(watch_argus_df)
```

数据示例

```
    predict  count label  name                      time
0    0.1376    3.0     1    黄金 2020-04-08 14:43:00+08:00
1    0.2961   12.0     2    白银 2020-04-08 15:03:44+08:00
2    0.2961   12.0     3    甲醇 2020-04-08 15:03:44+08:00
3    0.2961   12.0     4     铝 2020-04-08 15:03:44+08:00
4    0.2961   12.0     5    塑料 2020-04-08 15:03:44+08:00
5    0.2961   12.0     6    PP 2020-04-08 15:03:44+08:00
6    0.2961   12.0     7     锌 2020-04-08 15:03:44+08:00
7    0.0100    1.0     8     铜 2020-04-08 14:42:06+08:00
8    0.2961   12.0     9     镍 2020-04-08 15:03:44+08:00
9    0.2961   12.0    10     锡 2020-04-08 15:03:44+08:00
10   0.2961   12.0    11     铅 2020-04-08 15:03:44+08:00
11   0.2215    5.0    12    原油 2020-04-08 14:55:01+08:00
12   0.2442    1.0    13  股指期货 2020-04-08 15:03:44+08:00
13   0.9900    1.0    14    大豆 2020-04-08 15:01:02+08:00
14   0.1733    1.0    15    棉花 2020-04-08 14:59:32+08:00
15   0.2961   12.0    16    煤炭 2020-04-08 15:03:44+08:00
16   0.2961   12.0    17    玉米 2020-04-08 15:03:44+08:00
17   0.2961   12.0    18   铁矿石 2020-04-08 15:03:44+08:00
18   0.2961   12.0    19   PTA 2020-04-08 15:03:44+08:00
19   0.2961   12.0    20   棕榈油 2020-04-08 15:03:44+08:00
20   0.2961   12.0    21    钢铁 2020-04-08 15:03:44+08:00
21   0.2961   12.0    22  菜油菜粕 2020-04-08 15:03:44+08:00
22   0.2961   12.0    23    债券 2020-04-08 15:03:44+08:00
23   0.2961   12.0    24    锰硅 2020-04-08 15:03:44+08:00
24   0.2961   12.0    25    苹果 2020-04-08 15:03:44+08:00
25   0.2961   12.0    26    白糖 2020-04-08 15:03:44+08:00
26   0.2961   12.0    27    鸡蛋 2020-04-08 15:03:44+08:00
27   0.2961   12.0    28   PVC 2020-04-08 15:03:44+08:00
28   0.2961   12.0    29    小麦 2020-04-08 15:03:44+08:00
29   0.2961   12.0    30     稻 2020-04-08 15:03:44+08:00
30   0.2961   12.0    31    玻璃 2020-04-08 15:03:44+08:00
31   0.2961   12.0  1001   比特币 2020-04-08 15:03:44+08:00
32   0.2961   12.0  1002   莱特币 2020-04-08 15:03:44+08:00
33   0.2961   12.0  1003   以太坊 2020-04-08 15:03:44+08:00
34   0.2961   12.0  1004   EOS 2020-04-08 15:03:44+08:00
35   0.2961   12.0   all    所有 2020-04-08 15:03:44+08:00
```