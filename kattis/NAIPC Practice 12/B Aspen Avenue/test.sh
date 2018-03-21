g++ -std=c++11 aspen.cpp -o aspen
echo "----"
./aspen < aspen.1.in
echo "----"
./aspen < aspen.2.in
time ./aspen < test.in #> /dev/null 2> /dev/null