#include <iostream>
#include <string>
#include <limits>
#include <sstream>
#include "./string_calculator.h"

using std::cout, std::endl, std::cin;
using std::string;

int main() {
    // TODO(student): implement the UI
    cout << "String Calculator" << endl;
    cout << "\"q\" or \"quit\" or ctrl+d to exit" << endl;

    string num1;
    string sign;
    string num2;
    do {
        cout << ">> ";
        cin >> num1;

        if (num1 == "q" || num1 == "quit") {
            cout << endl;
            cout << "farvel!" << endl;
            cout << endl;
            return 0;
        }
        cin >> sign >> num2;

        cout << endl;

        if (sign == "+") {
            cout << "ans =" << endl;
            cout << endl;
            cout << "    " << add(num1, num2) << endl;
            cout << endl;
            num1  = "";
            num2 = "";
        }

        if (sign == "*") {
            cout << "ans =" << endl;
            cout << endl;
            cout << "    " << multiply(num1, num2) << endl;
            cout << endl;
            num1 = "";
            num2 = "";
        }



    } while (num1 != "q" || num1 != "quit");

}




