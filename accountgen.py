import requests
from random import randint
from threading import Thread
import time
import random
import string
from bs4 import BeautifulSoup as soup
import datetime


print("-------------------------------------")
print("     ADIDAS ACCOUNT CREATOR \n    Created by Anton Lin \n     www.github.com/antonjlin")
print("-------------------------------------")
p = open('proxies.txt')
proxieslines = p.readlines()
numproxies = len(proxieslines)
if numproxies > 0:
    useproxies = True
if numproxies == 0:
    useproxies = False

print('%s proxies loaded' %numproxies)

region = 'US'

emailin = input("Email: ")

password = input('Password: ')


open("createdaccounts.txt", "a")
log = open('createdaccounts.txt', 'a')

part1 = "https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/"


emaillist = []

runs = 0

tasks = int(input('Number of accounts to create: '))

def accountgenner(x, runs):

    adidasregion1 = part1.split('//')[1]
    adidasregion = adidasregion1.split('/')[0]
    #returns www.adidas.com


    timedelay = randint(0,2)
    s = requests.Session()

    if useproxies == True:
        if x + 1 <= len(proxieslines):
            proxy = proxieslines[x].rstrip()
        if x + 1 > len(proxieslines):
            if len(proxieslines) > 1:
                a = randint(1, len(proxieslines) - 1)
            if len(proxieslines) == 1:
                a = 0
            proxy = proxieslines[a].rstrip()

        try:
            proxytest = proxy.split(":")[2]
            userpass = True
        except IndexError:
            userpass = False

        if userpass == False:
            proxyedit = proxy

        if userpass == True:
            ip = proxy.split(":")[0]
            port = proxy.split(":")[1]
            userpassproxy = ip + ':' + port
            proxyedit = userpassproxy
            proxyuser = proxy.split(":")[2]
            proxyuser = proxyuser.rstrip()
            proxypass = proxy.split(":")[3]
            proxyuser = proxyuser.rstrip()

        if userpass == True:
            proxies = {'http': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy}
        if userpass == False:
            proxies = {'http': 'http://' + proxy}

#============================================

    print("[TASK %s]: Launched account creator." % x)
    securekey1 = None
    session1 = None
    securekey2 = None
    session2 = None
    securekey3 = None
    session3 = None
    accountcreated = False
    finalproceed = False


    prefix = emailin.split('@')[0]
    domain = emailin.split('@')[1]

    def emailcreated(email):
        alreadycreated = False
        with open('createdaccounts.txt') as f:
            for line in f:
                if email in line:
                    alreadycreated = True
            return alreadycreated

    def prefixgen(prefix):
        kad = 0
        for pos, ch in enumerate(prefix):
            dotnum = randint(1, 3)
            if dotnum == 1:
                newpos = pos + kad
                start = prefix[:newpos]
                end = prefix[newpos:]
                previous = prefix[newpos - 1]
                if previous != '.':
                    prefix = start + '.' + end
                    kad += 1
                if previous == '.':
                    pass

        email = str(prefix + '@' + domain)
        if email in emaillist or emailcreated(email):
            print("[TASK %s]: Email already genreated. Regenrating..." %x)
            time.sleep(0.25)
            prefixgen(prefix)
        else:
            emaillist.append(email)
            return email

    email = prefixgen(prefix)
    email = str(email)

    if email[:1] == '.':
        email = email[1:]
    with open('createdaccounts.txt') as createdaccounts:
        createdaccounts.readlines
    #for pos, ch in enumerate(email):
    #    if pos == 0:

    #        if ch == '.':
    #            email = email[1:]

    threadpass = password


    def generator():
        firstnameslist = ['Bill', 'Bob', 'Chris', 'Kyle', 'Alisdair', 'John', 'Steve', 'Santiago','Bernard', 'Ross', 'Donald', 'David', 'Andrew', 'Alison', 'Hilary','Vlad']
        namenum = randint(0, len(firstnameslist) - 1)
        firstname = firstnameslist[namenum]
        lastnameslist = ['Santiago', 'Brown', 'Johnson', 'Smith', 'Clinton', 'Hamilton', 'Cardon', 'Wood','Canterbury','Garcia','Edwards','Munro','Trump','Faux','Saint']
        lastnamenum = randint(0, len(lastnameslist) - 1)
        lastname = lastnameslist[lastnamenum]
        day = randint(1, 28)
        month = randint(1, 12)
        year = randint(1990, 1998)
        return firstname, lastname, day, month, year

    firstname, lastname, day, month, year = generator()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Upgrade-Insecure-Requests': '1', 'Host': adidasregion, 'Connection': 'keep-alive'}
    generallink = part1 + 'MiAccount-Register/'
    if useproxies == True:
        j = s.get(generallink, headers=headers, proxies=proxies)
    if useproxies == False:
        j = s.get(generallink, headers=headers)
    page1 = soup(j.text, 'html.parser')

    for item in page1.findAll('input'):
        if item['name'] == 'dwfrm_mipersonalinfo_securekey':
            securekey1 = item['value']
    if securekey1 == None:
        print("[TASK %s]: Failed to create account. Retrying..." % x)
        runs +=1
        accountcreated = False
        proceed1 = False
        #retry
    else:
        proceed1 = True
        #keep filling out the form

    if proceed1 == False:
        if runs <5:
            time.sleep(1)
            accountgenner(x,runs)
        if runs == 5:
            print("[TASK %s]: Failed account generation 5 times, quitting..." %x)
            pass

    if proceed1 == True:

        for form in page1.findAll('form'):
            if form['id'] == 'dwfrm_mipersonalinfo':
                strip = form['action']
                strip2 = strip.split('Register/')[1]
                #returns code after url (session id)
                #https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/C376093238
                session1 = strip2.rstrip()

        if session1 == None:
            print("[TASK %s]: Failed to create account. Retrying..." % x)
            runs +=1
            accountcreated = False
            proceed2 = False
        else:
            proceed2 = True

        if proceed2 == False:
            if runs < 5:
                time.sleep(1)
                accountgenner(x,runs)
            if runs == 5:
                print("[TASK %s]: Failed account generation 5 times, quitting..."%x)
                pass

        if proceed2 == True:
            accountlink = part1 + 'MiAccount-Register/' + session1

            payload1 = {'dwfrm_mipersonalinfo_firstname': firstname, 'dwfrm_mipersonalinfo_lastname': lastname,'dwfrm_mipersonalinfo_customer_birthday_dayofmonth': str(day),'dwfrm_mipersonalinfo_customer_birthday_month': str(month),'dwfrm_mipersonalinfo_customer_birthday_year': str(year),'dwfrm_mipersonalinfo_step1': 'Next', 'dwfrm_mipersonalinfo_securekey': securekey1}


            if useproxies == True:
                p = s.post(accountlink, headers=headers, data=payload1, proxies=proxies)
            if useproxies == False:
                p = s.post(accountlink, headers=headers, data=payload1)
            time.sleep(0.5)

            page2 = soup(p.text, 'html.parser')

            for item in page2.findAll('input'):
                if item['name'] == 'dwfrm_milogininfo_securekey':
                    securekey2 = item['value']

            if securekey2 == None:
                print("[TASK %s]: Failed to create account. Retrying..." % x)
                runs +=1
                accountcreated = False
                proceed3 = False
            else:
                proceed3 = True

            if proceed3 == False:
                if runs < 5:
                    time.sleep(1)
                    accountgenner(x,runs)
                if runs == 5:
                    print("[TASK %s]: Failed account generation 5 times, quitting..." %x)
                    pass

            if proceed3 == True:

                for form in page2.findAll('form'):
                    if form['id'] == 'dwfrm_milogininfo':
                        strip = form['action']
                        strip2 = strip.split('Register/')[1]
                        session2 = strip2.rstrip()

                if session2 == None:
                    print("[TASK %s]: Failed to create account. Retrying..." % x)
                    runs +=1
                    accountcreated = False
                    proceed4 = False
                else:
                    proceed4 = True

                if proceed4 == False:
                    if runs < 5:
                        time.sleep(1)
                        accountgenner(x,runs)
                    if runs == 5:
                        print("[TASK %s]: Failed account generation 5 times, quitting..."%x)
                        pass

                if proceed4 == True:

                    accountlink2 = part1 + 'MiAccount-Register/' + session2

                    headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Upgrade-Insecure-Requests': '1', 'Host': adidasregion, 'Origin': 'http://' + adidasregion,'Referer': accountlink}

                    payload2 = {'dwfrm_milogininfo_email': email, 'dwfrm_milogininfo_password': threadpass,'dwfrm_milogininfo_newpasswordconfirm': threadpass, 'dwfrm_milogininfo_step2': 'Next','dwfrm_milogininfo_securekey': securekey2}

                    time.sleep(timedelay)
                    if useproxies == True:
                        k = s.post(accountlink2, headers=headers2, data=payload2, proxies=proxies)
                    if useproxies == False:
                        k = s.post(accountlink2, headers=headers2, data=payload2)

                    page3 = soup(k.text, 'html.parser')

                    if 'Email already taken' in str(page3):
                        print("[TASK %s]: Email for Adidas Account is taken. Retrying..." %x)
                        runs +=1
                        validemail = False
                    else:
                        validemail = True

                    if validemail == False:
                        if runs < 5:
                            time.sleep(0.5)
                            accountgenner(x,runs)
                        if runs == 5:
                            print("[TASK %s]: Failed account generation 5 times, quitting..." %x)
                            pass


                    if validemail == True:
                        for item in page3.findAll('input'):
                            if item['name'] == 'dwfrm_micommunicinfo_securekey':
                                securekey3 = item['value']

                        if 'Please make sure your password contains a minimum of one letter' in page3:
                            print("[TASK %s]: Password entered did not meet Adidas's requirements.")

                        if securekey3 == None:
                            print("[TASK %s]: Failed to create account. Retrying..." % x)
                            runs +=1
                            accountcreated = False
                            proceed5 = False
                        else:
                            proceed5 = True

                        if proceed5 == False:
                            if runs < 5:
                                time.sleep(1)
                                accountgenner(x, runs)
                            if runs == 5:
                                print("[TASK %s]: Failed account generation 5 times, quitting..." %x)
                                pass

                        if proceed5 == True:

                            for form in page3.findAll('form'):
                                if form['id'] == 'dwfrm_micommunicinfo':
                                    strip = form['action']
                                    strip2 = strip.split('Register/')[1]
                                    session3 = strip2.rstrip()

                            if session3 == None:
                                print("[TASK %s]: Failed to create account. Retrying..." % x)
                                runs +=1
                                accountcreated = False
                                proceed6 = False
                            else:
                                proceed6 = True

                            if proceed6 == False:
                                if runs < 5:
                                    time.sleep(1)
                                    accountgenner(x,runs)
                                if runs == 5:
                                    print("[TASK %s]: Failed account generation 5 times, quitting..." %x)
                                    pass

                            if proceed6 == True:

                                accountlink3 = part1 + 'MiAccount-Register/' + session3
                                headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Upgrade-Insecure-Requests': '1', 'Host': adidasregion, 'Origin': 'http://' + adidasregion,'Referer': accountlink}

                                payload3 = {'dwfrm_micommunicinfo_agreeterms': 'true', 'dwfrm_micommunicinfo_step3': 'Register','dwfrm_micommunicinfo_securekey': securekey3}

                                time.sleep(timedelay)
                                if useproxies == True:
                                    g = s.post(accountlink3, headers=headers2, data=payload3, proxies=proxies)
                                if useproxies == False:
                                    g = s.post(accountlink3, headers=headers2, data=payload3)
                                time.sleep(0.5)

                                if 'justRegistered=true' in g.text:
                                    currenttime3 = str(datetime.datetime.now())
                                    currenttime4 = currenttime3.split(" ")[1]
                                    currenttime5 = currenttime4.split(".")[0]
                                    accountstring = "%s:%s" % (email, threadpass)
                                    #log.write("[" + currenttime5 + "]:" + accountstring + "\n")
                                    log.write(accountstring + "\n")
                                    print("-------------------------------------")
                                    print("   Task {}: Success, created account: \n   Email: {} \n   Password: {}".format(x,email, threadpass))
                                    print("-------------------------------------")
                                    finalproceed = True



                                else:
                                    print("[Task %s]: Failed to create account. Retrying..." % x)
                                    accountcreated = False
                                    finalproceed = False
                                if finalproceed == False:
                                    time.sleep(0.5)
                                    accountgenner(x,runs)
                                if finalproceed == True:
                                    pass


for i in range(0, tasks):
    if useproxies :
        #thread
        t = Thread(target=accountgenner, args=(i,runs))
        t.start()
        time.sleep(2)
    else:
        #dont thread to avoid banning.
        accountgenner(i,runs)
