# F.A.T Albert

### The Albert
---
#### Synopsis:
  The smart penetration testing tool. This tool is meant as an all in one for penetration testing, **mixing some __tried and tested methods__** for gathering recon on a __single machine__ or an entire __subnet__. 
  
  With output being printed into Nmap XML document for easy use with ExploitDB. The scans used within this tool will be incredibly verbose and make its best attempt at service identification, although it uses __subprocess__ to leverage the strength and power of Nmap, it still combines the extra steps into a single tool. This fixes 2 issues, the first being having to manually run all XML output through ExploitDB to find the most likely exploits to use against your clients machine, **AND** simplifies the recon process. The **best** part of this tool, is it uses both active scanning or passive scanning, the choice is at your fingertips, it leverages the power of Shodan with all results written to a single file(overwritten each run) for later review, the full logging of the shodan results can be found inside the `atk_output` folder, matter of a fact, __ALL__ output from each scan can be found inside the `atk_output` folder [Example](https://github.com/oldkingcone/Albert/tree/master/atk_output). 
  
  This tool will also make an attempt to retrieve the Geo Location data for a specified IP address. And to top it all off, this program will attempt to enumerate SMTP username's and password's, leveraging the power of SecLists.

-----

#### Install:

>sudo apt install python3-setuptools python3-minimal python3-pip python-dev python3-dev python3-scapy python3-tqdm python3-termcolor python3-shodan nmap exploitdb

__OR:__


> sudo apt install nmap exploitdb python3-setuptools python3-minimal python3-pip python-dev python3-dev

> sudo pip3 install -r requirements

Upon successful installation of the required packages, you will __NEED__ to acquire an API key to use VulnersDB from:
[https://www.vulners.com](https://www.vulners.com)

---

#### Usage:

  The useage of this tool is very easy, there is a guided menu. The options are seperated by type, future editions of this tool will incoporate exploitation and post-exploitation phases to further simplify the whole process. Along with the additions of those 2 phases, it will also have the ability to automate the whole process, and not just shotgun blast exploits at a clients machine in the hope that one will work. 


---


### Future Features:

1. Automation of Recon Phase
   1. Add Option to choose automated recon phase with little printed out to the screen, other than the reccommended exploits, suggested by ExploitDB.
   2. Make this into an API so it can be imported into other projects.
2. A routine that, based off of information collected from the targeted system, populates the correct information within exploit
   1. Correct hostname paramaters, named pipes, or other collected information.
   2. Routine to handle Exploitation process either manual or guided.
3. SQL Injection testing.
   1. By either adding SQLMap directly to the project, or other means.
  4. SQL Database logging of discovered weaknesses/information.
5. Automatic cloaking(through TOR)
    1. Use Stem package for this.
6. Network Pivoting
    1. Add a way to pivot yourself through the network exploring all available options.
7. Bring in AI( oh yea ):
    1. Teach the AI to recognize honeypots and docker containers, and to avoid them at all costs.
    2. Also teach the AI to help with fuzzing to bypass WAF/IDS.

---


### Thanks:

If you enjoy this tool, say thank you to the crew of Freedom45, or, Chef, Root, and Johnny5.

---
