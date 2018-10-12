# F.A.T Albert
### The Albert
#### Synopsis
-----


The smart penetration testing tool. This tool is meant as an all in one for penetration testing, **mixing some __tried and tested methods__** for gathering recon on a __single machine__ or an entire __subnet__. With output being printed into Nmap XML format for easy use with ExploitDB. The scans used within this tool will be incredibly verbose and make its best attempt at service identification, although it uses subprocess to leverage the strength and power of Nmap, it still combines the extra steps into a single tool. This fixes 2 issues, the first being having to manually run all XML output through ExploitDB to find the most likely exploits to use against your clients machine, **AND** simplifies the recon process.


-----



***`sudo apt install python3-setuptools python3-minimal python3-pip python-dev python3-dev python3-scapy python3-tqdm python3-termcolor python3-shodan nmap exploitdb`***

__OR:__


> sudo apt install nmap exploitdb python3-setuptools python3-minimal python3-pip python-dev python3-dev


__ Then run:__


> sudo pip3 install -r requirements
