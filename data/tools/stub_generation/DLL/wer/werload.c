
#define UNICODE
#include <windows.h>
#include <werapi.h>
#include <shlwapi.h>
#pragma comment(lib, "shlwapi.lib")

#include <stdio.h>

int main(void) {
    HRESULT hr;
    WCHAR   path[MAX_PATH];
    
    GetModuleFileName (NULL, path, MAX_PATH);
    PathRemoveFileSpec(path);
    PathAppend(path, L"wermodule.dll");
    hr = WerRegisterRuntimeExceptionModule(path, NULL);
    
    RaiseException (0xABCD1234, EXCEPTION_NONCONTINUABLE, 0, NULL);
    
    WerUnregisterRuntimeExceptionModule(path, NULL);
    return 0;
}
