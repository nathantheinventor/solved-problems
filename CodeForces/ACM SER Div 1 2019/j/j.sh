#!/bin/bash

g++ -std=c++17 j.cpp -o j
./j < j.1.in > j.1.out && diff j.1.out j.1.ans
./j < j.2.in > j.2.out && diff j.2.out j.2.ans
