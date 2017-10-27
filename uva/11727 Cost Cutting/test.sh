g++ cost.cpp -o cost
./cost < cost.in > cost.out

diff cost.expected.out cost.out