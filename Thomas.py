from requests import get
from random import choice
from random import randrange
from threading import Thread
url='https://bad0c-403cd5ae3f06.herokuapp.com/Qredes/keyword='
def randomword(length):
  return ''.join(choice('azertyuiopqsdfghjklmwxcvbn1234567890') for i in range(length))
def thomas():
  while True:
    try:
       g=get(url+randomword(randrange(3,9))).json()['usernames']
       for username in g:
         print(username)
         with open('qredesusers.txt','a') as f:
           f.write(username+'\n')
           f.close()
    except:thomas()
for _ in range(20):
  Thread(target=thomas).start()
