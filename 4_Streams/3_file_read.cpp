#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream ifile("test.txt", std::ios::in);
    std::string line;

    if (ifile.is_open()) {
        while (std::getline(ifile, line)) {
            std::cout << line << "\n";
        }
        ifile.close();
    } else {
        std::cerr << "Failed to open file!" << std::endl;
    }

    return 0;
}