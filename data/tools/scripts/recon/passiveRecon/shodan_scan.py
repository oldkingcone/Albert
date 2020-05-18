try:
    import random
    from time import sleep
    import json
    import shodan
    import sys
    import os
    import shodan_keys as shodan_key
    import pathlib
    from tqdm import tqdm
except ImportError as e:
    print("[~] Please install the requirements file( pip install -r requirements) [~]\n {}".format(str(e)))
    sys.exit(1)

api = shodan.Shodan(shodan_key.shodan_key)

def progress_bar(time):
    for i in tqdm(range(int(time))):
        sleep(1)

def write_file(line):
    with open('hosts_list', 'at') as f:
        f.writelines(line)
    f.close()
    return False

def list_reject(target = ''):
    search = api.search(target)
    id_seen = set()
    for result in search["matches"]:
        if result["ip_str"] in id_seen:
            print("[~] Already seen: {} skipping! [~]".format(str(result["ip_str"])))
        else:
            print("[~] New IP Found! {} [~]".format(str(result["ip_str"])))
            oops = [str(result["ip_str"]), '\n']
            write_file(''.join(oops))
            id_seen.add(result["ip_str"])
    return False

try:
    os.system('clear')
    while True:
        test = str(input("[~] Please enter in a word to search for, or press enter to use default list [~]\n->"))
        if test == '':
            compled = ["port:\"21\"",
                       "port:\"22\"",
                       "port:\"23\"",
                       "port:\"80\"",
                       "port:\"8080\"",
                       "product:\"Windows\""
                       "product:\"Linux\"",
                       "product:\"Unix\"",
                       "product:\"apache\""]
            while True:
                sleep_time = random.randint(100,500)
                for item in compled:
                    print("[~] Selecting {} [~]".format(str(item)))
                    list_reject(item)
                progress_bar(sleep_time)
                continue
        if test != '':
            print("[~] Sorry for the basicness, this can only do 1 at a time. so, selecting user input of {}".format(
                str(test)))
            list_reject(test)
            continue
except (shodan.APIError, OSError, KeyError, KeyboardInterrupt) as s:
    print("[!] Something happened! [!]\n-> {}" .format(str(s)))