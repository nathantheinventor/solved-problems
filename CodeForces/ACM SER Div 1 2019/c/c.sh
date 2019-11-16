#!/bin/bash

g++ -std=c++11 c.cpp -o c
time ./c < c.in > c.out && diff c.out c.ans
time ./c < secret1.in > secret1.out && diff secret1.out secret1.ans
time ./c < secret2.in > secret2.out && diff secret2.out secret2.ans
time ./c < secret3.in > secret3.out && diff secret3.out secret3.ans
time ./c < secret4.in > secret4.out && diff secret4.out secret4.ans
time ./c < secret5.in > secret5.out && diff secret5.out secret5.ans
time ./c < secret6.in > secret6.out && diff secret6.out secret6.ans
time ./c < secret7.in > secret7.out && diff secret7.out secret7.ans
time ./c < secret8.in > secret8.out && diff secret8.out secret8.ans
