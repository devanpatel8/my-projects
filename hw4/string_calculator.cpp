#include <iostream>
#include <string>
#include "./string_calculator.h"

using std::cout, std::endl;
using std::string;
using namespace std;

unsigned int digit_to_decimal(char digit) {
    // TODO(student): implement
    if (digit >= '0' && digit <= '9') {
        return (digit - '0');
    }
    else {
        throw std::invalid_argument("Invalid Argument");
    }
}

char decimal_to_digit(unsigned int decimal) {
    // TODO(student): implement
    if (decimal <= 9) {
        return ('0' + decimal);
    }
    else {
        throw std::invalid_argument("Invalid Argument"); 
    }
}

string trim_leading_zeros(string num) {
    // TODO(student): implement
    if (num.at(0) == '-') {
        num = num.erase(0,1);
        while (num.at(0) == '0' && num.length() > 1) {
            num = num.erase(0,1);
        }
        if (num == "0") {
            return num;
        }
        return "-" + num;
    }
    else {
        while (num.at(0) == '0' && num.length() > 1) {
            num = num.erase(0,1);
    }
        return num;
    }
}

string add(string lhs, string rhs) {
    // TODO(student): implement
    bool isNegative = false;
    if (lhs.at(0) == '-' && rhs.at(0) == '-') {
        isNegative = true;
        lhs = lhs.erase(0,1); //remove negative 
        rhs = rhs.erase(0,1);
    }

    //trim zeros
    if (lhs.at(0) == '0' || rhs.at(0) == '0') {
        lhs = trim_leading_zeros(lhs);
        rhs = trim_leading_zeros(rhs);
    }

    //always give lhs shorter number
    if(lhs.length() > rhs.length()) {
        swap(lhs, rhs); 
    }

    //initialize useful variables
    int lhsLength = lhs.length();
    int rhsLength = rhs.length();
    int extraDigits = rhsLength - lhsLength;
    int lhsLastIndex = lhs.length() - 1;
    int carry = 0;
    int intSum;
    string strSum;

    
    
    for (int i = lhsLastIndex; i >= 0; --i) {
        intSum = digit_to_decimal(lhs.at(i)) + digit_to_decimal(rhs.at(i + extraDigits)) + carry; //add last decimal of each digit plus digit
        strSum.push_back(decimal_to_digit(intSum%10)); //if sum is greater than 10, take remainder and carry to next addition
        carry = intSum/10; //get carry
    }
    //repeat for extra digits
    for (int i = extraDigits - 1; i >= 0; --i) {
        intSum = digit_to_decimal(rhs.at(i)) + carry;
        strSum.push_back(decimal_to_digit(intSum%10));
        carry = intSum/10;
    }
    //add whatever is left
    if (carry) {
        strSum.push_back(decimal_to_digit(carry));
    }

    string finalSum;
    for(int i = strSum.length()-1; i>=0; i--) { //reverse method
        finalSum = finalSum + strSum[i];  
    }

    if (isNegative == true) {
        return '-' + finalSum;
    }
    else {
        return finalSum;
    }

}



string multiply(string lhs, string rhs) {
    // TODO(student): implement

    if (lhs == "0" || rhs == "0") { //0x0
      return "0";
    }
    /*if (lhs != "0" && trim_leading_zeros(rhs) == "1") { //multiply by 1
        return trim_leading_zeros(lhs);
    }*/

    bool isNegative = false;
    if (lhs.at(0) == '-' && rhs.at(0) == '-') {
        isNegative = false;
        lhs = lhs.erase(0,1); //remove negative 
        rhs = rhs.erase(0,1);
    } else {
        if (lhs.at(0) == '-') {
            lhs = lhs.erase(0,1);
            isNegative = true;
        }   
        if (rhs.at(0) == '-') {
            rhs = rhs.erase(0,1);
            isNegative = true;
        }
    }



    if (lhs.at(0) == '0' || rhs.at(0) == '0') { //trim leading zeros
        lhs = trim_leading_zeros(lhs);
        rhs = trim_leading_zeros(rhs);
    }

    //initialize useful variables
    int lhsLastIndex = lhs.length() - 1;
    int rhsLastIndex = rhs.length() - 1;
    string strProduct(lhs.size() + rhs.size(), 0); //initialize string with set limit 
    int intResult;


    for (int i = lhsLastIndex; i >= 0; --i) { //iterate through lhs first for all rhs digits
        for (int j = rhsLastIndex; j >= 0; --j) {
            intResult = (digit_to_decimal(lhs.at(i)) * digit_to_decimal(rhs.at(j))) + strProduct[i + j + 1];
            strProduct[i + j + 1] = intResult % 10;
            strProduct[i + j] += intResult / 10;
        }
    }

    int strProductLength = strProduct.size();
    for (int i = 0; i < strProductLength; i++) {
        strProduct[i] += '0';
    }
    if (strProduct[0] == '0') {
        strProduct = strProduct.substr(1);
    }

    string final_string = "-" + strProduct;

    if (isNegative == true) {
        return final_string;
    }

return strProduct;
}


