import requests
from bs4 import BeautifulSoup as BS

s = requests.session()

auth_html = s.get('https://www.it4profit.com/login/logon.jsp?REFPAGE=%2Fadmin%2Fcompany%2Fuser_list.jsp')

auth_bs = BS(auth_html.content, 'html.parser')

# crf = auth_bs.select('input[name="ancor"]')[0]['value']

payLoad = {
    "PASSWORD": "Aa123456",
    "USERNAME": "78718088"
}

answ = s.post('https://www.it4profit.com/login/authorize2.jsp', data=payLoad)
answ_bs = BS(answ.content, 'html.parser')

# crf=answ_bs.select()

print(answ.content)
