g++ -std=c++11 intprd.cpp -o intprd
./intprd < intprd.in > intprd.out

#diff intprd.expected.out intprd.out
cat intprd.out