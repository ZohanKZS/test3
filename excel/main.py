from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io
import pandas as pd
import openpyxl as op

DAT=''

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = 'C:\Users\Admin\PycharmProjects\BotAioGram\aerobic-factor-343013-31e041b499ba2.json'
SERVICE_ACCOUNT_FILE = 'aerobic-factor-343013-31e041b499ba.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

results = service.files().list(pageSize=10,fields="nextPageToken, files(id, name, mimeType)").execute()

# pp.pprint('pp resuly - '+str(results))

idf=''
for i in results['files']:
    if i['name']=='DataForBot.xlsx':
        idf=i['id']

print(idf)

# exit()

# print('len files - '+str(len(results.get('files'))))


results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType, parents, createdTime, permissions, quotaBytesUsed)").execute()
# pp.pprint('pervy file - '+str(results.get('files')[0]))


# file_id = '1TxS_QAw-5GDU0boI3KWT7NjicdJxILlp'
# file_id = '1dHWpLEbpq-SNeYvFss-_e4ljykXGbsh7'
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

# Print the sheet names
# print(xl.sheet_names)

df1 = xl.parse('Sheet1')

sh='as;dlfkj --- '+str(df1.iat[0,0])

# print(sh)
# print(df1)

# sh=df1.loc[25]['k2']

# print(df1.iloc[1][1])
# print(sh)

k=0
for n in range(0,df1.__len__()):
    print('---------'+n.__str__())
    for i in df1.loc[n]:
        # str(i.loc[k].array)
        print(i, end='        ')
        k+=1
    print('')

# DAT=df1.iloc[3][1]






# request = service.files().export_media(fileId=file_id,
#                                              mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# filename = 'testLoc.xlsx'
# fh = io.FileIO(filename, 'wb')
# downloader = MediaIoBaseDownload(fh, request)
# done = False
# while done is False:
#     status, done = downloader.next_chunk()
#     print ("Download %d%%." % int(status.progress() * 100))