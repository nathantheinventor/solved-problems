#!/bin/bash
python3 test3.py < test.in > test.out && diff test.out test.ex
