g++ -std=c++11 -O2 agtc.cpp -o agtc
./agtc < agtc.in
time ./agtc < agtc2.in > agtc2.out
diff agtc2.out agtc2.expected
