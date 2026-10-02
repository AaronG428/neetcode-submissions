class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        n = 2**k
        all_sets = []
        for i in range(n):
            current_set = []
            for j in range(k):
                e = nums[j]
                # print("i:",j)
                # print("idx:",0b1<<j)
                if i&(0b1<<j):
                    current_set.append(e)
            
            all_sets.append(current_set)
        return all_sets