import zipfile
import os

for folders, subfolders, files in os.walk('C:\\backup'):

    for f in files:
        if f.endswith('.bak'):
            pathZ = '' + folders + '\\' + f.split('.')[0]+'.zip'
            path = '' + folders + '\\' + f
            fzip = zipfile.ZipFile(pathZ, 'w')
            fzip.write(path, compress_type=zipfile.ZIP_DEFLATED)
            fzip.close()
            # print('     '+path)
            os.remove(path)
    break
