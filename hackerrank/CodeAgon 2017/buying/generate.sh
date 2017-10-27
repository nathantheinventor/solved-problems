for i in {1..100}
do
    python3 generate.py > $i.in
    python3 buying.py < $i.in > $i.out
done