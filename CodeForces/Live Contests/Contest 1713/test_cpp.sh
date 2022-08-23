#!/bin/bash
g++ solve.cpp -O3 -obanana
./banana < $1.in.txt > $1.out.txt
cat $1.out.txt
echo "------"
diff $1.out.txt $1.ans.txt
