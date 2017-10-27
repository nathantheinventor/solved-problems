#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    char letter;
    string match;
    Node* children[4];
    Node() {
        match = "";
        children[0] = nullptr;
        children[1] = nullptr;
        children[2] = nullptr;
        children[3] = nullptr;
    }
    Node* insert(char c) {
        Node* ans = nullptr;
        switch(c) {
            case 'a':
                ans = (children[0] == nullptr) ? new Node(): children[0];
                children[0] = ans;
                break;
            case 'c':
                ans = (children[1] == nullptr) ? new Node(): children[1];
                children[1] = ans;
                break;
            case 'g':
                ans = (children[2] == nullptr) ? new Node(): children[2];
                children[2] = ans;
                break;
            case 't':
                ans = (children[3] == nullptr) ? new Node(): children[3];
                children[3] = ans;
                break;
        }
        ans->letter = c;
        ans->match = match + c;
        return ans;
    }
    ~Node() {
        if (children[0]) {
            delete children[0];
        }
        if (children[1]) {
            delete children[1];
        }
        if (children[2]) {
            delete children[2];
        }
        if (children[3]) {
            delete children[3];
        }
    }
    Node* get(char c) {
        switch (c) {
            case 'a': return children[0];
            case 'c': return children[1];
            case 'g': return children[2];
            case 't': return children[3];
        }
    }
};

int main() {
    string s1, s2;
    bool dup = false;
    while(cin >> s1 >> s2) {
        if (dup) {
            cout << endl;
        }
        dup = true;
        Node main;
        vector<Node*> nodes;
        for (auto& c: s1) {
            vector<Node*> newNodes;
            newNodes.push_back(main.insert(c));
            for (Node* n: nodes) {
                newNodes.push_back(n->insert(c));
            }
            nodes = newNodes;
        }
        int len = 0;
        vector<string> ans;
        ans.push_back("No common sequence.");
        vector<Node*> matches;
        matches.push_back(&main);
        for (auto& c: s2) {
            vector<Node*> newMatches;
            newMatches.push_back(&main);
            for (Node* n: matches) {
                if (n->get(c) != nullptr) {
                    newMatches.push_back(n->get(c));
                    string tmp = n->get(c)->match;
                    if (tmp.size() > len) {
                        len = tmp.size();
                        ans.clear();
                        ans.push_back(tmp);
                    } else if (tmp.size() == len) {
                        ans.push_back(tmp);
                    }
                }
            }
            matches = newMatches;
        }
        sort(ans.begin(), ans.end());
        string last = "";
        for (string s: ans) {
            if (s != last) {
                cout << s << endl;
            }
            last = s;
        }
    }
}