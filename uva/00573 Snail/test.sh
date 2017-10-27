g++ snail.cpp -o snail
./snail < snail.in > snail.out

diff snail.expected.out snail.out