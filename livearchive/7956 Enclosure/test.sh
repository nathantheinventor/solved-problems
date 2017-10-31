g++ -std=c++11 enclosure.cpp -o enclosure

for file in secret/*.in
do
    echo $file
    filename=$(echo $file | grep "[A-Za-z0-9-]*\." -o | grep "[A-Za-z0-9-]*" -o)
    ./enclosure < secret/$filename.in > secret/$filename.out
    diff secret/$filename.ans secret/$filename.out
done