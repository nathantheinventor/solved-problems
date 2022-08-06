#!/bin/bash
python3 solve.py < $1.in.txt > $1.out.txt
cat $1.out.txt
echo "------"
diff $1.out.txt $1.ans.txt
