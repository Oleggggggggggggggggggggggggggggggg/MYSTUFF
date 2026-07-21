#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "C++ setup is working!\n";
    cin >> num;
    cout << "Hello My Friend!\n";
    cout << num << endl;
    if (num > 10) {
        cout << "Your number is greater than 10\n";
    } else if (num == 10) {
        cout << "Your number is equal to 10\n";
    } else {
        cout << "Your number is less than 10\n";
    }
    return 0;
}