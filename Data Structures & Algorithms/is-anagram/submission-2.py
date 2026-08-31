from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = Counter(s)
        string2 = Counter(t)

        return True if string1 == string2 else False