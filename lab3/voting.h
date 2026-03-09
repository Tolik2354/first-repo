#ifndef VOTING_H
#define VOTING_H

#include "candidate.h"
#include <vector>
using namespace std;

class Voting {
private:
    vector<Candidate> candidates;

public:
    void addCandidate(string name);
    void vote(int index);
    void showResults();
};

#endif