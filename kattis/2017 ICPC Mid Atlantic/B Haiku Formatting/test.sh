#!/bin/bash
python3 haiku.py < haiku.1.in > haiku.1.out && diff haiku.1.out haiku.1.exp
python3 haiku.py < haiku.2.in > haiku.2.out && diff haiku.2.out haiku.2.exp
python3 haiku.py < haiku.3.in > haiku.3.out && diff haiku.3.out haiku.3.exp
python3 haiku.py < haiku.4.in > haiku.4.out && diff haiku.4.out haiku.4.exp
