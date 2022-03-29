import requests
from lxml import html, etree
from bs4 import BeautifulSoup as BS
import re

URL_LOG = "https://www.it4profit.com/login/authorize2.jsp"
URL_MAIN_ = "https://www.it4profit.com/purchasing/apps/supplyMng/app.jsp#/supplyBB?isLoad=1&supplier=&brand=&df=15%2F02%2F2022&dt=08%2F03%2F2022&productType=&productCat=&article=&shipTo=&supplierStatus=15201&reserve=&condition=&salesMng=190122034647732192&batch=&poId=&poNum=&whs=1&cargo=&stockAge=&tmpl=&stockSummary=0&fModel=%7B%7D&filterProductType=1"
URL_MAIN ="https://www.it4profit.com/purchasing/supply_management_table.jsp?EMAIL=zakhar.korzhov%40asbck.kz&RPP=10000&RS=0&AR=off&AR_INT=180000&qaz=1&USER_ID=190122034647732192&USER_ID_C13=20190122034647734523000000&USER_ID_C13RES=20190122034647734523000000&SF=1&AE_CH=1&MNF=&SELLER=&COND=701&PT=&PC=&WHS_TO=&SUP_KIND=&USER_ID2RES=190122034647732192&ART=MV7&SUP_STAT=15201&DF=27%2F01%2F2022&DT=17%2F02%2F2022&STOCK_AGE=&BATCH=&PO_NUM=&CARGO_NUM=&DT_ID=3"
LOGIN = "78717944"
PASSWORD = "Ba2019oV"


def parseDet(rr):
    # URL = 'https://www.olx.kz/list/q-samsung-note-10-plus/'
    # HEADERS = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    # }


    # res = requests.get(URL)


    soup = BS(rr.content, 'html.parser')
    #   but=soup.prettify()
    #   print(but)
    # items = soup.findAll(id='ROW_')
    items=soup.findAll(class_='td')

    k=0
    for it in items:
        if k<=1:
            k+=1
            continue

        d=it.findAll('td')

        print('{4}  art-{0}  bach-{1}  wh-{2}  qty-{3}'.format(
            d[0].text.strip(),
            d[4].text.strip(),
            d[7].text.strip(),
            d[18].text.strip(),
            k
        ))
        k+=1




s = requests.Session()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

result = requests.get(URL_LOG, headers=headers)
#tree = html.fromstring(result.text)

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
parseDet(r2)

# print(r1.url)
# print('******************************************************************************************************************************************')
# print(r2.content)


