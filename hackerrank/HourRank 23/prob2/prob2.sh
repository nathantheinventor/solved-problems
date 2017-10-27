g++ -std=c++11 prob2.cpp -o prob2
./prob2 < prob2.in > prob2.out
diff prob2.expected.out prob2.out