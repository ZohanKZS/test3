import requests
from lxml import html, etree

URL_LOG = "https://www.it4profit.com/login/authorize2.jsp"
URL_MAIN = "https://www.it4profit.com/purchasing/apps/supplyMng/app.jsp#/supplyBB?isLoad=1&supplier=&brand=&df=15%2F02%2F2022&dt=08%2F03%2F2022&productType=&productCat=&article=&shipTo=&supplierStatus=15201&reserve=&condition=&salesMng=190122034647732192&batch=&poId=&poNum=&whs=1&cargo=&stockAge=&tmpl=&stockSummary=0&fModel=%7B%7D&filterProductType=1"
LOGIN = "78717944"
PASSWORD = "Ba2019oV"




s = requests.Session()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

result = requests.get(URL_LOG, headers=headers)
tree = html.fromstring(result.text)
#authURL = list(set(tree.xpath("//input[@name='authURL']/@value")))[0]

# print(authURL)

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "73",
    "Content-Type": "application/x-www-form-urlencoded",
    #"Cookie": "JSESSIONID=0022Xi-x4dIpoUiPyn_wrGaDC_3:-1",
    "Host": "www.it4profit.com",
    "Origin": "https://www.it4profit.com",
    "Referer": "https://www.it4profit.com/login",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

data = {
    "USERNAME": LOGIN,
    "PASSWORD": PASSWORD,
    "rememberMe": "false",
    "flow": "websiteSignUp",
    "mode": "login",
    "action": "loginAction",
    "withFields": "rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode",
    #"authURL": authURL,
    "nextPage": URL_MAIN,
    "showPassword": "",
    #"countryCode": "+49",
    #"countryIsoCode": "DE"
}

r1 = s.post(URL_LOG, data=data, headers=headers)
r2 = s.get(URL_MAIN)

print(r1.url)
print('******************************************************************************************************************************************')
print(r2.content)


