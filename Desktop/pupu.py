import random
import time
import requests
import urllib3
import datetime
# 用Fiddler爬取用户代理和商品地址
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/ccac09fa-5171-4f1e-9263-e731be3400d7'


# 根据url申请请求头
def getPupu():
    # 设计获取价格波动时间

    result = requests.get(url, headers=headers, verify=False)
    return result
    randoms=random.randint(2,6)
    time.sleep(randoms)


# 运用json方法解析字典
result = getPupu()
orange = result.json()
TradeName = orange['data']['name']
TradeSpec = orange['data']['spec']
TradePrice = orange['data']['price']/100
market_price = orange['data']['market_price']/100
title = orange['data']['share_content']

# 输出商品规格
print("-------------------商品: "+TradeName+"-------------------------------")
print("规格: "+TradeSpec)
print("价格: "+str(TradePrice))
print("原价/折扣价: "+str(market_price)+"/"+str(TradePrice) )
# print("详细内容: "+title)
print("-------------------------商品: "+TradeName+"的价格波动--------------------------------")


# 运用while()循环实现价格波动
if __name__ == '__main__':
    while (1):
        result = getPupu()
        TradePrice = orange['data']['price']
        time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("当前时间为" +time+ ", 价格为" + str(TradePrice/100))
