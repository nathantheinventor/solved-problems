#!/bin/bash
g++-5 -std=c++11 airports.cpp -o airports
echo "compiled"
./airports < airports.1.in > airports.1.out && diff airports.1.out airports.1.exp
echo "solved 1"
./airports < airports.2.in > airports.2.out && diff airports.2.out airports.2.exp
echo "solved 2"