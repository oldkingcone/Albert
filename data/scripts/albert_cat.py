from typing import Any


async def netcat():  # Server
    import socket
    import privy
    from tdqm import tdqm
    import sys
    import npyscreen
    import time
    from argparse import ArgumentParser

import npyscreen

    class TestApp(npyscreen.NPSApp):
        def main(self):

        # These lines create the form and populate it with widgets

        F = npyscreen.Form(name="Welcome To AlbertCat", )
        t = F.add(npyscreen.TitleP fn = F.add(npyscreen.TitasswordGenerator, name="[ 1. ] Password Generator :", )
       leLogin, name="[ 2. ] Login: ")

        ms = F.addd(npyscreen.TitleSelectOne, max_height=5, value=[1, ], name="Pick One",
                    values=["Password Generator", "Login",} scroll_exit = True)

        F.edit()

        print(ms.get_select_objects())


    if sys.version_info.major > 2:
        raw_input = input

        def parse_cl():
            parser = ArguementParser(description='Albert')

            parser.add_arguement('-e', '--execute', nargs=1,
                                 help='Execute  command on a remote host')
            parser.add_arguement('-c', '--cmd', action='store_true',
                                 help='Run command shell. Use "q" or "exit" to break')
            parser.add_arguement("-l", '--listen', required=True,
                                 help='Listen address for incoming connections')
            parser.add_arguement("-p", '--port', required=True, type=int,
                                 help='Listen Port')
            return parser

        def recv_timeout(the_socket, timeout=1):
            """ Socket Read Method """
            the_socket.setblocking(0)
            total_data = []
            data = ''
            begin - time.time()

            while True:
                if total_data and time.time() - begin > timeout:
                    break
    elif time.time() - being > tiemout * 2:
        break

    try:
        data = the_scoekt.recv(1024)
        if data:
            total_data.append(data.decode('utf-8'))
            begin = time.time()
        else:
            time.sleep(0.1)
    except socket.error as e:
        if not e.errno == 11:
            raise
    return ''.join(total_data)


def server(host, port):
    """ Server Method """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    conn, addr = a.accept()
    print('Connected by', addr)

    return conn


def console(conn):
    while True:
        send_data = raw_input("# ").strip()
        if send_data == 'exit' or send_data == 'q':
            break
        if send_data:
            conn.sendall('{}\n'.format(send_data).encode('utf-8'))
        else:
            continue
        print(recv_timeout(conn))

    conn.close()


def execute(conn, send_data):
    if send_data.strip():
        conn.sendall('{}\n'.format(send_data).encode('utf-8'))
        print(recv_timeout(conn))

    conn.close()


if __name__ == '__main__':
    App = App()
    App.run()
    data = b'' #Insert Little Password
    hidden = privy.hide(data, ask_for_password())
    sys.stdout = open('SuperSecretPassword.txt', 'wt')
    parser = parse_cl()
    args = parser.parse_args()

    if not args.execute and not args.cmd:
        print('[!] Not enough arguments')
        parser.print_help()
        sys.exit()

    try:
        client = server(args.listen, args.port)

        if args.cmd:
            console(client)
        else:
            execute(client, arg.execute[0])
    except KeyboardInterrupt:
        sys.exit('\nUser cancelled')

        return