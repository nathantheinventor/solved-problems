"""
If anyone looks at this problem when I'm not there tomorrow, this is what I came up with -
it seems to be a basic character replacement encryption. Now I just need to find out
what to do with the numbers. Basically, "xrtp" --> 0, "pmr" --> 1, and so forth.
The "_" means that the letter was not in the input, so we might have to punt on it.
So how do we get "99999" from the numbers "29" and "987"?
-- Sam :)
"""

import re

nums = ['xrtp', 'pmr', 'yep', 'yjtrr', 'gp.t', 'gobr', 'do.', 'drbrm', 'rohjy', 'momr']

for _ in range(int(input())):
    line = input().split()
    for num in line:
        n = -1
        for i, numRe in enumerate(nums):
            if re.match(numRe, num):
                n = i
        assert n > -1