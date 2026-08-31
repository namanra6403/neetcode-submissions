from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        var = Counter(nums)

        count = defaultdict(list)

        for num, freq in var.items():
            count[freq].append(num)

        res = []

        for i in range(len(nums), 0, -1):
            for num in count[i]:# ← loop through each number in bucket!
                res.append(num)
                if len(res) == k:
                    return res