import os
print('running')
def ser(x):
    os.system(x)
def download():
    import requests
    url = 'https://mustyklutzyconfiguration.charan200415.repl.co/download'
    ser(f'curl -o test.tar.gz {url}')
    ser('tar -xvf test.tar.gz')
    ser('rm test.tar.gz')
#download()
def upload():    
    ser('tar chvfz test.tar.gz project')
    import requests
    url = 'https://mustyklutzyconfiguration.charan200415.repl.co/'
    file='test.tar.gz'
    files = {'file1': (file, open(file, 'rb'))}
    response = requests.post(url, files=files)
    ser('rm test.tar.gz')
from time import sleep
from datetime import datetime
import pytz
while True:
    india = pytz.timezone('Asia/Kolkata')
    india_time = datetime.now(india).strftime('%Y:%m:%d %H:%M:%S')
    x=True
    if x:
        with open('project/log','w') as file:
            file.write('')
        x=False
    with open('project/log','a') as file:
        file.write('Uploaded Below Files At '+str(india_time))
    print('Uploaded Below Files At '+str(india_time))
    upload()
    print('sleeping')
    sleep(5)
