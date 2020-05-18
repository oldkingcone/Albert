from subprocess import Popen,PIPE
import nmap

class massiveScanner:

    def massBanner(target, configFile):
        if configFile != '':
            if target != '':
                allTheBanners = f"masscan {target} -q {configFile}"
            else:
                allTheBanners = f"masscan -q {configFile}"
            banners = Popen()

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