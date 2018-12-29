import win32api as winapi
import psutil
# import stem find a usage for this later.

try:
    print(winapi.GetComputerName())
    print(winapi.GetDomainName())
    print(winapi.GetLastInputInfo())
    print(psutil.disk_partitions())
    print(psutil.disk_usage("/"))
    print(psutil.disk_io_counters())
    PROC_NAMES = ["Taskmgr.exe", "browser_broker.exe", "firefox.exe", "chrome.exe"]
    for item in PROC_NAMES:
        for proc in psutil.process_iter():
            if proc.name() == item:
                prox = set()
                prox.add(str(proc))
                for item in prox:
                    print(item)
    for item in PROC_NAMES:
        print(winapi.FindExecutable(item))
except Exception as e:
    print("something broke.....\n{}".format(e))