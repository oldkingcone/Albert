#!/usr/bin/env python3
try:
    from proxybroker import Broker
    import aiohttp
    from proxybroker import Broker, ProxyPool
    from proxybroker.errors import NoProxyError
    from urllib.parse import urlparse
    import geoip2
    from subprocess import Popen, PIPE
    import pathlib
    import time
    from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
    import sched
    import random
    import shodan
    import sys
    from api import apikey, vulners_api
    import time
    import base64
    import os
    from time import sleep
    from termcolor import cprint
    from scapy.all import sr, srp, IP, UDP, ICMP, TCP, ARP, Ether
    # import dpkt
    import vulners
    import asyncio
except (ImportError) as e:
    print("[✘] Something is terribly wrong:\n->{} [✘]".format(e))
    sys.exit(1)

# if os.getuid() != 0:
#     cprint("Please run this as root.", 'red')
#     sys.exit(1)

PATH = './atk_output/'
PW_PATH = "./data/main_pass.txt"
NAMES_PATH = "./data/main_names.txt"
class Albert_api:

    def _pw_lists(path):
        print("Starting to import password lists, please be patient.\n")
        usersnames = set()
        try:
            with open(path, 'r') as ax:
                sykes = ax.readlines()
                for line in sykes:
                    usersnames.add(line.strip('\n'))
                return usersnames
        except (IOError, FileNotFoundError) as e:
            print("[✘] Password List collection failure: {} [✘]\n\n".format(e))
            return e


    def _usernames(path):
        passes = set()
        with open(path, 'r') as a:
            try:
                style = a.readlines()
                for line in style:
                    passes.add(line.strip('\n'))
                return passes
            except (IOError, FileNotFoundError) as e:
                print("[✘] Username collection routine failure: {} [✘]\n\n".format(e))
                return e


    def write_file(line):
        with open('hosts_list', 'at') as f:
            f.writelines(line)
        f.close()
        return False


    async def list_reject(target=''):
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
                Albert_api.write_file(''.join(oops))
                return target
        except shodan.APIError as e:
            os.system('cls')
            print('[✘] Shodan Scanner Failure: {} [✘]\n\n'.format(e))
            option = input('[*] Shieeeet you wanna chagne that API Key? <Y/n>: ').lower()
            if option == ('y'):
                file = open('api.py', 'w')
                SHODAN_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid Shodan.io API Key: ')
                oppsie = ["apikey= ", "\"", str(SHODAN_API_KEY), "\""]
                file.write(''.join(oppsie))
                print('[~] File Dropped Nigga: ./api.py')
                file.close()
                return target


    async def nmapScan(ip):  # Nmap function created
        try:
            args = "-sS -p 15-6893 -sV --version-all -A -T2 -sC --data-length 180 -oX " \
                   "./XML_Outpot/{}.xml -vvv --reason".format(ip)
            print("[ + ] Using: {} [ + ]".format(args))
            command = 'nmap ' + ip + ' ' + args
            nmScanner = Popen([command], stdout=PIPE)
            print(nmScanner.communicate())
            return ip
        except Exception as e:
            print("[✘] Nmap Failure: {} [✘]".format(e))
            return ip


    async def subnet_discover(ip):
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
            print("[✘] Sorry, that was not an IP [✘] \n\t\t-> {}".format(es))
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
            return ip
        except Exception as e:
            print("[✘] Scappy Failure: {} [✘]".format(e))
            return e


    async def dns_dumpster(domain):
        try:
            res = DNSDumpsterAPI({'verbose': True}).search(domain)
            aks = ['DNS Dumpster results:', '\n', str(res), '\n']
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
            print("[✘] DNS Dumpster Failure: {} [✘]".format(e))
            return e


    async def smtp_enum(server, port):
        # self.server = str(server)
        import smtplib
        import pathlib
        user = Albert_api._usernames(path=pathlib.Path(NAMES_PATH))
        passwd = Albert_api._pw_lists(path=pathlib.Path(PW_PATH))
        try:
            smtpServer = smtplib.SMTP(server, port)
            smtpServer.ehlo()
            smtpServer.starttls()
        except ConnectionRefusedError as e:
            print("[-] SMTP Connection Refused: {} [-]".format(str(e)))
            await asyncio.sleep(1)
            return e
        for username in user:
            for passw in passwd:
                con = smtplib.SMTP()
                try:
                    ex = con.login(username, passw)
                    print("[+] {} [+]".format(ex))
                    return ex
                except Exception as e:
                    print("[✘] SMTP Enum failure: {} [✘]".format(e))
                    return e


    async def panel_find(server, adminList):
        import urllib3
        if adminList == '': adminList = open("./data/adm_list", "r")
        for admin in adminList.readlines():
            ax = set()
            ax.add(admin.strip("\n"))
            x = urllib3.PoolManager()
            try:
                for item in ax:
                    lx = server + "/"+item
                    print(lx)
                    x.request('GET', lx, retries=False)
                    await asyncio.sleep(1)
                    if x.status == '200' or x.status != 200:
                        print("[-] Found Da Panel -> {}".format(lx))
                        return lx
            except (BaseException, WindowsError) as e:
                print("[✘] Panel Find Failed: {} [✘]".format(str(e)))


# async def iplocator(ip):
# going to replace with maxminds API/DB for ip location generation.
#     import urllib3
#     url = "http://ip-api.com/json/"+ip
#     try:
#         u = urllib3.PoolManager()
#         x = u.request('GET', url)
#         if x.status != '200' or x.status != 200:
#             print("[ + ] Failed at request! [ + ]")
#             pass
#         else:
#             print(x.data)
#     except Exception as e:
#         print("[-} Did Not Work:\n{} [~]".format(e))

    async def exploit_db():
        from subprocess import PIPE, Popen
        scan = list()
        for files in os.listdir('./XML_Output/'):
            if files.endswith(".xml"):
                set.add(files)
        try:
            for item in scan:
                command = 'searchsploit -x --nmap {}'.format(str(item))
                db_search = Popen([command], stdout=PIPE, stderr=PIPE)
                return print(db_search.communicate())
        except Exception as e:
            print("[✘] Exploit DB Failure: {} [✘]".format(e))
            return e

async def main(ip):
    subnets = [ip+"/10", ip+"/12",ip+"/16", ip+"/24", ip+"/32"]
    smtp_ports = ["25", "2525", "465"]
    pop3_ports = []
    imap_ports = []
    #@todo add imap and pop3 username enumeration.

    passive = asyncio.create_task(Albert_api.list_reject(ip))

    for i in subnets:
        await asyncio.gather(
            asyncio.create_task(Albert_api.nmapScan(ip=i)))

    passiv_task = asyncio.create_task(Albert_api.subnet_discover(ip))

    pasiv_task = asyncio.create_task(Albert_api.dns_dumpster(ip))
    pas_task = asyncio.create_task(Albert_api.panel_find(ip, adminList=''))
    for x in smtp_ports:
        await asyncio.gather(asyncio.create_task(Albert_api.smtp_enum(ip, x)))

    agre_task = asyncio.create_task(Albert_api.exploit_db())

    await passive
    await passiv_task
    await pasiv_task
    await pas_task
    await agre_task

ip = str(input("Enter destination IP or Host name:\n->"))
start = time.time()
print("[+] Welcome! Starting run at: {} [+]".format(start))
asyncio.run(main(ip))
end = time.time()
print("[+] Finished at: {} [+]\n[+] Thank you for playing [+]".format(end - start))
