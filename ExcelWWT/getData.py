from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io
import pandas as pd
import openpyxl as op


def getDF():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'wwtech-4db078c1e265.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()

    idf = ''
    for i in results['files']:
        if i['name'] == 'DataForBot.xlsx':
            idf = i['id']

    results = service.files().list(
        pageSize=10,
        fields="nextPageToken, files(id, name, mimeType, parents, createdTime, permissions, quotaBytesUsed)").execute()
    file_id = idf

    request = service.files().get_media(fileId=file_id)
    fl = 'testLoc.xlsx'
    fh = io.FileIO(fl, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        # print ("Download %d%%." % int(status.progress() * 100))

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


def getDFLocal():
    fl = 'testLoc.xlsx'

    xl = pd.ExcelFile(fl)

    df1 = xl.parse('Sheet1')

    return df1


class but1:
    def __init__(self, d, lng=''):
        delt = 0
        if lng == 'en':
            delt = 23

        self.bt1 = d.loc[2 + delt][5]
        self.bt2 = d.loc[6 + delt][5]
        self.bt3 = d.loc[10 + delt][5]
        self.bt4 = d.loc[14 + delt][5]
        self.bt5 = d.loc[18 + delt][5]


def celp(df, x, y):
    return print(df.loc[x - 1][y - 2])


def cel(df, x, y):
    if x - 1 < 0 or y - 2 < 0:
        return ''
    else:
        return df.loc[y - 2][x - 1]






