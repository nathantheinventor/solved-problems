g++ -std=c++11 e.cpp -o e
# ./e < e.in
./e < e.in > e.out
diff e.out e.ans