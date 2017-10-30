for file in secret/*.in
do
    echo $file
    filename=$(echo $file | grep "[A-Za-z0-9-]*\." -o | grep "[A-Za-z0-9-]*" -o)
    time python3 enclosure.py < secret/$filename.in > secret/$filename.out
    diff secret/$filename.ans secret/$filename.out
done