#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from extra_scan import extras_scan
    from sys import executable
    import urllib
    import pathlib
    import time
    from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
    import sched
    import random
    import urllib
    import shodan
    import sys
    import nmap
    from api import apikey, vulners_api_key
    import time
    import base64
    import vulners
    import os
    from time import sleep
    from termcolor import cprint
    from scapy.all import sr, srp, IP, UDP, ICMP, TCP, ARP, Ether
    import dpkt
    import sqlite3
except (ImportError) as e:
    print("Something is terribly wrong:\n->{}".format(e))
    sys.exit(1)
try:
    system_check = os.uname()
    from subprocess import Popen, PIPE
    clear = 'clear'
    from subprocess import Popen, PIPE
    if os.getuid() != 0:
        cprint("[ !! ] Please make sure to run this script as sudo [ !! ]", "red", attrs=["blink"])
        sys.exit(1)
except AttributeError:
    clear = 'cls'
    pass

if Sploit.checkForRun():
    cprint("[ + ] Please wait, building database if this is the first run.. [ + ]", "white", attrs=["blink"])
    Sploit.makeDB()
    Sploit.insertTimeruns(what="initial")
PATH = './atk_output/' + str(time.time())
logo = '''
 ________   __        _______   ______   ______   _________   
/_______/\ /_/\     /_______/\ /_____/\ /_____/\ /________/\  
\::: _  \ \\:\ \    \::: _  \ \\::::_\/_\:::_ \ \\__.::.__\/  
 \::(_)  \ \\:\ \    \::(_)  \/_\:\/___/\\:(_) ) )_ \::\ \    
  \:: __  \ \\:\ \____\::  _  \ \\::___\/_\: __ `\ \ \::\5 \   
   \:.\ \  \ \\:\/___/\\::(_)  \ \\:\____/\\ \ `\ \ \ \::\ \  
    \__\/\__\/ \_____\/ \_______\/ \_____\/ \_\/ \_\/  \__\/ 
is Restarting'''
cprint("[ + ] Please wait, indexing extra modules. [ + ]", "white", attrs=['blink'])
DIRECTORIES = ['./data/scripts', './data/scripts/persistance', './data/lists', './XML_Output/']
for item in DIRECTORIES:
    purpose = ''
    if item == './data/scripts': purpose = "Recon"
    elif item == './data/scripts/persistance': purpose = "Persist"
    elif item == './data/lists': purpose = "General"
    elif item == './XML_Output': purpose = "Scan_Result"
    Sploit.buildToolsList(directory=str(item), purpose=purpose)


def pw_lists():
    print("Starting to import password lists, please be patient.\n")
    PATH_DIR = './data/main_pass.txt'
    usersnames = set()
    try:
        with open(PATH_DIR, 'r') as ax:
                sykes = ax.readlines()
                for line in sykes:
                    print(line.strip('\n'))
                    usersnames.add(line.strip('\n'))
                return usersnames
    except (IOError, FileNotFoundError) as e:
        print("{}".format(e))
        return e

def usernames():
    PATH_DIR = './data/main_names.txt'
    passes = set()
    with open(PATH_DIR, 'r') as a:
        try:
            style = a.readlines()
            for line in style:
                print(line.strip('\n'))
                passes.add(line.strip('\n'))
            return passes
        except (IOError, FileNotFoundError) as e:
            print("{}".format(e))
            return e

def albert_faces():
    alberts = ''
    albert = random.randint(1, 3)
    if albert == 1: alberts = "./art/albert_face.txt"
    if albert == 2: alberts = "./art/albert_face_2.txt"
    if albert == 3: alberts = "./art/fat_albert_3"
    face = open(alberts, "r")
    lulz = face.readlines()
    for line in lulz:
        cprint(line.strip("\n"), 'green')
        sleep(0.5)
    sleep(0.5)
    cprint("Loading The King Himself Hopefully He Left You Some Exploits....", 'red')
    sleep(0.5)
    cprint("Gr33ts: Chef Gordon, Root, Johnny 5", 'red')
    return "t"

def write_file(line):
    with open('hosts_list', 'at') as f:
        f.writelines(line)
    f.close()
    return False


def atk_log(atk):
    try:
        with open(PATH, 'a') as f:
            lines = set()
            lines.add(atk)
            for item in lines:
                f.writelines(item)
            f.write('\n-----------------------------------------------------------------------------\n')
        f.close()
        return False
    except TypeError as e:
        print("{}".format(e))
        return e


def list_reject(target=''):
    api = shodan.Shodan(apikey)
    try:
        search = api.host(target)
        print("""
                IP: {}
                Organization: {}
                Operating System: {}
        """.format(search['ip_str'], search.get('org', 'n/a'), search.get('os', 'n/a')))

        # Print all banners
        for item in search['data']:
            print("""
                        Port: {}
                        Banner: {}
                """.format(item['port'], item['data']))
            oops = [str(search['ip_str'], "\n", str(search['data'], "\n"))]
            write_file(''.join(oops))
        return False
    except shodan.APIError as e:
        os.system(clear)
        print('[✘] Errpr: %s' % e)
        option = input('[*] Shieeeet you wanna chagne that API Key? <Y/n>: ').lower()
        if option == ('y'):
            file = open('api.py', 'w')
            SHODAN_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid Shodan.io API Key: ')
            oppsie = ["apikey= ", "\"", str(SHODAN_API_KEY), "\""]
            file.write(''.join(oppsie))
            print('[~] File Dropped Nigga: ./api.py')
            file.close()
            print('[~] Take 5 To Larp Around\n {}'.format(logo))
            return False


def nmapScan(tgtHost, tgtPort, args, file):  # Nmap function created
    try:
        if args != '':
            print("[ + ] Using: {} [ + ]".format(args))
            command = 'nmap ' + tgtHost + ' ' + args
            nmScanner = Popen([command], stdout=PIPE)
            print(nmScanner.communicate())
        if args == '':
            nmScan = nmap.PortScanner()
            nmScan.scan(tgtHost, tgtPort)
            state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
            nmScan.csv()
            print("[ ! ]  {}\n TCP: {} \n UP/DOWN: {}\n".format(tgtHost, tgtPort, state))
            return "Scan file is located at: ", file
    except FileNotFoundError:
        print("Please install Nmap on your system, and try this again.")
        return tgtHost, tgtPort


def subnet_discover(ip):
    import netaddr
    try:
        question = netaddr.IPAddress(ip)
        response = netaddr.IPNetwork(ip).cidr
        print("Reverse DNS {}".format(question.reverse_dns))
        print("Subnet/CIDR: {}".format(response.cidr))
        print("Private? {}".format(question.is_private))
        print("Net Mask: {}".format(response.netmask))
        print("Broad Cast: {}".format(response.broadcast))
        print("Host Mask: {}".format(response.hostmask))
        print("Multicast: {}".format(question.is_multicast))
        return response
    except netaddr.core.AddrFormatError as es:
        print("[ + ] Sorry, that was not an IP [ + ]\n\t\t-> {}".format(es))
        return es


def scapy_selection(net):
    import datetime as dt
    from scapy.all import srp, ETHER_ANY, ARPHDR_ETHER, conf, IFACES
    try:
        print("{}".format(IFACES.show(resolve_mac=True, print_result=True)))
        interface = str(input("[ + ] Please choose an interface [ + ]\n->"))
        ip = net
        time_start = dt.datetime.now()
        conf.verb = 0
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, iface=interface, inter=0.1)
        print("MAC and IP\n")
        for snd, rcv in ans:
            print(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
            stop_time = dt.datetime.now()
            total_time = time_start - stop_time
            print("[ ** ] Complete! [ ** ]")
            print("[ ** ] Finished in: {} [ ** ]".format(total_time))
        return "ARP Scan of: ", ip
    except Exception as e:
        print("{}".format(e))
        return e


def dns_dumpster(domain):
    try:
        res = DNSDumpsterAPI({'verbose': True}).search(domain)
        aks = ['DNS Dumpster results:', '\n', str(res), '\n']
        atk_log(''.join(aks))
        print("[ + ] Searching for {} [ + ]".format(domain))
        print("\n[ + ] DNS Servers [ + ]")
        for entry in res['dns_records']['dns']:
            print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        print("\n[ + ] MX Records [ + ]")
        for entry in res['dns_records']['mx']:
            print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        print("\n[ + ] Host Records (A) [ + ]")
        for entry in res['dns_records']['host']:
            if entry['reverse_dns']:
                print(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
            else:
                print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        print("\n[ + ] TXT Records [ + ]")
        for entry in res['dns_records']['txt']:
            print("{}".format(entry))
        image_retrieved = res['image_data'] is not None
        print("\nRetrieved Network mapping image? {} (accessible in 'image_data')".format(image_retrieved))
        print(repr(base64.b64decode(res['image_data'])[:20]) + '...')
        xls_retrieved = res['xls_data'] is not None
        print("\nRetrieved XLS hosts? {} (accessible in 'xls_data')".format(xls_retrieved))
        print(repr(base64.b64decode(res['xls_data'])[:20]) + '...')
        return domain
    except Exception as e:
        print("{}".format(e))
        return e


def smtp_enum(server, user, passwd):
    import smtplib
    if user == '' and passwd == '':
        user = usernames()
        passwd = pw_lists()
    else:
        try:
            userOpen = open(user, "r")
            userWord = userOpen.readlines()
            userOpen.close()
        except IOError:
            print("[-]No User file found: " + user)
            pass
        try:
            passOpen = open(passwd, "r")
            passWord = passOpen.readlines()
            passOpen.close()
        except IOError:
            print("[-]No Password File Found")
            pass
    try:
        smtpServer = smtplib.SMTP(server, port)
        smtpServer.ehlo()
        smtpServer.starttls()
    except:
        print(" No server found")
        sys.exit(1)
    for username, passe in userWord, passWord:
        con = smtplib.SMTP()
        try:
            con.login(username, passe)
            print("server: ")
            print("port: ")
            print("username: ")
            print("password: ")
        except Exception as e:
            print("{}".format(e))
            return e

def panel_find(server, adminList):
    import urllib3
    if adminList == '':adminList = open("./data/adm_list", "r")
    for admin in adminList.readlines():
        ax = set()
        ax.add(admin)
        x = urllib3.PoolManager()
        for item in ax:
            lx = server + item
            x.request('GET', lx)
            if x.status == '200' or x.status != 200:
                print("[-] Found Da Panel -> {}".format(lx))

def iplocator(ip):
    import urllib3
    url = "http://ip-api.com/json/"+ip
    try:
        u = urllib3.PoolManager()
        x = u.request('GET', url)
        if x.status != '200' or x.status != 200:
            print("[ + ] Failed at request! [ + ]")
            pass
        else:
            print(x.data)
    except Exception as e:
        print("[-] Did Not Work:\n{} [~]".format(e))

def vulners_api(option, term):
    vulners_search = vulners.Vulners(api_key=api)
    if api == '':
        file = open('vulnersapi.py', 'w')
        VULNERS_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid VulnersCom API Key: ')
        oppsie = ["apikey= ", "\"", str(VULNERS_API_KEY), "\""]
        file.write(''.join(oppsie))
        print('[~] File Dropped Nigga: ./vulnersapi.py')
        file.close()
        print('[~] Take 5 To Larp Around\n {}'.format(logo))
    if option == "1":
        exploit = vulners_search.search(term, limit=10, fields=['bulletinFamily', 'exploit', 'description',
                                                                'modified', 'published', 'id', 'href', 'title',
                                                                'vector',
                                                                'type', 'vhref', 'title', 'type'])
        for item in exploit:
            print("Exploits found for {}:\n{}".format(term, item))

    if option == "2":
        clue = vulners_search.documentList(term)
        for item in clue:
            print("{}".format(item))
    if option == "3":
        sploit = vulners_search.searchExploit(term)
        for loit in sploit:
            print("{}".format(loit))
    if option == "4":
        version = str(input("Please enter a version number\n->"))
        stuff = vulners_search.softwareVulnerabilities(term, version)
        results = stuff.get('exploit')
        vulnrabilities_list = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty']]
        return vulnrabilities_list
    # if option == "5":
    # all_cve = vulners_search.archive("cve")
    # text_ai_score = vulners_search.aiScore(" Flamming Botnet")
    # print('[~] Hey! Hey! Hey! Time To Put Your BigBoy Pants On, Self Audit!')
    # OS_vulnerabilities = vulners_search.audit(os=' ', os_version=' ', package=[' '])
    # vulnerable_packages = OS_vulnerabilities.get('pacakge')
    # missed_patches_ids = OS_vulnerabilities.get('vulnerabilitites')
    # cve_list = OS_vulnerabilities.get('cvelist')


def exploit_db(file):
    from subprocess import PIPE, Popen
    default = './XML_Output/scan.xml'
    try:
        if file == '':
            command = 'searchsploit -x --nmap {}'.format(default)
            db_search = Popen([command], stdout=PIPE, stderr=PIPE)
            atk_log(print(db_search.communicate()))
        if file != '':
            fil = file
            command = 'searchsploit -x --nmap {}' .format(fil)
            db_search = Popen([command], stdout=PIPE, stderr=PIPE)
            atk_log(print(db_search.communicate()))
    except Exception as e:
        print("{}".format(e))
        return e

def netsh_pivot(option, iface, listenport, connectport, host):
    from subprocess import Popen, PIPE
    if option == '1':
        # put the popen connamds in here
        command = "{}{}{}".format(listenport, connectport, host)
        Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return

def netsh_pipe(choice, iface, listenport, connectport, host):
    if port == "":
        listenport, connectport = random.randint(1, 1000)
    else:
        connectport = connectport
        listenport = listenport
    command_v4 = 'netsh {} portpory add v4 to v4 listenport={} connectport={}'.format(iface, listenport, connectport)
    command_wlan = 'netsh wlan show networks mode=bssid'
    command_del = 'netsh {} portproxy del'

    if choice == '1':
        Popen(command_v4, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    if choice == '2':
        Popen(command_wlan, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    if choice == '3':
        Popen(command_del, stdin=PIPE, stdout=PIPE, stderr=PIPE)

def extra_mods(lang, method=''):
    Sploit.queryTools(lang=lang, method=method)

        # @todo will be adding in a way to select the entry/row


if __name__ == '__main__':
    # @todo bring in a honeypot detection routine.
    # @todo a way to avoid docker containers like the plague.
    # @todo, Scapy routine, list available interfaces.
    # @todo, add packet sniffing on the fly. <- debating on using this.
    run = albert_faces()
    sleep(0.4)
    while run == 't':
        try:
            os.system(clear)
            options = str(input("\n\n\n\t[ + ]\n\t  [ ?? ] Recon Phase:\n\n" \
                                "\t\t > 1. Shodan\n" \
                                "\t\t > 2. Nmap(Targeted Scanning of host system written out to XML file)\n" \
                                "\t\t > 3. Subnet Discovery\n" \
                                "\t\t > 4. NMAP Scan of subnet hosts(ARP or ICMP ACK)\n" \
                                "\t\t > 5. DNSDumpster for invalid Domain setups\n" \
                                "\t\t > 6. Vulners DB Search API\n" \
                                "\t\t > 7. Admin Finder\n" \
                                "\t\t > 8. SMTP User Enum/Brute Force\n"\
                                "\t\t > 9. IP Locator\n"\
                                "\t --------------------------------------------------\n\n" \
                                "\t  [ !! ] Exploitation phase:\n"
                                "\t\t > E1 Exploit DB\n\n"\
                                "\t --------------------------------------------------\n\n"\
                                "\t [ ** ] Post-Exploitation Phase:\n"\
                                "\t\t > P1 Windows API Manipulation\n" \
                                "\t\t > P2 Network Pivot with NetSH\n"\
                                "\t -------------------------------------------------\n\n"\
                                "\t [ && ] Automate Process:\n"\
                                "\t\t > A1 Async Automation\n"\
                                "\t -------------------------------------------------\n\n"\
                                "\t [ ++ ] Additive Module Search:\n"\
                                "\t\t > M1 Extra Modules\n"
                                "\n\n[ * ] Choice goes here: \n->")).lower()

            if options == 'm1':
                cprint("[ ! ] Searching by language............. [ ! ]\n")
                lang = input("[ ? ] Which language module would you like to search for? [ ? ] \n->")
                try:
                    extra_mods(lang=lang, method='')
                except FileNotFoundError:
                    cprint("[ !!! ] Database not found! re-run the program to generate this please. [ !!! ]", "red",
                           attrs=["bold", "blink"])
            if options == 'a1':
                import auto_albert
                try:
                    a = Albert_api
                    atk_log(a)
                    continue
                except Exception as e:
                    print("[!] Automation Failure: {} [!]".format(e))
                    continue

            if options == '1':
                os.system(clear)
                choice = str(input("[ + ] Is this a file list, or a single IP:\n" \
                                   "\t1 . ) File List\n" \
                                   "\t2 . ) Single IP\n" \
                                   "[ + ] ->"))

                if choice == '1':
                    os.system(clear)
                    dest = str(input("[ + ] Please input the name of the file list:\n->"))
                    liz = set()

                    if dest == '':
                        os.system(clear)
                        print("[ ! ] Hey! Hey! Hey! Need a file name! [ ! ]")
                        run = 'a'
                    reader = open(dest, "r")
                    for line in reader.readlines():
                        line.strip("\n")
                        atk_log(list_reject(line))
                    continue

                if choice == '2':
                    os.system(clear)
                    choice = str(input("[ + ] Please Input the IP: \n->"))
                    atk_log(list_reject(choice))
                    continue

            if options == '2':
                def_args = "-sW -p 15-6893 -sV --version-all -A -T2 -sC --data-length 180 -oX " \
                           "./XML_Outpot/scan.xml -vvv --reason"
                print("Default Args: \n{}".format(def_args))
                question = str(input("[ + ] Would you like to use custom args with the nmap scan? [ + ] \n->")).lower()
                if question == 'n':
                    os.system(clear)
                    host = str(input("[ + ] Please input host IP:\n->"))
                    port = str(input("[ + ] Please input port:\n->"))
                    try:
                        atk_log(nmapScan(host, port, args=def_args, file=''))
                    except KeyError as e:
                        print("[ !! ] IP Must not be a valid IP: \n{}".format(e))
                        continue
                    continue
                if question == 'y':
                    os.system(clear)
                    host = str(input("[ + ] Please input host IP:\n->"))
                    port = str(input("[ + ] Please input port:\n->"))
                    file = './XML_Output/{}.xml'.format(host)
                    def_args = "-sW -p 15-6893 -sV --version-all -A -T2 -sC --data-length 180 -oX " \
                               "./XML_Outpot/{}.xml -vvv --reason".format(host)
                    args = str(
                        input("[ + ] Please enter the full commands:\n Example: -f -t 0 -n -Pn –data-length 200 -D" \
                              "\n->"))
                    print("If you choose to not enter any different args, these will be used\n" \
                          "Default Args: \n{}".format(def_args))
                    if args == '':
                        atk_log(nmapScan(host, port, args=def_args, file=file))
                        continue
                    if args != '':
                        atk_log(nmapScan(host, port, args=args, file=file))
                        continue

            if options == "3":
                choice = str(input("[ + ] Please input the subnet to detect [ + ]\n->"))

                if choice != '':
                    atk_log(subnet_discover(choice))
                    continue

            if options == "4":
                chance = str(input("[ ** ] Are you choosing\n" \
                                   "\t1. ) ARP\n" \
                                   "\t2. ) ICMP ACK [ ** ]\n[ + ] ->"))
                if chance == "2":
                    print("[ !! ] So sorry, not done with that yet... [ !! ]")
                    continue

                if chance == "1":
                    strike = str(input("[ + ] Please enter the IP, we will need to scan the subnet [ + ]"))
                    atk_log(scapy_selection(subnet_discover(strike)))
                    continue

            if options == "5":
                domain = str(input("[ * ] Please enter a domain name: [ * ]\n->"))
                atk_log(dns_dumpster(domain=domain))
                continue

            if options == "6":
                choice = str(input("[ + ] VulnersDB search API:\n" \
                                   "\t1 . ) Search by term\n" \
                                   "\t2 . ) Search by CVE code\n" \
                                   "\t3 . ) Search for specific exploits\n" \
                                   "\t4 . ) Search by term and Version Number [ + ]\n" \
                                   "[ + ] - >"))
                if choice == "1":
                    term = str(input("[ + } Please input a string to search for [ + ]\n->"))
                    atk_log(vulners_api(option="1", term=term))
                    continue
                if choice == "2":
                    term = str(input("[ + } Please input a Doc to search for [ + ]\n->"))
                    atk_log(vulners_api(option="2", term=term))
                    continue
                if choice == "3":
                    term = str(input("[ + } Please input a CVE number to search for \n" \
                                     "example: CVE-2017-14174 [ + ]\n->"))
                    atk_log(vulners_api(option="3", term=term))
                    continue
                if choice == "4":
                    term = str(input("[ + } Which software are we to search for [ + ]\n->"))
                    atk_log(vulners_api(option="4", term=term))
                    continue
            if options == '7':
                from pathlib import Path
                server = str(input("[ + ] Please input the server address [ + ]\n->"))
                admlist = str(input("[ + ] Please tell me where the admin list is, or leave blank for default [ + ]\n->"))
                if server != '' and admlist != '':
                    atk_log(panel_find(server, adminList=Path(admlist)))
                    continue
            if options == '8':
                server = str(input("[ + ] Please input a server address/IP [ + ]\n->"))
                user = str(input("[ + ] Please enter a path for username list, or leave blank for default [ + ]\n->"))
                password = str(input("[ + ] Please enter path for password list, or leave blank for default [ + ]\n->"))
                if user != '': Path(user)
                if password != '': Path(password)
                atk_log(smtp_enum(server=server, user=user, passwd=password))
                continue
            if options == '9':
                import ipaddress
                ip = str(input("[ + ] Please input an IP to locate [ + ]\n->"))
                atk_log(iplocator(ip))
                continue
            if options == 'e1':
                question = str(input("[ + ] Is the file outside of the default XML_Output directory? y/N\n->")).lower()
                if question == 'n':
                    try:
                        default_path = './XML_Output/scan.xml'
                        atk_log(exploit_db(default_path))
                        continue
                    except FileNotFoundError as e:
                        print("Hey! Hey! Hey! No one likes a liar... \n{}".format(e))
                if question == "y":
                    path = str(input("[ + ] Please put the full path to the file:\n->"))
                    if path != '':
                        from pathlib import Path
                        lib = Path(path)
                        atk_log(exploit_db(lib))
                        continue
                    if path == '':
                        print("[ !! ] Please input a path!! [ !! ]")
                        continue
            if options == "p1":
                print("[ * ] Sorry, that is a coming feature! [ * ]")
                continue
            if options == 'p2':
                print("[ + ] Still working on this and perfecting it! check back later! [ + ]")
                continue
            if options == '':
                os.system(clear)
                print("[ ! ] Please enter a value! [ ! ]")
                continue

        except KeyboardInterrupt:
            choice = str(input("\n[ + ] Would you like to exit? [ + ]\n->")).lower()
            if choice != "y":
                continue
            if choice == 'y':
                print("[ !! ] Good-Bye! [ !! ]")
                sys.exit(1)
