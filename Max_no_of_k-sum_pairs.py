class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = 0
        d = defaultdict(int)
        for num in nums:
            if d[k-num] > 0:
                pairs += 1
                d[k-num] -= 1
            else:
                d[num] += 1
        return pairs