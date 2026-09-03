class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)
    
        actual_max = 1

        for num in hashset:
            if (num - 1) not in hashset:
                maxlen = 1
                temp = num + 1
                while temp in hashset:
                    maxlen += 1
                    if maxlen > actual_max:
                        actual_max = maxlen
                    temp += 1


        return actual_max
