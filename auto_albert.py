try:
    import logging
    import geoip2
    from subprocess import Popen, PIPE
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
    from api import apikey, vulners_api
    import time
    import base64
    import os
    from time import sleep
    from termcolor import cprint
    from scapy.all import sr, srp, IP, UDP, ICMP, TCP, ARP, Ether
    import dpkt
    import vulners
    import asyncio
    import argparse
except (ImportError) as e:
    print("[✘] Something is terribly wrong:\n->{} [✘]".format(e))
    sys.exit(1)

ip = str(input("Enter destination IP or Host name:\n->"))
logging.basicConfig(filename="./atk_output/debug.txt",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")
PATH = './atk_output/'

PW_PATH = "./data/main_pass.txt"
NAMES_PATH = "./data/main_names.txt"
class Albert_api:
    def _pw_lists(path):
        logging.debug("Starting to import password lists, please be patient.\n")
        paths = path
        usersnames = set()
        try:
            with open(paths, 'r') as ax:
                sykes = ax.readlines()
                for line in sykes:
                    usersnames.add(line.strip('\n'))
                return usersnames
        except (IOError, FileNotFoundError) as e:
            logging.debug("[✘] Password List collection failure: {} [✘]\n\n".format(e))
            return e


    def _usernames(path):
        passes = set()
        paths = path
        with open(paths, 'r') as a:
            try:
                style = a.readlines()
                for line in style:
                    passes.add(line.strip('\n'))
                return passes
            except (IOError, FileNotFoundError) as e:
                logging.debug("[✘] Username collection routine failure: {} [✘]\n\n".format(e))
                return e


    def write_file(line):
        with open('hosts_list', 'at') as f:
            f.writelines(line)
        f.close()
        return False


    async def list_reject(target=''):
        logging.debug("--> Inside shodan scanner\n\n")
        api = shodan.Shodan(apikey)
        try:
            search = api.host(target)
            logging.debug("""
			    	IP: {}
				    Organization: {}
				    Operating System: {}
		    """.format(search['ip_str'], search.get('org', 'n/a'), search.get('os', 'n/a')))

        # Print all banners
            for item in search['data']:
                logging.debug("""
				    		Port: {}
					    	Banner: {}
				    """.format(item['port'], item['data']))
                oops = [str(search['ip_str'], "\n", str(search['data'], "\n"))]
                Albert_api.write_file(''.join(oops))
                return target
        except shodan.APIError as e:
            os.system('cls')
            logging.debug('[✘] Shodan Scanner Failure: {} [✘]\n\n'.format(e))
            option = input('[*] Shieeeet you wanna chagne that API Key? <Y/n>: ').lower()
            if option == ('y'):
                file = open('api.py', 'w')
                SHODAN_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid Shodan.io API Key: ')
                oppsie = ["apikey= ", "\"", str(SHODAN_API_KEY), "\""]
                file.write(''.join(oppsie))
                logging.debug('[~] File Dropped Nigga: ./api.py')
                file.close()
                return target


    async def nmapScan(ip):  # Nmap function created
        logging.debug("--> Inside Nmap scanning module\n\n")
        try:
            args = "-sS -p 15-6893 -sV --version-all -A -T2 -sC --data-length 180 -oX " \
                   "./XML_Outpot/{}.xml -vvv --reason".format(ip)
            logging.debug("[ + ] Using: {} [ + ]".format(args))
            command = 'nmap ' + ip + ' ' + args
            nmScanner = Popen([command], stdout=PIPE)
            logging.debug(nmScanner.communicate())
            return ip
        except Exception as e:
            logging.debug("[✘] Nmap Failure: {} [✘]".format(e))
            return ip


    async def subnet_discover(ip):
        logging.debug("--> Inside subnet discovery module\n\n")
        import netaddr
        try:
            question = netaddr.IPAddress(ip)
            response = netaddr.IPNetwork(ip).cidr
            logging.debug("Reverse DNS {}".format(question.reverse_dns))
            logging.debug("Subnet/CIDR: {}".format(response.cidr))
            logging.debug("Private? {}".format(question.is_private))
            logging.debug("Net Mask: {}".format(response.netmask))
            logging.debug("Broad Cast: {}".format(response.broadcast))
            logging.debug("Host Mask: {}".format(response.hostmask))
            logging.debug("Multicast: {}".format(question.is_multicast))
            return response
        except netaddr.core.AddrFormatError as es:
            logging.debug("[✘] Sorry, that was not an IP [✘] \n\t\t-> {}".format(es))
            return es


    def scapy_selection(net):
        logging.debug("-->Inside Scapy scanning:\n\n")
        import datetime as dt
        from scapy.all import srp, ETHER_ANY, ARPHDR_ETHER, conf, IFACES
        try:
            logging.debug("{}".format(IFACES.show(resolve_mac=True, print_result=True)))
            interface = str(input("[ + ] Please choose an interface [ + ]\n->"))
            ip = net
            time_start = dt.datetime.now()
            conf.verb = 0
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, iface=interface, inter=0.1)
            logging.debug("MAC and IP\n")
            for snd, rcv in ans:
                logging.debug(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
                stop_time = dt.datetime.now()
                total_time = time_start - stop_time
                logging.debug("[ ** ] Complete! [ ** ]")
                logging.debug("[ ** ] Finished in: {} [ ** ]".format(total_time))
            return ip
        except Exception as e:
            logging.debug("[✘] Scappy Failure: {} [✘]".format(e))
            return e


    async def dns_dumpster(domain):
        try:
            res = DNSDumpsterAPI({'verbose': True}).search(domain)
            aks = ['DNS Dumpster results:', '\n', str(res), '\n']
            logging.debug("[ + ] Searching for {} [ + ]".format(domain))
            logging.debug("\n[ + ] DNS Servers [ + ]")
            for entry in res['dns_records']['dns']:
                logging.debug(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
            logging.debug("\n[ + ] MX Records [ + ]")
            for entry in res['dns_records']['mx']:
                logging.debug(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
            logging.debug("\n[ + ] Host Records (A) [ + ]")
            for entry in res['dns_records']['host']:
                if entry['reverse_dns']:
                    logging.debug(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
                else:
                    logging.debug(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
            logging.debug("\n[ + ] TXT Records [ + ]")
            for entry in res['dns_records']['txt']:
                logging.debug("{}".format(entry))
            image_retrieved = res['image_data'] is not None
            logging.debug("\nRetrieved Network mapping image? {} (accessible in 'image_data')".format(image_retrieved))
            logging.debug(repr(base64.b64decode(res['image_data'])[:20]) + '...')
            xls_retrieved = res['xls_data'] is not None
            logging.debug("\nRetrieved XLS hosts? {} (accessible in 'xls_data')".format(xls_retrieved))
            logging.debug(repr(base64.b64decode(res['xls_data'])[:20]) + '...')
            return domain
        except Exception as e:
            print("[✘] DNS Dumpster Failure: {} [✘]".format(e))
            return e


    async def smtp_enum(server):
        import smtplib
        import pathlib
        port = '25'
        user = Albert_api._usernames(path=pathlib.Path(NAMES_PATH))
        passwd = Albert_api._pw_lists(path=pathlib.Path(PW_PATH))
        try:
            smtpServer = smtplib.SMTP(server, port)
            smtpServer.ehlo()
            smtpServer.starttls()
        except:
            logging.debug("[-] No server found [-]")
            sys.exit(1)
        for username, passe in user, passwd:
            con = smtplib.SMTP()
            try:
                ex = con.login(username, passe)
                logging.debug("[+] {} [+]".format(ex))
                return ex
            except Exception as e:
                logging.debug("[✘] SMTP Enum failure: {} [✘]".format(e))
                return e


    async def panel_find(server, adminList):
        import urllib3
        if adminList == '': adminList = open("./data/adm_list", "r")
        for admin in adminList.readlines():
            ax = set()
            ax.add(admin)
            x = urllib3.PoolManager()
            try:
                for item in ax:
                    lx = server + item
                    x.request('GET', lx)
                    if x.status == '200' or x.status != 200:
                        logging.debug("[-] Found Da Panel -> {}".format(lx))
                        return lx
            except Exception as e:
                logging.debug("[✘] Panel Find Failed: {} [✘]".format(str(e)))


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
                return logging.debug(db_search.communicate())
        except Exception as e:
            logging.debug("[✘] Exploit DB Failure: {} [✘]".format(e))
            return e


def netsh_pivot(option, iface, listenport, connectport, host):
    from subprocess import Popen, PIPE
    if option == '1':
        # put the popen connamds in here
        command = "{}{}{}".format(listenport, connectport, host)
        Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return


def netsh_pipe(choice, iface, listenport, connectport, host):
    if listenport == "" or connectport == "":
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


async def main(ip=ip):
    passive = asyncio.create_task(Albert_api.list_reject(ip))
    aggressive = asyncio.create_task(Albert_api.nmapScan(ip=ip))
    passiv_task = asyncio.create_task(Albert_api.subnet_discover(ip))
    pasiv_task = asyncio.create_task(Albert_api.dns_dumpster(ip))
    pas_task = asyncio.create_task(Albert_api.panel_find(ip, adminList=''))
    pa_task = asyncio.create_task(Albert_api.smtp_enum(ip))
    agre_task = asyncio.create_task(Albert_api.exploit_db())

if __name__ == "__main__":
    start = time.time()
    logging.debug("[+] Welcome! Starting run at: {} [+]".format(start))
    asyncio.run(main())
    end = time.time()
    logging.debug("[+] Finished at: {} [+]\n[+] Thank you for playing [+]".format(end - start))
