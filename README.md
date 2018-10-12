# F.A.T Albert
### The Albert
#### Synopsis
-----


  The smart penetration testing tool. This tool is meant as an all in one for penetration testing, **mixing some __tried and tested methods__** for gathering recon on a __single machine__ or an entire __subnet__. With output being printed into Nmap XML document for easy use with ExploitDB. The scans used within this tool will be incredibly verbose and make its best attempt at service identification, although it uses __subprocess__ to leverage the strength and power of Nmap, it still combines the extra steps into a single tool. This fixes 2 issues, the first being having to manually run all XML output through ExploitDB to find the most likely exploits to use against your clients machine, **AND** simplifies the recon process.

-----

#### Install:
---
>sudo apt install python3-setuptools python3-minimal python3-pip python-dev python3-dev python3-scapy python3-tqdm python3-termcolor python3-shodan nmap exploitdb

__OR:__


> sudo apt install nmap exploitdb python3-setuptools python3-minimal python3-pip python-dev python3-dev

> sudo pip3 install -r requirements

Upon successful installation of the required packages, you will __NEED__ to acquire an API key to use VulnersDB from:
[https://www.vulners.com](https://www.vulners.com)

---

#### Usage:
---


  The useage of this tool is very easy, there is a guided menu. The options are seperated by type, future editions of this tool will incoporate exploitation and post-exploitation phases to further simplify the whole process. Along with the additions of those 2 phases, it will also have the ability to automate the whole process, and not just shotgun blast exploits at a clients machine in the hope that one will work. 


---
