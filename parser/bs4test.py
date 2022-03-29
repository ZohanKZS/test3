import requests
from bs4 import BeautifulSoup as BS


def parse():
    URL = 'https://www.olx.kz/list/q-samsung-s22-ultra/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }

    # res=requests.get(URL,headers=HEADERS)
    res = requests.get(URL)
    soup = BS(res.content, 'html.parser')
    items1 = soup.findAll('div', class_='offer-wrapper')
    # items1 = soup.findAll('h3', class_='lheight22 margintop5')

    comps = []

    for item1 in items1:

        it =hr = ''
        pr = 0
        if item1.find('a', class_='marginright5 link linkWithHash detailsLink') != None:
            it = item1.find('a', class_='marginright5 link linkWithHash detailsLink').get_text(strip=True)
            hr = item1.find('a', class_='marginright5 link linkWithHash detailsLink').get('href')
        if item1.find('p', class_='price') != None:
            pr = item1.find('p', class_='price').get_text(strip=True)



        if pr!=0 and it!=None:
            comps.append({
                'title': it,
                'price': pr,
                'link': hr
            })

    for comp in comps:
        adr=comp['link']
        print(f"{comp['title']} ------------>  {comp['price']}  -------->  {comp['link']}")
        if adr.strip()!='':
            print('------------------------------------------------------------------------------------')
            print(parseDet(adr))
            print('------------------------------------------------------------------------------------')
            print('')
            print('')
            print('')


    # print(dir(it))
def parseDet(URL):
    # URL = 'https://www.olx.kz/list/q-samsung-note-10-plus/'
    # HEADERS = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    # }


    res = requests.get(URL)
    soup = BS(res.content, 'html.parser')
    items1 = soup.findAll('div', class_='css-g5mtbi-Text')

    # s=''
    # if len(items1)!=0:
    #     s=items1[0].text



    # return
    s = (items1[0].text if len(items1)!=0 else '')
    return print(s)

    # print(dir(it))


parse()
# ur='https://www.olx.kz/d/obyavlenie/samsung-note-10plus-256gb-IDlPwsV.html#687f19f33f'
# ur='https://www.olx.kz/d/obyavlenie/samsung-galaxy-note-10-plus-petropavlovsk-mira-IDlRLgu.html#eb53ee22e9'
# parseDet(ur)
