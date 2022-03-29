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
SERVICE_ACCOUNT_FILE = 'C:\Users\Admin\PycharmProjects\BotAioGram\aerobic-factor-343013-31e041b499ba2.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

results = service.files().list(pageSize=10,fields="nextPageToken, files(id, name, mimeType)").execute()

pp.pprint('pp resuly - '+str(results))

print('len files - '+str(len(results.get('files'))))


results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType, parents, createdTime, permissions, quotaBytesUsed)").execute()
pp.pprint('pervy file - '+str(results.get('files')[0]))


file_id = '1TxS_QAw-5GDU0boI3KWT7NjicdJxILlp'

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
print(xl.sheet_names)

df1 = xl.parse('Sheet1')

# sh=df1.iat[46,2]

# print(sh)
print(df1)

# sh=df1.loc[1]['22']

print(df1.iloc[3][1])


DAT=df1.iloc[3][1]






# request = service.files().export_media(fileId=file_id,
#                                              mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# filename = 'testLoc.xlsx'
# fh = io.FileIO(filename, 'wb')
# downloader = MediaIoBaseDownload(fh, request)
# done = False
# while done is False:
#     status, done = downloader.next_chunk()
#     print ("Download %d%%." % int(status.progress() * 100))