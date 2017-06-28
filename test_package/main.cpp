#include "utf8/utf8.h"
#include <iostream>
#include <string>
#include <vector>

int main()
{
  std::cout << "\n===== BEGIN TestPackage =====\n";

  std::string myString{"a regular string"};
  std::vector<unsigned short> utf16Vec{};
  utf8::utf8to16(myString.begin(), myString.end(), std::back_inserter(utf16Vec));

#ifndef NDEBUG
    std::cout << "Build Type: DEBUG\n";
#else
    std::cout << "Build Type: RELEASE\n";
#endif

    std::cout << "====== END TestPackage ======\n";
    return 0;
}
