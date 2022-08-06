g++ f.cpp --std=c++11 -o f
./f < f.in > f.out
diff f.out f.ans
python3 f_gen.py | time ./f > /dev/null
