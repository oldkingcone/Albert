# -*- coding: utf-8 -*-
try:
    from vulnersapi import api
    from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
    import sched
    import random
    import urllib
    import shodan
    import sys
    import nmap
    from api import apikey
    from tqdm import tqdm as tqdm
    import time
    import base64
    import os
    from time import sleep
    from termcolor import cprint
    from scapy.all import sr, srp, IP, UDP, ICMP, TCP, ARP, Ether
    import dpkt
    import vulners
except (ImportError) as e:
    print("Something is terribly wrong:\n->{}".format(e))
    sys.exit(1)

logo = '''
 ________   __        _______   ______   ______   _________   
/_______/\ /_/\     /_______/\ /_____/\ /_____/\ /________/\  
\::: _  \ \\:\ \    \::: _  \ \\::::_\/_\:::_ \ \\__.::.__\/  
 \::(_)  \ \\:\ \    \::(_)  \/_\:\/___/\\:(_) ) )_ \::\ \    
  \:: __  \ \\:\ \____\::  _  \ \\::___\/_\: __ `\ \ \::\5 \   
   \:.\ \  \ \\:\/___/\\::(_)  \ \\:\____/\\ \ `\ \ \ \::\ \  
    \__\/\__\/ \_____\/ \_______\/ \_____\/ \_\/ \_\/  \__\/ 
is Restarting'''

def albert_faces():
    alberts = ''
    albert = random.randint(1, 6)
    if albert == 1: alberts = "./art/albert_face.txt"
    if albert == 2: alberts = "./art/albert_face_2.txt"
    if albert == 3: alberts = "./art/fat_albert_3"
    if albert == 4: alberts = "./art/memo_cat"
    if albert == 5: alberts = "./art/memo_logo"
    if albert == 6: alberts = "./art/memo_logo_2"
    face = open(alberts, "r")
    lulz = face.readlines()
    for line in lulz:
        cprint(line.strip("\n"), 'green')
        sleep(0.5)
    sleep(0.5)
    cprint("Loading The King Himself Hopefully He Left You Some Exploits....", 'red')
    sleep(0.5)
    cprint("Gr33ts: Chef Gordon, Root, Johnny 5", 'red')


def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        time.sleep(1)


def write_file(line):
    with open('hosts_list', 'at') as f:
        f.writelines(line)
    f.close()
    return False


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
        os.system('cls')
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


def nmapScan(tgtHost, tgtPort, args):  # Nmap function created
    from subprocess import Popen, PIPE
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
        return False


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


def scapy_selection(net):
	#the interface list works wonders on windows, but not on linux.
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
    except:
        raise

def dns_dumpster(domain):
    try:
        res = DNSDumpsterAPI({'verbose': True}).search(domain)
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
    except:
        raise

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
                                                               'modified', 'published', 'id', 'href', 'title', 'vector',
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
    if file == '':
        command = 'searchsploit -x --nmap ./XML_Output/scan.xml'
        db_search = Popen([command], stdout=PIPE)
        print(db_search.communicate())
    if file != '':
        fil = file
        command = 'searchsploit -x --nmap '+ fil
        db_search = Popen([command], stdout=PIPE)
        print(db_search.communicate())

if __name__ == '__main__':
    # @todo bring in a honeypot detection routine.
    # @todo a way to avoid docker containers like the plague.
    # @todo, add packet sniffing on the fly. <- debating on using this.
    run = 't'
    albert_faces()
    sleep(0.4)
    while run == 't':
        try:
            os.system('cls')
            options = str(input("\n\n\n\t[ + ] Would you like to use:\n"\
                                "\t\t1. ] Shodan\n"\
                                "\t\t2. ] Nmap(Targeted Scanning of host system written out to XML file)\n"\
                                "\t\t3. ] Subnet Discovery\n"\
                                "\t\t4. ] NMAP Scan of subnet hosts(ARP or ICMP ACK)\n"\
                                "\t\t5. ] DNSDumpster for invalid Domain setups\n"\
                                "\t\t6. ] Windows API Manipulation\n"\
                                "\t\t7. ] Vulners DB Search API\n"\
                                "\t\t- > Press CTRL + C to return to the menu < -\n"\
                                "\t --------------------------------------------------\n"
                                "\t Please ensure that all recon is done at least with nmap before using this\n"\
                                "\t Section of this tool."\
                                "\t 8. ] Exploit DB\n"\
                                "[ * ] - >"))
            if options == '1':
                os.system('cls')
                choice = str(input("[ + ] Is this a file list, or a single IP:\n"\
                                   "\t1 . ) File List\n"\
                                   "\t2 . ) Single IP\n"\
                                   "[ + ] ->"))

                if choice == '1':
                    os.system('cls')
                    dest = str(input("[ + ] Please input the name of the file list:\n->"))
                    liz = set()

                    if dest == '':
                        os.system('cls')
                        print("[ ! ] Hey! Hey! Hey! Need a file name! [ ! ]")
                        run = 'a'
                    reader = open(dest, "r")
                    for line in reader.readlines():
                        line.strip("\n")
                        list_reject(line)
                    continue

                if choice == '2':
                    os.system('cls')
                    choice = str(input("[ + ] Please Input the IP: \n->"))
                    list_reject(choice)
                    continue

            if options == '2':
                def_args = "-sW -p 15-6893 -sV --version-all -A -T2 -sC -S www.microsoft.com --data-length 180 -oX" \
                           "./XML_Outpot/scan.xml -vvv --reason"
                print("Default Args: \n{}".format(def_args))
                question = str(input("[ + ] Would you like to use custom args with the nmap scan? [ + ] \n->")).lower()
                if question == 'n':
                    os.system('cls')
                    host = str(input("[ + ] Please input host IP:\n->"))
                    port = str(input("[ + ] Please input port:\n->"))
                    try:
                        nmapScan(host, port, args=def_args)
                    except KeyError as e:
                        print("[ !! ] IP Must not be a valid IP: \n{}".format(e))
                        continue
                    continue
                if question == 'y':
                    os.system('cls')
                    def_args = "-sW -p 15-6893 -sV --version-all -A -T2 -sC -S www.microsoft.com --data-length 180 -oX" \
                               "./XML_Outpot/scan.xml -vvv --reason"
                    host = str(input("[ + ] Please input host IP:\n->"))
                    port = str(input("[ + ] Please input port:\n->"))
                    args = str(input("[ + ] Please enter the full commands:\n Eample: -f -t 0 -n -Pn –data-length 200 -D"\
                                     "\n->"))
                    print("Default Args: \n{}".format(def_args))
                    if args == '':
                        nmapScan(host, port, args=def_args)
                        continue
                    if args != '':
                        nmapScan(host, port, args=args)
                        continue

            if options == "3":
                choice = str(input("[ + ] Please input the subnet to detect [ + ]\n->"))

                if choice != '':
                    subnet_discover(choice)
                    continue

            if options == "4":
                chance = str(input("[ ** ] Are you choosing\n"\
                                   "\t1. ) ARP\n"\
                                   "\t2. ) ICMP ACK [ ** ]\n[ + ] ->"))
                if chance == "2":
                    print("[ !! ] So sorry, not done with that yet... [ !! ]")
                    continue

                if chance == "1":
                    strike = str(input("[ + ] Please enter the IP, we will need to scan the subnet [ + ]"))
                    scapy_selection(subnet_discover(strike))
                    continue

            if options == "5":
                domain = str(input("[ * ] Please enter a domain name: [ * ]\n->"))
                dns_dumpster(domain=domain)
                continue

            if options == "6":
                print("[ * ] Sorry, that is a coming feature! [ * ]")
                continue

            if options == "7":
                choice = str(input("[ + ] VulnersDB search API:\n"\
                                   "\t1 . ) Search by term\n"\
                                   "\t2 . ) Search by CVE code\n"\
                                   "\t3 . ) Search for specific exploits\n"\
                                   "\t4 . ) Search by term and Version Number [ + ]\n"\
                                   "[ + ] - >"))
                if choice == "1":
                    term = str(input("[ + } Please input a string to search for [ + ]\n->"))
                    vulners_api(option="1", term=term)
                    continue
                if choice == "2":
                    term = str(input("[ + } Please input a Doc to search for [ + ]\n->"))
                    vulners_api(option="2", term=term)
                    continue
                if choice == "3":
                    term = str(input("[ + } Please input a CVE number to search for \n"\
                                     "example: CVE-2017-14174 [ + ]\n->"))
                    vulners_api(option="3", term=term)
                    continue
                if choice == "4":
                    term = str(input("[ + } Which software are we to search for [ + ]\n->"))
                    vulners_api(option="4", term=term)
                    continue
            if options == '8':
                question = str(input("[ + ] Is the file outside of the default XML_Output directory? y/N\n->")).lower()
                if question == 'n':
                    try:
                        default_path = './XML_Output/scan.xml'
                        exploit_db(default_path)
                        continue
                    except FileNotFoundError as e:
                        print("Hey! Hey! Hey! No one likes a liar... \n{}".format(e))
                if question == "y":
                    path = str(input("[ + ] Please put the full path to the file:\n->"))
                    if path != '':
                        from pathlib import Path
                        lib = Path(path)
                        exploit_db(lib)
                        continue
                    if path == '':
                        print("[ !! ] Please input a path!! [ !! ]")
                        continue
            if options == '':
                os.system('cls')
                print("[ ! ] Please enter a value! [ ! ]")
                continue

        except KeyboardInterrupt:
            choice = str(input("[ + ] Would you like to exit? [ + ]\n->")).lower()
            if choice != "y":
                continue
            if choice == 'y':
                print("[ !! ] Good-Bye! [ !! ]")
                sys.exit(1)


