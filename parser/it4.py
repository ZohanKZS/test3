import requests
from bs4 import BeautifulSoup as BS

adr='https://www.it4profit.com/purchasing/apps/supplyMng/app.jsp#/supplyBB?isLoad=1&supplier=&brand=&df=15%2F02%2F2022&dt=08%2F03%2F2022&productType=&productCat=&article=&shipTo=&supplierStatus=15201&reserve=&condition=&salesMng=190122034647732192&batch=&poId=&poNum=&whs=1&cargo=&stockAge=&tmpl=&stockSummary=0&fModel=%7B%7D&filterProductType=1'
adr1='https://www.it4profit.com/login/authorize2.jsp'

r=requests.post(adr1)
html=BS(r.content,'html.parser')

# for el in html.select('.ag-body-container > .ag-cell ag-cell-not-inline-editing ag-cell-no-focus ag-cell-value ng-scope'):
#     tit=el.select('.caption > a')
#     print(tit[0].text)

print(html.title)




