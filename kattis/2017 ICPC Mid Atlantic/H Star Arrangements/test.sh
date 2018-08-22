#!/bin/bash
python3 star.py < star.1.in > star.1.out && diff star.1.out star.1.exp
python3 star.py < star.2.in > star.2.out && diff star.2.out star.2.exp
python3 star.py < star.3.in > star.3.out && diff star.3.out star.3.exp
