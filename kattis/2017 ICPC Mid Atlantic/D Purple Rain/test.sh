#!/bin/bash
python3 rain.py < rain.1.in > rain.1.out && diff rain.1.out rain.1.exp
python3 rain.py < rain.2.in > rain.2.out && diff rain.2.out rain.2.exp
