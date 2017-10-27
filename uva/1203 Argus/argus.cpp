#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

struct Type {
    long freq;
    long id;
    long nextOccurrence;
    const bool operator<(const Type t) const {
        if (nextOccurrence != t.nextOccurrence) {
            return nextOccurrence > t.nextOccurrence;
        } else {
            return id > t.id;
        }
    }
};

typedef priority_queue<Type> minHeap;

int main() {
    string x;
    cin >> x;
    minHeap heap;
    while (x == "Register") {
        int id, freq;
        cin >> id >> freq;
        Type* t = new Type();
        t->freq = freq;
        t->id = id;
        t->nextOccurrence = freq;
        cin >> x;
        heap.push(*t);
    }
    int k;
    cin >> k;
    while (k--) {
        Type top = heap.top();
        heap.pop();
        cout << top.id << endl;
        top.nextOccurrence += top.freq;
        heap.push(top);
    }
}