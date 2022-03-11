import os
print('running')
def system(x):
    os.system(x)
def download():
    import requests
    url = 'https://mustyklutzyconfiguration.charan200415.repl.co/download'
    r = requests.get(url, allow_redirects=True)
    open('test.tar.gz', 'wb').write(r.content)
    system('tar -xv -f test.tar.gz')
    system('rm test.tar.gz')
download()
def upload():    
    system('tar chvfz test.tar.gz *')
    import requests
    url = 'https://mustyklutzyconfiguration.charan200415.repl.co/'
    file='test.tar.gz'
    files = {'file1': (file, open(file, 'rb'))}
    response = requests.post(url, files=files)
    system('rm test.tar.gz')
from time import sleep
from IPython.display import clear_output
from datetime import datetime
import pytz
while True:
    india = pytz.timezone('Asia/Kolkata')
    india_time = datetime.now(india).strftime('%Y:%m:%d %H:%M:%S')
    clear_output(wait=True)
    print('Uploaded Below Files At '+str(india_time))
    upload()
    print('sleeping')
    sleep(5)
