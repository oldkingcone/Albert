from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import shodan
from data.api_keys.api import *
import os
import base64


def write_file(line):
    with open('hosts_list', 'at') as f:
        f.writelines(line)
    f.close()
    return False


class massivePassiveScan:

    def list_reject(target, clear):
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
                file = open('data/api_keys/api.py', 'w')
                SHODAN_API_KEY = input('[*] Hey! Hey! Hey! Enter A Valid Shodan.io API Key: ')
                oppsie = ["apikey= ", "\"", str(SHODAN_API_KEY), "\""]
                file.write(''.join(oppsie))
                return False

    def dns_dumpster(domain, clear):
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
            print("{}".format(e))
            return e

    def exploit_db(file, clear):
        from subprocess import PIPE, Popen
        default = './data/tools/output/XML_Output/scan.xml'
        try:
            if file == '':
                command = 'searchsploit -x --nmap {}'.format(default)
                db_search = Popen([command], stdout=PIPE, stderr=PIPE)
                print(db_search.communicate())
            if file != '':
                fil = file
                command = 'searchsploit -x --nmap {}'.format(fil)
                db_search = Popen([command], stdout=PIPE, stderr=PIPE)
                print(db_search.communicate())
        except Exception as e:
            print("{}".format(e))
            return e