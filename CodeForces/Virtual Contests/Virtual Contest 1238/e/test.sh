#!/bin/bash

g++ -O2 -std=c++11 e.cpp -o e

./e < e.1.in
./e < e.2.in
./e < e.3.in
python3 gen.py | time ./e

# for i in 1 2 3 4 5 6 7 8 9 10; do
#     python3 gen.py | python3 e.py
# done
