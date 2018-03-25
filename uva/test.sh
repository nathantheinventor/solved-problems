if [ "$1" = "cpp" ]; then
    g++-7 -std=c++11 $2.cpp -o $2
    ./$2 < $2.in > $2.out
    diff $2.out $2.exp
else
    python3 $1.py < $1.in > $1.out
    diff $1.out $1.exp
fi
