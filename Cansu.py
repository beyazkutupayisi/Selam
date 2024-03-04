def check_imports():
    try:
        import user_agent
        import datetime
        import webbrowser
        import pyfiglet
        import threading
        import signal
    except ImportError as error:
        os.system('pip install user_agent')
        os.system('pip install datetime')
        os.system('pip install webbrowser')
        os.system('pip install pyfiglet')
        os.system('pip install threading')
        os.system('pip install signal')
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)



import subprocess
import sys
import time
import requests
import webbrowser
import base64
import json
import urllib3
import os
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print('\x1b[32m bekle cano Kontrol ediyorum ( İzin veriliyor ...⏳')
time.sleep(2)
print('\x1b[33m Toolu kullanmak İçin lütfen @thomashack kanalına katılın')
time.sleep(3)
import webbrowser
webbrowser.open('https://t.me/thomashack')
print('\x1b[32mİzin Verildi ✅')
time.sleep(2)

import time
import os
B = '\x1b[38;5;208m'  
BYellow = '\x1b[1;33m'




def install_module(module):
    subprocess.check_call([
        sys.executable,
        '-m',
        'pip',
        'install',
        module])

def check_module(module):
    try:
        __import__(module)
        print(f'[✓] {module} modülü mevcut.')
    except:
        print(f'[!] {module} modülü bulunamadı. Yükleniyor...')
        install_module(module)

required_modules = [
    'requests',
    'webbrowser',
    'base64',
    'json',
    'urllib3',
    'os',
    'random']

for module in required_modules:
    check_module(module)


os.system('clear')

memo='''

\x1b[1;33m

#####################%%%#####*****####################*
##############%%%%%%#**=-::.. . ..::.-+*##############*
%%%%%%%%%%%%%%%#*+=:.               .:+###############*
%%%%%%%%%%%%%*-.     .     .       ..:=###############*
%%%%%%%%%%#=:  ..   ..     ..    ...-*-#%%#############
%%%%%%%%%+.   .. ..:.  .....  .::-=+**+*#%%%###########
%%%%%%%%- ......:-==--=+*+==++*****+==-=+*%%%%%########
%%%%%%*: ...::--=+++***###%%%%%#+:..  .=+.*%%%%%%######
%%%%%%: ...:---=++***######***=:. .:..-+*=*%%%%%%%#####
%%%%%%:...:----=++**+*+====+++-:::::::=*#####*#%%%%%%%%
%%%%%@+..::::--====-:::-=++*#%#******###*+*+-:=%%%%%%%%
@@@@%@*..:::-----:::---=+#%%%##########*++=--:*%%%%%%%@
@@@@@@#..:::---::-=*####%%##**+++++++===+**++=-*%%%%%%@
@@@@@@@-..::::::-#+==#@%%#++++++++=====+**=-----%%%%%@@
@@@@@@@#....:::.-**#=**%##+++****###*##%#*=++=-.+@%%%@@
@@@@@@@@*.......=++*####*==+***######%%##**++++++#%%@@@
@@@@@@@@@#: ....:=-:------.:-++++++++****+++*##*=-%@@@@
@@@@@@@@@@@+.....:::---:::-:.:---------------:::.=%@@@@
@@@@@@@@@@@@%+:...:=*******+=--:...........   :+#@@@@@@
@@@@@@@@@@@@@@@%-.:=**####**++=-:.::::.... .+#@@@@@@@@@
@@@@@@@@@@@@@@٪٪@++++++*****++=-:---::....=%@@@@@@@@@@@
@@@@@@@@@@@@@%+=+*%@@@%##*++===--===--:..*@@@@@@@@@@@@@
@@@@@@@@@@@@@:    .:=*@٪٪@@%*+-------::.*@@@@@@@@@@@@@@
@@@@@@@@@@@@=......   .=#@٪٪@@%*+=-:::.=@@@@@@@@@@@@@@@
@@@@@@@@@@@%: ........   :=%@@@@@%#*-. *@@@@@@@@@@@@@@@
@@@@@@@@@%+:....... .....   -#@@@@@@@#*-+@@@@@@@@@@@@@@
@@@@@@@#-. ........... ....   -#@@@@@%#::#@@@@@@@@@@@@@
%@@@@%*:................    ..  -*%#-+*-.-#@@@@@@@@@@@@
%%@@@%#+=--:::::::.........  ..   :-==*%-  -#@@@@@%@@@@
%%%%%%%#*++===--:::::::::.......   .:=*%@=  .+%@%%%%%@@
%%%%%%%%%%##*+++====---::::::........:-+%%+::-+%%%%%%%@
%%%%%%%%@@@@%%%##**+=====------:::::::-=#%%*++*#%%%%%%@
                 < MEHMET VODAFONE TOOL V1.2 >
              TLE : @PHPMEHMET / @THOMASHACK

 \033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬MEHMET▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''                                               
print(memo)                                                            
   


def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

random_ip = generate_random_ip()

def save_password(parola):
    with open('saved_password.txt', 'w') as file:
        file.write(parola)

def load_password():
    try:
        with open('saved_password.txt', 'r') as file:
            return file.read().strip()
    except:
        pass

telno = input('\x1b[32mTel No Gir 0\' olmadan: \x1b[0m')
saved_password = load_password()
parola = None
if saved_password:
    use_saved_password = input('\x1b[33m 〽️Kayıtlı Parola Bulundu Kullanılsın mı (E/H): \x1b[0m').lower()
    if use_saved_password == 'e':
        parola = saved_password
    else:
        parola = input('\x1b[32m🔒VF Şifren\'i Gir: \x1b[0m')
        save_option = input('\x1b[33m🦐Yeni Şifre Kaydedilsin mi? (E/H): \x1b[0m').lower()
        if save_option == 'e':
            save_password(parola)
else:
    save_option = input('\x1b[33m🦐Şifre Kaydedilsin mi? (E/H): \x1b[0m').lower()
    if save_option == 'e':
        parola = input('\x1b[32m🔒VF Şifren\'i Gir: \x1b[0m')
        save_password(parola)

if parola is None:
    parola = input('\x1b[32m Vodafone Şifren\'i Gir: \x1b[0m')
    save_option = input('\x1b[33mYeni Şifre Kaydedilsin mi ?  (E/H): \x1b[0m').lower()
    if save_option == 'e':
        save_password(parola)

headers = {
    'User-Agent': 'VodafoneMCare/2308211432 CFNetwork/1325.0.1 Darwin/21.1.0',
    'Content-Length': '83',
    'Connection': 'keep-alive',
    'Accept-Language': 'tr_TR',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'm.vodafone.com.tr',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Forwarded-For': random_ip 
}

url = 'https://m.vodafone.com.tr/maltgtwaycbu/api/'
data = {
    'context': 'e30=',
    'username': telno,
    'method': 'twoFactorAuthentication',
    'password': parola 
}

response = requests.post(url, headers=headers, data=data)
proid = response.json().get('process_id')

if proid is None:
    print('\x1b[31m〽️ Şifre veya Numara Yanlış❌\x1b[0m')
    raise SystemExit()

print('\x1b[32mŞifre Doğrulama Başarılı✅\x1b[0m')
kod = input('\x1b[33m[+] SMS ile Gelen Kodu Gir: \x1b[0m')

veri = {
    'langId': 'tr_TR',
    'clientVersion': '17.2.5',
    'reportAdvId': '0AD98FF8-C8AB-465C-9235-DDE102D738B3',
    'pbmRight': '1',
    'rememberMe': 'true',
    'sid': proid,
    'otpCode': kod,
    'platformName': 'iPhone' 
}

base64_veri = base64.b64encode(json.dumps(veri).encode('utf-8'))

data2 = {
    'context': base64_veri,
    'grant_type': 'urn:vodafone:params:oauth:grant-type:two-factor',
    'code': kod,
    'method': 'tokenUsing2FA',
    'process_id': proid,
    'scope': 'ALL' 
}

response2 = requests.post(url, headers=headers, data=data2)
sonuc2 = response2.json()

o_head = {
    'Accept': 'application/json',
    'Language': 'tr',
    'ApplicationType': '1',
    'ClientKey': 'AC491770-B16A-4273-9CE7-CA790F63365E',
    'sid': proid,
    'Content-Type': 'application/json',
    'Content-Length': '54',
    'Host': 'm.vodafone.com.tr',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.10.0',
    'X-Forwarded-For': random_ip 
}

print('\x1b[1;33m Giriş Yapıldı ✅')
time.sleep(3)
os.system('clear')
print (memo)

print('\x1b[1;39m 〽️ Hangi İşlemi Yapmak İstiyorsun:')
sec = input('\x1b[1;33m\n[1] Çark Çevir\n[2] 50TL Fatura İndirimi Al\n[3] Faturalı Sınırsız İnternet\n[〽️] Seçiminiz: \x1b[0m')

if sec == '1':
    cark_data = {
        'clientKey': 'AC491770-B16A-4273-9CE7-CA790F63365E',
        'clientVersion': '16.8.3',
        'language': 'tr',
        'operatingSystem': 'android' 
    }
    
    cark_url = f'https://m.vodafone.com.tr/squat/getSquatMarketingProduct?sid={proid}'
    al_url = f'https://m.vodafone.com.tr/squat/updateSquatMarketingProduct?sid={proid}'
    
    cark = requests.post(cark_url, headers=o_head, json=cark_data).json()

    try:
        c1 = cark['data']['name']
        c2 = cark['data']['code']
        c3 = cark['data']['interactionID']
        c4 = cark['data']['identifier']
        
        al_data = {
            'clientKey': 'AC491770-B16A-4273-9CE7-CA790F63365E',
            'clientVersion': '
