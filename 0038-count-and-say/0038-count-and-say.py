from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        def rle_encoding(iterable_s):
            return "".join(
        f"{len(tuple(g))}{k}" 
        for k, g in groupby(iterable_s)
            )
        
        def count(k):
            if k == 1:
                return "1"
            
            else:
                prev = count(k-1)
                return rle_encoding(prev)
            
        return count(n)

