# create a startup item inside the registry hive, so our program starts on startup.
import win32api as winapi

try: 
	print(winapi.GetCommandLine(" REG ADD HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\Albert"))
	print(winapi.GetCommandLine("REG ADD HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce /v Albert /t REG_MULTI_SZ /f"))
	
