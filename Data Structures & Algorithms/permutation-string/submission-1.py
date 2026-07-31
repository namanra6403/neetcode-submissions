class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        for r in range(len(s2)):
            var = list(s1)  # treat var as a mutable list (like a bag of chars to remove from)

            i = r
            while i < len(s2) and s2[i] in var:
                var.remove(s2[i])  # remove matched char
                if not var:  # if var is empty, all chars in s1 matched
                    return True
                i += 1

        return False
