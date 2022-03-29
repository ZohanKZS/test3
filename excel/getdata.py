from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io
import pandas as pd
import openpyxl as op

def getDF():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'aerobic-factor-343013-31e041b499ba.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    results = service.files().list(pageSize=10,fields="nextPageToken, files(id, name, mimeType)").execute()

    idf=''
    for i in results['files']:
        if i['name']=='DataForBot.xlsx':
            idf=i['id']

    results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name, mimeType, parents, createdTime, permissions, quotaBytesUsed)").execute()
    file_id=idf

    request = service.files().get_media(fileId=file_id)
    fl = 'testLoc.xlsx'
    fh = io.FileIO(fl, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))

    xl = pd.ExcelFile(fl)

    df1 = xl.parse('Sheet1')

    # k=0
    # for n in range(0,df1.__len__()):
    #     print('---------'+n.__str__())
    #     for i in df1.loc[n]:
    #         # str(i.loc[k].array)
    #         print(i, end='        ')
    #         k+=1
    #     print('')

    return df1

class but1:
    def __init__(self,d,lng=''):
        delt=0
        if lng=='en':
            delt=23
            
        self.bt1=d.loc[2+delt][5]
        self.bt2=d.loc[6+delt][5]
        self.bt3=d.loc[10+delt][5]
        self.bt4=d.loc[14+delt][5]
        self.bt5=d.loc[18+delt][5]








