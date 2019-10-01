import os
import zipfile

def start():
    with zipfile.ZipFile('bitcoiinGo.zip') as myzip:
        with myzip.open('bitcoiinGo') as myfile:
            data = myfile.read()
    with open('bitcoiinGo','w+b') as myfile:
        myfile.write(data)
    os.system('bash -c "/mnt/c/B2G/bitcoiinGo init genesis.json"')
    
start()
