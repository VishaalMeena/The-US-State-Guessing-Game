#include <iostream>
#include <string>
using namespace std;

// Function to perform XOR
string xorOperation(string dividend, string divisor) {
    string result = "";
    for (int i = 1; i < divisor.length(); i++) {
        result += (dividend[i] == divisor[i]) ? '0' : '1';
    }
    return result;
}

// Function to perform CRC division
string mod2div(string dividend, string divisor) {
    int pick = divisor.length();
    string tmp = dividend.substr(0, pick);

    while (pick < dividend.length()) {
        if (tmp[0] == '1')
            tmp = xorOperation(divisor, tmp) + dividend[pick];
        else
            tmp = xorOperation(string(pick, '0'), tmp) + dividend[pick];
        pick++;
    }
    if (tmp[0] == '1')
        tmp = xorOperation(divisor, tmp);
    else
        tmp = xorOperation(string(pick, '0'), tmp);

    return tmp;
}

int main() {
    string data, divisor;

    cout << "Enter data bits: ";
    cin >> data;
    cout << "Enter divisor (generator polynomial): ";
    cin >> divisor;

    int m = divisor.length();
    string appended_data = data + string(m - 1, '0');

    string remainder = mod2div(appended_data, divisor);
    string codeword = data + remainder;

    cout << "\nRemainder (CRC): " << remainder;
    cout << "\nTransmitted Codeword: " << codeword;

    // Receiver side
    string check = mod2div(codeword, divisor);
    if (check.find('1') != string::npos)
        cout << "\nError detected in received message!\n";
    else
        cout << "\nNo error detected (data is correct).\n";

    return 0;
}
