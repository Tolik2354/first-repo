#include <iostream>
#include <windows.h>
#include "Voting.h"

using namespace std;

int main() {

    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    Voting voting;

    voting.addCandidate("Іван");
    voting.addCandidate("Петро");
    voting.addCandidate("Ольга");

    voting.vote(0);
    voting.vote(1);
    voting.vote(0);
    voting.vote(2);
    voting.vote(0);

    voting.showResults();

    return 0;
}