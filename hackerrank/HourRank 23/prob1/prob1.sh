g++ -std=c++11 prob1.cpp -o prob1
./prob1 < prob1.in > prob1.out
diff prob1.expected.out prob1.out