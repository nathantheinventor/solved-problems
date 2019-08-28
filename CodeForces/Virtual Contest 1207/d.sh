echo "TEST CASE 1:"
python3 d.py < d.1.in > d.1.out && diff d.1.out d.1.ans

echo "TEST CASE 2:"
python3 d.py < d.2.in > d.2.out && diff d.2.out d.2.ans

echo "TEST CASE 3:"
python3 d.py < d.3.in > d.3.out && diff d.3.out d.3.ans
