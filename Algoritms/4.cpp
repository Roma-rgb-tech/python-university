#include <iostream>
#include <string>
std::string removePunctuation(std::string str) {
    if (str.empty()) {
        return "";
    }

    char first = str[0];
    std::string marks = ":;,.-";
    std::string rest = removePunctuation(str.substr(1));


    if (marks.find(first) != std::string::npos) {
        return rest;
    } else { 
        return first + rest;
    }
}


int main() {
    std::string input = "Привіт, ; це - завдання з : рекурсією.";
    std::string result = removePunctuation(input);

    std::cout << "Оригінал: " << input << std::endl;
    std::cout << "Результат: " << result << std::endl;

}




#include <iostream>
int recursiveCompare(const char* s1, const char* s2, int n) {
    if (n <= 0) {
        return 0;
    }

    if (*s1 == '\0' || *s2 == '\0' || *s1 != *s2) {
        return (unsigned char)*s1 - (unsigned char)*s2;
    }


    return recursiveCompare(s1 + 1, s2 + 1, n - 1);
}

int main() {
    const char* str1 = "Hello World";
    const char* str2 = "Hello Ukraine";
    int n = 5;

    int result = recursiveCompare(str1, str2, n);

    if (result == 0) {
        std::cout << "Перші " << n << " символів однакові." << std::endl;
    } else {
        std::cout << "Рядки відрізняються в межах перших " << n << " символів." << std::endl;
    }

}



