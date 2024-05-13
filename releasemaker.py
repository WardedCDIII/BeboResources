import os
from zipfile import ZipFile

with ZipFile('release.zip', 'w') as zip_obj:
    for folder,sub,files, in os.walk("BeboResources"):
        for filename in files:
            file_path = os.path.join(folder,filename)
            zip_obj.write(file_path,os.path.basename(file_path))
