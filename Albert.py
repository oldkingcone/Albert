#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import sched
    import random
    import urllib
    from urllib.request import urlopen
    import http.client
    from urllib import parse
    import shodan
    import sys
    import nmap
    import optparse
    from api import apikey
    from tqdm import tqdm as tqdm
    import time
    import os
    import platform
    from time import sleep
    from termcolor import cprint
    from scapy.all import sr, srp, IP, UDP, ICMP, TCP, ARP, Ether
    import dpkt
except (ImportError) as e:
    print("Something is terribly wrong:\n->{}".format(e))

ap = apikey
if ap == '':
    print("Your API Key empty: \n->{}".format(ap))
    sys.exit(1)

api = shodan.Shodan(apikey)

def albert_faces():
    alberts = ''
    albert = random.randint(1, 6)
    if albert == 1: alberts = "./albert_face.txt"
    if albert == 2: alberts = "./albert_face_2.txt"
    if albert == 3: alberts = "./fat_albert_3"
    if albert == 4: alberts = "./memo_cat"
    if albert == 5: alberts = "./memo_logo"
    if albert == 6: alberts = "./memo_logo_2"
    face = open(alberts, "r")
    lulz = face.readlines()
    for line in lulz:
        cprint(line.strip("\n"), 'green')
        sleep(0.5)
    sleep(0.5)
    cprint("Loading The King Himself Hopefully He Left You Some Exploits....", 'red')
    sleep(0.5)
    cprint("Gr33ts: Chef Gordon, Root, Johnny 5", 'red')

test = platform.system()
if test == 'Windows': clear = 'cls'
elif test == 'Linux': clear = 'clear'
elif test == 'Java': clear = 'clear'
elif test == '':
    print("[ ! ] Exiting, you have an unknown system! [ ! ] ")
    sys.exit(1)

def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        time.sleep(1)


def write_file(line):
    with open('hosts_list', 'at') as f:
        f.writelines(line)
    f.close()
    return False

def list_reject(target = ''):
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
        os.system(clear)
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
        if option.startswith('y'):
            file = open('api.py', 'w')
            SHODAN_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid Shodan.io API Key: ')
            oppsie = ["apikey= ", "\"",  str(SHODAN_API_KEY), "\""]
            file.write(''.join(oppsie))
            print('[~] File Dropped Nigga: ./api.py')
            file.close()
            print('[~] Take 5 To Larp Around\n {}'.format(logo))
            return False

def nmapScan(tgtHost, tgtPort):  # Nmap function created
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[ ! ]  {}\n TCP: {} \n UP/DOWN: {}\n".format(tgtHost, tgtPort, state))
    return False


def subnet_discover(ip):
    import netaddr
    question = netaddr.IPAddress(ip).reverse_dns()
    print("Reverse DNS {}".format(netaddr.IPAddress(ip).reverse_dns()))
    print("Subnet/CIDR: {}".format(netaddr.IPNetwork(ip).cidr()))
    print("Private? {}".format(netaddr.IPNetwork.is_private(ip)))
    print("Net Mask: {}".format(netaddr.IPNetwork(ip).netmask()))
    print("Broad Cast: {}".format(netaddr.IPNetwork(ip).broadcast()))
    print("Host Mask: {}".format(netaddr.IPNetwork(ip).hostmask()))
    print("Multicast: {}".format(netaddr.IPNetwork(ip).is_multicast()))
    return question

def scapy_selection(net):
    import datetime as dt
    from scapy.all import srp,ETHER_ANY,ARPHDR_ETHER,conf
    try:
        interface = str(input("[ + ] Please choose an interface [ + ]\n->"))
        ip = net
        time_start = dt.datetime.now()
        conf.verb = 0
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, iface=interface, inter=0.1)
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
    #@todo bring in a honeypot detection routine.
    #@todo a way to avoid docker containers like the plague.
    #@todo DNS Dumpster routine
    #@todo, Scapy routine, to create custom icmp messages on the fly. -> going with ARP instead
    #@todo, add packet sniffing on the fly.
    #@todo, add functionality to dump nmap
    run = 't'
    albert_faces()
    sleep(0.4)
    while run == 't':
        try:
            os.system(clear)
            options = str(input("[ + ] Would you like to use:\n"
                       "1.) Shodan\n"
                       "2.) Nmap(Targeted Scanning of host system written out to XML file)\n"
                       "3.) Inactive(Zombie Host Scapy Scan)\n"
                       "4.) NMAP Scan of subnet hosts(ARP or ICMP ACK)\n"
                       "->"))
            if options == '1':
                os.system(clear)
                choice = str(input("[ + ] Is this a file list, or a single IP:\n"
                           "1.) File List\n"
                           "2.) Single IP\n"
                           "->"))
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
                        list_reject(line)
                if choice == '2':
                    os.system(clear)
                    choice = str(input("[ + ] Please Input the IP: \n->"))
                    list_reject(choice)

            if options == '2':
                os.system(clear)
                host = str(input("[ + ] Please input host IP:\n->"))
                port = str(input("[ + ] Please input port:\n->"))
                nmapScan(host, port)
            if options == "3":
                choice = str(input("[ + ] Please input the subnet to detect [ + ]\n->"))
                if choice != '':
                    subnet_discover(choice)
            if options == "4":
                chance = str(input("[ ** ] Are you choosing\n"
                                   "1.) ARP\n"
                                   "2.) ICMP ACK\n->"))
                if chance == "2":
                    print("[ !! ] So sorry, not done with that yet... [ !! ]")
                    continue
                if chance == "1":
                    strike = str(input("[ + ] Please enter the IP, we will need to scan the subnet [ + ]"))
                    scapy_selection(subnet_discover(strike))
            if options == '':
                os.system(clear)
                print("[ ! ] Please enter a value! [ ! ]")
                print("[ ?? ] Exiting! [ ?? ]")
                sys.exit(1)
        except:
            raise
