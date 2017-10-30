for file in secret/*.in
do
    echo $file
    filename=$(echo $file | grep "[a-z0-9-]*\." -o | grep "[a-z0-9-]*" -o)
    python3 intents.py < secret/$filename.in > secret/$filename.out
    diff secret/$filename.ans secret/$filename.out
done