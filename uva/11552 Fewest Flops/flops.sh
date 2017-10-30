g++ -std=c++11 -O2 flops.cpp -o flops
time ./flops < flops.in
time ./flops < flops2.in > flops2.out
diff flops2.out flops2.expected
