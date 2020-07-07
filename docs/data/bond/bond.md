## [mssdk](https://github.com/cdmaxsmart/mssdk) 债券数据

### 债券基础信息

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/mssdk/readme/index/bond_stock_index.png)

上图是利用 [mssdk](https://github.com/cdmaxsmart/mssdk) 的 **get_bond_bank** 函数获取的中国银行间
交易商协会发布的债券数据来绘制的, 可以在上面明确看出近几个月发债规模急速上升.

### 债券基础名词

#### 固定收益证券

是指持券人可以在特定的时间内取得固定的收益并预先知道取得收益的数量和时间, 如固定利率债券、优先股股票等.

#### 国债

国债又称国家公债, 是国家以其信用为基础, 按照债券的一般原则, 通过向社会发行债券筹集资金所形成的债权债务关系. 国债是中央政府为筹集财政资金而发行的一种政府债券, 由中央政府向投资者出具的、承诺在一定时期支付利息和到期偿还本金的债权债务凭证, 由于国债的发行主体是国家, 所以它具有最高的信用度, 被公认为是最安全的投资工具. 

### 债券基础数据

#### 银行间市场债券发行基础数据

银行间市场的债券发行数据是由交易商协会公布的的日级数据, 在很大程度上可以债券发行规模变化. 调用例子如下: 

接口: get_bond_bank

目标地址: http://zhuce.nafmii.org.cn/fans/publicQuery/manager

描述: 获取银行间债券市场数据

限量: 单次最大20行, 建议用 for 获取行数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| page_num | int  | Y    |  默认参数 page_num=1, 输入想要提取的页码, 多页提取请用 for 循环|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| firstIssueAmount   | str   | Y        | 金额(亿元)     |
| isReg        | str   | Y        | 是否注册, 显示为: 备案或者注册     |
| regFileName            | str   | Y        | 债券名称     |
| regPrdtType        | str   | Y        | 品种 |
| releaseTime      | float | Y        | 更新时间     |
| projPhase      | float | Y        | 项目阶段     |

接口示例

```python
import mssdk as ms
ms.get_bond_bank(page_num=1)
```

数据示例

```
   firstIssueAmount isReg                               regFileName  \
0                 9     1    淮南市产业发展(集团)有限公司关于发行2019年度第一期短期融资券的注册报告   
1                10     1          光大嘉宝股份有限公司关于发行2019年度第一期中期票据的注册报告   
2                15     1           西安高新控股有限公司关于发行2019年第二期中期票据的注册报告   
3                10     1          启迪控股股份有限公司关于发行2019年度第一期中期票据的注册报告   
4                 5     2  云南华电金沙江中游水电开发有限公司关于发行2019年度第二期短期融资券的注册报告   
5                 5     1       南京栖霞山旅游发展有限公司关于发行2019年度第一期中期票据的注册报告   
6                14     2   徐工集团工程机械有限公司关于发行2019年度第二期短期融资券的注册报告(备案)   
7                10     1      天津临港投资控股有限公司关于发行2019年度第一期超短期融资券的注册报告   
8                 2     1          中德联合集团有限公司关于发行2019年度第一期中期票据的注册报告   
9                10     1             浙江恒逸集团有限公司2019年度第七期超短期融资券注册报告   
10                5     1        西王集团有限公司关于发行2019-2021年度超短期融资券的注册报告   
11                5     1   荆州市城市建设投资开发有限公司关于注册发行2019年度第二期中期票据的注册报告   
12               10     1       招商局通商融资租赁有限公司关于发行2019年度第一期中期票据的注册报告   
13               15     1          中国旅游集团有限公司关于发行2019年度第四期中期票据的注册报告   
14               22     1     天津市保障住房建设投资有限公司关于发行2019年度第二期中期票据的注册报告   
15                5     1     余姚市城市建设投资发展有限公司关于发行2019年度第四期中期票据的注册报告   
16                5     2       四川蓝光发展股份有限公司关于发行2019年度第二期短期融资券的注册报告   
17                5     1      连云港市工业投资集团有限公司关于发行2019年度第二期中期票据的注册报告   
18               10     1        德州德达城市建设投资运营有限公司2019年度第一期中期票据的注册报告   
19                5     2   厦门经济特区房地产开发集团有限公司关于发行2019年度第一期中期票据的注册报告   

   regPrdtType          releaseTime projPhase  
0           CP  2019-10-12 00:00:00        20  
1          MTN  2019-10-12 00:00:00        20  
2          MTN  2019-10-12 00:00:00        20  
3          MTN  2019-10-12 00:00:00        20  
4           CP  2019-10-12 00:00:00        60  
5          MTN  2019-10-12 00:00:00        20  
6           CP  2019-10-12 00:00:00        60  
7          SCP  2019-10-12 00:00:00        20  
8          MTN  2019-10-12 00:00:00        20  
9          SCP  2019-10-12 00:00:00        30  
10         SCP  2019-10-12 00:00:00        20  
11         MTN  2019-10-12 00:00:00        20  
12         MTN  2019-10-12 00:00:00        20  
13          PN  2019-10-12 00:00:00        20  
14         MTN  2019-10-12 00:00:00        20  
15         MTN  2019-10-12 00:00:00        20  
16          CP  2019-10-12 00:00:00        20  
17         MTN  2019-10-12 00:00:00        20  
18         MTN  2019-10-12 00:00:00        20  
19          PN  2019-10-12 00:00:00        60
```

### 中国债券市场行情数据

#### 现券市场报价行情

接口: bond_spot_quote

目标地址: http://www.chinamoney.com.cn/chinese/mkdatabond/

描述: 提供中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-债券市场行情-现券市场报价行情

限量: 单次返回所有数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | - | - | - |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 债券简称      | str   | Y        |   |
| 报价机构      | str   | Y        |    |
| 买入/卖出净价(元)     | str   | Y        |     注意单位    |
| 买入/卖出收益率(%)        | str   | Y        |  注意单位  |

接口示例

```python
import mssdk as ms
bond_df = ms.bond_spot_quote()
print(bond_df)
```

数据示例

```
      债券简称  报价机构  债券简称       买入/卖出净价(元)      买入/卖出收益率(%)
0     19国开08  民生银行   99.93 / 100.35  3.4325 / 3.3325
1     19国开07  民生银行  100.16 / 100.39  3.1075 / 3.0075
2     19国开04  民生银行  100.42 / 100.97  3.6016 / 3.5016
3     19农发04  民生银行  100.36 / 100.76  3.4146 / 3.3146
4     19农发03  民生银行  100.20 / 100.42  3.1038 / 3.0038
      ...   ...              ...              ...
5344  16进出02  浦发银行  100.09 / 100.44  2.9849 / 2.6849
5345  16国开13  浦发银行    96.42 / 97.28  3.6601 / 3.5101
5346  16国开10  浦发银行    97.51 / 98.33  3.6270 / 3.4770
5347  16农发17  浦发银行  100.83 / 101.78  3.2717 / 2.9717
5348  15进出14  浦发银行  100.95 / 102.45  3.6823 / 3.3923
```

#### 现券市场成交行情

接口: bond_spot_deal

目标地址: http://www.chinamoney.com.cn/chinese/mkdatabond/

描述: 提供中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-债券市场行情-现券市场成交行情

限量: 单次返回所有即期数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | - | - | - |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 债券简称      | str   | Y        |   |
| 成交净价(元)      | float   | Y        |    |
| 最新收益率(%)      | float   | Y        |         |
| 涨跌(BP)        | float   | Y        |    |
| 加权收益率(%)      | float   | Y        |         |
| 交易量(亿)        | float   | Y        |    |

接口示例

```python
import mssdk as ms
bond_df = ms.bond_spot_deal()
print(bond_df)
```

数据示例

现券市场成交行情

```
             债券简称 成交净价(元) 最新收益率(%)  涨跌(BP) 加权收益率(%) 交易量(亿)
0          19国开15   98.97   3.5750    1.00   3.5826   None
1        19附息国债03   99.82   2.7714    0.14   2.7772   None
2        19附息国债11   99.87   2.8000    0.25   2.7963   None
3        19附息国债04  100.82   2.9832   -1.54   2.9747   None
4        15附息国债05  102.95   3.0359   -1.41   3.0359   None
           ...     ...      ...     ...      ...    ...
1673     19附息国债08  102.74   3.8750    0.50   3.8750   None
1674       15沪闵行债   61.52   3.6500    7.39   3.6500   None
1675  19桂林银行CD227   96.45   3.6494    0.55   3.6494   None
1676  15渝地产PPN001  100.86   3.8500  -55.27   3.8500   None
1677     15阿克苏信诚债   60.10   6.2306     NaN   6.2306   None
```

#### 国债及其他债券收益率曲线

接口: bond_china_yield

目标地址: http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2019-02-07&endDate=2020-02-04&gjqx=0&qxId=ycqx&locale=cn_ZH

描述: 提供中国债券信息网-国债及其他债券收益率曲线

限量: 单次返回所有指定日期间( **start_date** 到 **end_date** 需要小于一年)的所有数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| start_date | str | Y | start_date="2019-02-04", 指定开始日期 |
| end_date | str | Y | end_date="2020-02-04", 指定结束日期; **start_date** 到 **end_date** 需要小于一年 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 曲线名称      | str   | Y        |   |
| 日期      | str   | Y        |    |
| 3月      | float   | Y        |         |
| 6月        | float   | Y        |    |
| 1年      | float   | Y        |         |
| 3年        | float   | Y        |    |
| 5年        | float   | Y        |    |
| 7年        | float   | Y        |    |
| 10年        | float   | Y        |    |
| 30年        | float   | Y        |    |

接口示例

```python
import mssdk as ms
bond_china_yield_df = ms.bond_china_yield(start_date="2018-01-01", end_date="2019-01-01")
print(bond_china_yield_df)
```

数据示例

```
                    曲线名称          日期      3月  ...      7年     10年     30年
0              中债国债收益率曲线  2018-12-31  2.6153  ...  3.1641  3.2265  3.7056
1    中债商业银行普通债收益率曲线(AAA)  2018-12-31  2.9719  ...  4.1536  4.2202  4.5918
2      中债中短期票据收益率曲线(AAA)  2018-12-31  3.1667  ...  4.2589  4.3281   &nbsp
3              中债国债收益率曲线  2018-12-30  2.6153  ...  3.1641  3.2265  3.7056
4    中债商业银行普通债收益率曲线(AAA)  2018-12-30  2.9719  ...  4.1536  4.2202  4.5918
..                   ...         ...     ...  ...     ...     ...     ...
751  中债商业银行普通债收益率曲线(AAA)  2018-01-03  4.4477  ...  5.3384  5.3471  5.4737
752    中债中短期票据收益率曲线(AAA)  2018-01-03  4.7607  ...  5.4794  5.4879   &nbsp
753            中债国债收益率曲线  2018-01-02  3.7797  ...  3.9000  3.9008  4.3723
754  中债商业银行普通债收益率曲线(AAA)  2018-01-02  4.4379  ...  5.3180  5.3310  5.4577
755    中债中短期票据收益率曲线(AAA)  2018-01-02  4.8554  ...  5.4589  5.4718   &nbsp
```

#### 质押式回购-成交明细

接口: bond_repo_zh_tick

目标地址: http://stockhtm.finance.qq.com/sstock/ggcx/131802.shtml

描述: 提供债券-质押式回购-实时行情-成交明细

限量: 单次返回所有指定日期的成交明细数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| code | str | Y | code="sz131802", 指定质押式回购 |
| trade_date | str | Y | trade_date="20200207", 指定日期 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 成交时间      | str   | Y        |  时间: 09:25:04; |
| 成交价格      | float   | Y        |    |
| 价格变动      | float   | Y        |         |
| 成交量(手)        | float   | Y        |    |
| 成交额(元)      | float   | Y        |         |
| 性质        | str   | Y        | 买卖盘标记   |

接口示例

```python
import mssdk as ms
bond_repo_zh_tick_df = ms.bond_repo_zh_tick(code="sz131802", trade_date="20200207")
print(bond_repo_zh_tick_df)
```

数据示例

```
      成交时间  成交价格  价格变动  成交量(手)   成交额(元)  性质
0     09:25:04  2.40  1.17     284   284000  卖盘
1     09:30:05  2.70  0.30     985   985000  卖盘
2     09:30:27  2.70  0.00    1030  1030000  卖盘
3     09:30:30  2.70  0.00     200   200000  卖盘
4     09:30:57  2.50 -0.20     500   500000  卖盘
        ...   ...   ...     ...      ...  ..
1101  15:23:28  1.45  0.00      38    38000  卖盘
1102  15:24:55  1.45  0.00      25    25000  卖盘
1103  15:26:06  1.45  0.00      34    34000  卖盘
1104  15:26:54  1.45  0.00      59    59000  卖盘
1105  15:30:05  1.45  0.00      80    80000  卖盘
```

### 沪深债券

#### 实时行情数据

接口: bond_zh_hs_spot

目标地址: http://vip.stock.finance.sina.com.cn/mkt/#hs_z

描述: 沪深债券数据是从[新浪财经](http://vip.stock.finance.sina.com.cn/mkt/#hs_z)获取的数据

限量: 单次返回所有沪深债券的实时行情数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -    |   -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| ------------ | ----- | -------- | ---------------- |
| -          | -   | -        | 不逐一列出     |

接口示例

```python
import mssdk as ms
bond_zh_hs_spot_df = ms.bond_zh_hs_spot()
print(bond_zh_hs_spot_df)
```

数据示例

```
        symbol    code      name    trade  ... pb mktcap nmc turnoverratio
0     sh010107  010107     21国债⑺  102.990  ...  0      0   0             0
1     sh010303  010303     03国债⑶  102.620  ...  0      0   0             0
2     sh010504  010504     05国债⑷  108.510  ...  0      0   0             0
3     sh010512  010512     05国债⑿  101.500  ...  0      0   0             0
4     sh010609  010609     06国债⑼  100.000  ...  0      0   0             0
        ...     ...       ...      ...  ... ..    ...  ..           ...
6344  sz149027  149027    20荣安01    0.000  ...  0      0   0             0
6345  sz149028  149028  20CATL01    0.000  ...  0      0   0             0
6346  sz149029  149029    20圆融S1    0.000  ...  0      0   0             0
6347  sz149033  149033    20中证01    0.000  ...  0      0   0             0
6348  sz149034  149034    20中证02    0.000  ...  0      0   0             0
```

#### 历史行情数据

接口: bond_zh_hs_daily

目标地址: http://money.finance.sina.com.cn/bond/quotes/sh019315.html(示例)

描述: 历史行情数据是从[新浪财经](http://money.finance.sina.com.cn/bond/quotes/sh019315.html)获取的数据, 历史数据按日频率更新

限量: 单次返回具体某个沪深转债的所有历史行情数据(日频)

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| symbol | str  | Y    |   symbol="sh010107"|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| ------------ | ----- | -------- | ---------------- |
| date          | datetime   | Y        | -     |
| open          | float      | Y        | -     |
| high          | float      | Y        | -     |
| low           | float      | Y        | -     |
| close         | float      | Y        | -     |
| volume        | float      | Y        | -     |

接口示例

```python
import mssdk as ms
bond_zh_hs_daily_df = ms.bond_zh_hs_daily(symbol="sh010107")
print(bond_zh_hs_daily_df)
```

数据示例

```
               open     high      low    close    volume
date                                                    
2001-08-20  101.255  102.835  101.255  102.695  60765500
2001-08-21  102.743  103.213  102.683  103.133  19927710
2001-08-22  103.332  103.402  103.022  103.222  13132740
2001-08-23  103.260  103.300  103.080  103.110   9544530
2001-08-24  103.158  103.158  102.908  102.958   7068480
             ...      ...      ...      ...       ...
2020-02-07  102.890  102.970  102.890  102.920   1054710
2020-02-10  102.830  103.050  102.830  102.970   1367760
2020-02-11  102.970  103.500  102.880  102.880   1416580
2020-02-12  103.000  103.000  102.830  102.970   3021870
2020-02-13  102.940  103.040  102.880  102.920   1358700
```

### 沪深可转债

#### 实时行情数据

接口: bond_zh_hs_cov_spot

目标地址: http://vip.stock.finance.sina.com.cn/mkt/#hskzz_z

描述: 沪深可转债数据是从[新浪财经](http://vip.stock.finance.sina.com.cn/mkt/#hskzz_z)获取的数据

限量: 单次返回所有沪深可转债的实时行情数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -    |   -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| ------------ | ----- | -------- | ---------------- |
| -          | -   | -        | 不逐一列出     |

接口示例

```python
import mssdk as ms
bond_zh_hs_cov_spot_df = ms.bond_zh_hs_cov_spot()
print(bond_zh_hs_cov_spot_df)
```

数据示例

```
       symbol    code  name    trade  ... pb mktcap nmc turnoverratio
0    sh110031  110031  航信转债  126.760  ...  0      0   0             0
1    sh110033  110033  国贸转债  114.480  ...  0      0   0             0
2    sh110034  110034  九州转债  114.320  ...  0      0   0             0
3    sh110038  110038  济川转债  108.100  ...  0      0   0             0
4    sh110041  110041  蒙电转债  115.900  ...  0      0   0             0
..        ...     ...   ...      ...  ... ..    ...  ..           ...
222  sz128089  128089  麦米转债  129.410  ...  0      0   0             0
223  sz128090  128090  汽模转2  138.402  ...  0      0   0             0
224  sz128091  128091  新天转债  113.227  ...  0      0   0             0
225  sz128092  128092  唐人转债  113.500  ...  0      0   0             0
226  sz128093  128093  百川转债  109.305  ...  0      0   0             0
```

#### 历史行情数据

接口: bond_zh_hs_cov_daily

目标地址: http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=sh110048(示例)

描述: 历史行情数据是从[新浪财经](http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=sh110048)获取的数据, 历史数据按日频率更新

限量: 单次返回具体某个沪深可转债的所有历史行情数据(日频)

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| symbol | str  | Y    |   symbol="sh113542"|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| ------------ | ----- | -------- | ---------------- |
| date          | datetime   | Y        | -     |
| open          | float      | Y        | -     |
| high          | float      | Y        | -     |
| low           | float      | Y        | -     |
| close         | float      | Y        | -     |
| volume        | float      | Y        | -     |

接口示例

```python
import mssdk as ms
bond_zh_hs_cov_daily_df = ms.bond_zh_hs_cov_daily(symbol="sh113542")
print(bond_zh_hs_cov_daily_df)
```

数据示例

```
              open    high     low   close   volume
date                                               
2019-08-23  103.88  110.60  103.88  108.45  3957700
2019-08-26  108.40  108.40  106.19  107.68   444490
2019-08-27  107.67  109.01  107.54  108.68   327110
2019-08-28  108.12  109.02  108.10  109.00   129100
2019-08-29  108.68  108.99  108.56  108.71    69900
            ...     ...     ...     ...      ...
2020-02-07  111.76  112.30  111.51  112.10    33420
2020-02-10  111.51  113.55  111.00  111.72    12650
2020-02-11  111.72  113.73  111.12  113.00    18320
2020-02-12  113.00  114.80  112.88  113.10    22970
2020-02-13  112.10  114.23  111.15  112.17    24010
```

#### 可转债数据一览表

接口: bond_zh_cov

目标地址: http://data.eastmoney.com/kzz/default.html

描述: 东方财富网-数据中心-新股数据-可转债数据一览表

限量: 单次返回当前交易时刻的所有可转债数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -    |   -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| ------------ | ----- | -------- | ---------------- |
| 债券代码          | str   | Y        | -     |
| 交易场所          | str      | Y        | -     |
| 债券简称          | str      | Y        | -     |
| 申购日期           | str      | Y        | -     |
| 申购代码         | str      | Y        | -     |
| 正股代码        | str      | Y        | -     |
| 正股简称        | str      | Y        | -     |
| 债券面值        | float      | Y        | -     |
| 发行价格        | float      | Y        | -     |
| 转股价        | float      | Y        | -     |
| 中签号发布日        | str      | Y        | -     |
| 中签率        | float      | Y        | 注意单位: %     |
| 上市时间        | str      | Y        | -     |
| 备忘录        | str      | Y        | -     |
| 正股价        | float      | Y        | -     |
| 市场类型        | float      | Y        | -     |
| 股权登记日        | str      | Y        | -     |
| 申购上限        | float      | Y        | 注意单位: 万元     |
| 转股价值        | float      | Y        | -     |
| 债现价        | float      | Y        | -     |
| 转股溢价率        | float      | Y        | 注意单位: %     |
| 每股配售额        | float      | Y        | -     |
| 发行规模        | float      | Y        | 注意单位: 亿元     |

接口示例

```python
import mssdk as ms
bond_zh_cov_df = ms.bond_zh_cov()
print(bond_zh_cov_df)
```

数据示例

```
       债券代码    交易场所   债券简称  ...              转股溢价率   每股配售额     发行规模
0    128108  CNSESZ   蓝帆转债  ...  -9.46564885496219  3.2613  31.4404
1    113582  CNSESH   火炬转债  ...  -2.20077220077219   1.329        6
2    113035  CNSESH   福莱转债  ...  0.147710487444574   0.966     14.5
3    113581  CNSESH   龙蟠转债  ...              12.84   1.321        4
4    113580  CNSESH   康隆转债  ...               7.67       2        2
..      ...     ...    ...  ...                ...     ...      ...
377  110227  CNSESH   赤化转债  ...                  -     2.4      4.5
378  126006  CNSESH  07深高债  ...                  -     1.8       15
379  110971  CNSESH   恒源转债  ...                  -       1        4
380  110567  CNSESH   山鹰转债  ...                  -     1.1      4.7
381  110026  CNSESH   中海转债  ...                  -     0.9       20
```

#### 可转债比价表

接口: bond_cov_comparison

目标地址: http://quote.eastmoney.com/center/fullscreenlist.html#convertible_comparison

描述: 东方财富网-行情中心-债券市场-可转债比价表

限量: 单次返回当前交易时刻的所有可转债比价数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| - | -  | -   |   -|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| ------------ | ----- | -------- | ---------------- |
| 最新价          | float   | Y        | -     |
| 涨跌幅          | float      | Y        | -     |
| 转债代码          | str      | Y        | -     |
| 转债名称           | str      | Y        | -     |
| 上市日期         | str      | Y        | -     |
| 纯债价值        | float      | Y        | -     |
| 涨跌幅        | float      | Y        | -     |
| 正股代码        | str      | Y        | -     |
| 正股名称        | str      | Y        | -     |
| 转股价        | float      | Y        | -     |
| 转股价值        | float      | Y        | -     |
| 转股溢价率        | float      | Y        | 注意单位: %     |
| 纯债溢价率        | float      | Y        | 注意单位: %     |
| 回售触发价        | float      | Y        | -     |
| 强赎触发价        | float      | Y        | -     |
| 到期赎回价        | float      | Y        | -     |
| 开始转股日        | str      | Y        | -     |
| 申购日期        | str      | Y        | -     |

接口示例

```python
import mssdk as ms
bond_cov_comparison_df = ms.bond_cov_comparison()
print(bond_cov_comparison_df)
```

数据示例

```
        最新价   涨跌幅    涨跌幅    转债代码  转债名称  ...  回售触发价  强赎触发价  到期赎回价     开始转股日      申购日期
0         -     -  10.02  128108  蓝帆转债  ...  12.45  23.13    108  20201203  20200528
1         -     -   3.11  113582  火炬转债  ...  17.73  32.93    110  20201202  20200527
2         -     -   2.19  113035  福莱转债  ...   9.49  17.63    115  20201203  20200527
3    107.79  0.99    1.1  113581  龙蟠转债  ...   6.73  12.49    120  20201029  20200423
4     109.7  1.28   2.26  113580  康隆转债  ...  17.12  31.79    115  20201029  20200423
..      ...   ...    ...     ...   ...  ...    ...    ...    ...       ...       ...
254   107.8 -0.02   0.42  113009  广汽转债  ...  10.09  18.73    106  20160722  20160122
255  114.34  3.31   1.55  110034  九州转债  ...  12.82  23.82    108  20160721  20160115
256  108.85  0.51   0.49  110033  国贸转债  ...   5.19   9.65    108  20160705  20160105
257  110.29  0.01    1.2  110031  航信转债  ...  15.25  28.33    107  20151214  20150612
258  107.19  0.18   0.92  113008  电气转债  ...   3.59   6.67  106.6  20150803  20150202
```

### 全球债券行情数据

接口: bond_investing_global

目标地址: https://cn.investing.com/rates-bonds/

描述: 获取全球政府债券行情与收益率, 由于涉及国家和债券多(**近1000**个债券)具体参见[国家-债券目录](https://cn.investing.com/rates-bonds/world-government-bonds?maturity_from=10&maturity_to=310)

具体的调用方式可以参照: 

1. 先查询指数所在的国家名称;
2. 复制网页上国家名称(推荐复制), 如 **中国**;
3. 复制所显示的具体债券名称(推荐复制, 如果英文中间有空格, 也需要保留空格), 如 **中国1年期国债**; 也可以调用 **ms.bond_investing_global_country_name_url(country="美国")** 获取需要国家的具体指数名称
4. 在安装 [mssdk](https://github.com/cdmaxsmart/mssdk) 后输入, 如 **ms.bond_investing_global(country="中国", index_name="中国1年期国债", period="每周", start_date="2000-01-01", end_date="2020-06-06")**;
5. 稍后就可以获得所需数据.

限量: 单次返回某一个国家的具体某一个指数, 建议用 for 循环获取多个国家的多个指数, 注意不要大量获取, 以免给对方服务器造成压力!

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| country | str  | Y    |   country="中国"|
| index_name | str  | Y    |  index_name="中国1年期国债"; 可以通过 ms.bond_investing_global_country_name_url(country="美国") 获取|
| period | str  | Y    |  period="每月"; choice of {"每日", "每周", "每月"}|
| start_date | str  | Y    |  start_date='2000/01/01'|
| end_date | str  | Y    |  end_date='2019/10/17'|

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期索引  |
| 收盘      | float   | Y        | 收盘   |
| 开盘      | float   | Y        | 开盘        |
| 高        | float   | Y        |高    |
| 低         | float | Y        | 低         |
| 交易量      | str | Y        | 涨跌幅, 注意单位: %      |

接口示例

```python
import mssdk as ms
bond_investing_global_df = ms.bond_investing_global(country="中国", index_name="中国1年期国债", period="每周", start_date="2000-01-01", end_date="2020-06-06")
print(bond_investing_global_df)
```

数据示例

```
            收盘     开盘      高      低    涨跌幅
日期                                           
2020-05-31  1.720  1.543  1.720  1.543   6.77
2020-05-24  1.611  1.500  1.611  1.500   7.40
2020-05-17  1.500  1.400  1.500  1.400  21.95
2020-05-10  1.230  1.217  1.300  1.217   0.99
2020-05-03  1.218  1.210  1.227  1.180   6.56
           ...    ...    ...    ...    ...
2002-07-07  2.020  2.020  2.020  2.020  -0.30
2002-06-30  2.026  2.026  2.026  2.026   3.21
2002-06-23  1.963  1.963  1.963  1.963   1.19
2002-06-16  1.940  1.940  1.940  1.940   0.88
2002-06-09  1.923  1.923  1.923  1.923   0.52
```