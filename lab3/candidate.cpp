#include "candidate.h"

Candidate::Candidate(string n) {
    name = n;
    votes = 0;
}

void Candidate::addVote() {
    votes++;
}

string Candidate::getName() {
    return name;
}

int Candidate::getVotes() {
    return votes;
}