# -*- coding: utf-8 -*-
try:
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
except (ImportError) as e:
    print("Something is terribly wrong:\n->{}".format(e))

api = shodan.Shodan(apikey)


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
    try:
        search = api.host(target)
        # id_seen = set()
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
        logo = '''
		 ________   __        _______   ______   ______   _________   
		/_______/\ /_/\     /_______/\ /_____/\ /_____/\ /________/\  
		\::: _  \ \\:\ \    \::: _  \ \\::::_\/_\:::_ \ \\__.::.__\/  
		 \::(_)  \ \\:\ \    \::(_)  \/_\:\/___/\\:(_) ) )_ \::\ \    
		  \:: __  \ \\:\ \____\::  _  \ \\::___\/_\: __ `\ \ \::\ \   
		   \:.\ \  \ \\:\/___/\\::(_)  \ \\:\____/\\ \ `\ \ \ \::\ \  
			\__\/\__\/ \_____\/ \_______\/ \_____\/ \_\/ \_\/  \__\/ 
		is Restarting'''
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


def nmapScan(tgtHost, tgtPort):  # Nmap function created
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    nmScan.csv()
    print("[ ! ]  {}\n TCP: {} \n UP/DOWN: {}\n".format(tgtHost, tgtPort, state))
    return False


def subnet_discover(ip):
    import netaddr
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


def scapy_selection(net):
    import datetime as dt
    from scapy.all import srp, ETHER_ANY, ARPHDR_ETHER, conf
    try:
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


if __name__ == '__main__':
    # @todo bring in a honeypot detection routine.
    # @todo a way to avoid docker containers like the plague.
    # @todo DNS Dumpster routine
    # @todo, Scapy routine, to create custom icmp messages on the fly. -> going with ARP instead
    # @todo, add packet sniffing on the fly.
    run = 't'
    albert_faces()
    sleep(0.4)
    while run == 't':
        try:
            os.system('cls')
            options = str(input("\n\n\n\t[ + ] Would you like to use:\n"\
                                "\t\t1. ) Shodan\n"\
                                "\t\t2. ) Nmap(Targeted Scanning of host system written out to XML file)\n"\
                                "\t\t3. ) Subnet Discovery\n"\
                                "\t\t4. ) NMAP Scan of subnet hosts(ARP or ICMP ACK)\n"\
                                "\t\t5. ) DNSDumpster for invalid Domain setups\n"\
                                "\t\t6. ) Windows API Manipulation\n"\
                                "\t\t- > Press CTRL + C to return to the menu < -\n\n\n"\
                                "[ * ] - >"))
            if options == '1':
                os.system('cls')
                choice = str(input("[ + ] Is this a file list, or a single IP:\n"\
                                   "1.) File List\n"\
                                   "2.) Single IP\n"\
                                   "->"))
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
                os.system('cls')
                host = str(input("[ + ] Please input host IP:\n->"))
                port = str(input("[ + ] Please input port:\n->"))
                try:
                    nmapScan(host, port)
                except KeyError as e:
                    print("[ !! ] IP Must not be a valid IP: \n{}".format(e))
                    continue
            if options == "3":
                choice = str(input("[ + ] Please input the subnet to detect [ + ]\n->"))
                if choice != '':
                    subnet_discover(choice)
                    continue
            if options == "4":
                chance = str(input("[ ** ] Are you choosing\n1.) ARP\n2.) ICMP ACK\n->"))
                if chance == "2":
                    print("[ !! ] So sorry, not done with that yet... [ !! ]")
                    continue
                if chance == "1":
                    strike = str(input("[ + ] Please enter the IP, we will need to scan the subnet [ + ]"))
                    scapy_selection(subnet_discover(strike))
                    continue
            if options == "5":
                choice = str(input("[ * ] Please enter a domain name: [ * ]\n->"))
                res = DNSDumpsterAPI({'verbose': True}).search(choice)
                print("[ + ] Searching for {} [ + ]".format(choice))
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
                continue
            if options == "6":
                print("[ * ] Sorry, that is a coming feature! [ * ]")
                continue

            if options == '':
                os.system('cls')
                print("[ ! ] Please enter a value! [ ! ]")
                print("[ ?? ] Exiting! [ ?? ]")
                sys.exit(1)
        except KeyboardInterrupt:
            choice = str(input("[ + ] Would you like to exit? [ + ]\n->")).lower()
            if choice != "y":
                continue
            if choice == 'y':
                print("[ !! ] Good-Bye! [ !! ]")
                sys.exit(1)


