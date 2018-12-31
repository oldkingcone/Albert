# create a startup item inside the registry hive, so our program starts on startup.
import win32api as winapi

try: 
	print(winapi.GetCommandLine(" REG ADD HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\toteslegit"))
	print(winapi.GetCommandLine("REG ADD HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce /v toteslegit /t REG_DWORD_LITTLE_EDIAN /f"))
	