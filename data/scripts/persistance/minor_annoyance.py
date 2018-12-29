import win32api as winapi

try:
    winapi.ClipCursor(1, 1, 1, 1)

except Exception as e:
    print("{}".format(e))