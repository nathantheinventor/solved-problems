#!/bin/bash
g++-5 -std=c++11 solve.cpp -o solve
echo "Compiled"
./solve < test.in > test.out
diff test.out test.exp