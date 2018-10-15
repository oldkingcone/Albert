def netsh_pivot(option, iface, listenport, connectport, host):
    from subprocess import Popen, PIPE
    if option == '2':
        # put the popen connamds in here
        command = "{}{}{}".format(listenport, connectport, host)
        Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return 
    if option =='2':
        return 1
    if option == '3':
        return 1
