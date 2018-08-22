#!/bin/bash
g++-5 -std=c++11 badge.cpp -o badge
./badge < badge.1.in > badge.1.out && diff badge.1.out badge.1.exp
./badge < badge.2.in > badge.2.out && diff badge.2.out badge.2.exp
./badge <    big1001.in >    big1001.out && diff    big1001.out    big1001.ans
./badge <    big1002.in >    big1002.out && diff    big1002.out    big1002.ans
./badge <    big1003.in >    big1003.out && diff    big1003.out    big1003.ans
./badge <      comb5.in >      comb5.out && diff      comb5.out      comb5.ans
./badge <      comb6.in >      comb6.out && diff      comb6.out      comb6.ans
./badge <   comb1000.in >   comb1000.out && diff   comb1000.out   comb1000.ans
./badge <  combs1000.in >  combs1000.out && diff  combs1000.out  combs1000.ans
./badge <   line1000.in >   line1000.out && diff   line1000.out   line1000.ans
./badge <      loop6.in >      loop6.out && diff      loop6.out      loop6.ans
./badge <    loop100.in >    loop100.out && diff    loop100.out    loop100.ans
./badge <   loop1000.in >   loop1000.out && diff   loop1000.out   loop1000.ans
./badge < random1000.in > random1000.out && diff random1000.out random1000.ans
./badge < random1001.in > random1001.out && diff random1001.out random1001.ans
./badge < random1002.in > random1002.out && diff random1002.out random1002.ans
