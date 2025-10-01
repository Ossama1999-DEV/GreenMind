#include <iostream>
#include "version.h"

int main() {
    std::cout << "=== Bienvenue dans GreenMind ===" << std::endl;
    std::cout << "Version : " << GreenMind::getVersion() << std::endl;
    return 0;
}
