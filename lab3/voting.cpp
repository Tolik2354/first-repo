#include "voting.h"
#include <iostream>
using namespace std;

void Voting::addCandidate(string name) {
    candidates.push_back(Candidate(name));
}

void Voting::vote(int index) {
    if(index >= 0 && index < candidates.size()) {
        candidates[index].addVote();
    }
}

void Voting::showResults() {
    cout << "Результати голосування:\n";

    for(int i = 0; i < candidates.size(); i++) {
        cout << candidates[i].getName()
             << " - "
             << candidates[i].getVotes()
             << " голосів\n";
    }
}