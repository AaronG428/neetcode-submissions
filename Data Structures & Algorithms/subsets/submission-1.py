class Solution:
    '''return powerset of nums tacked onto end of existing'''
    def powerset(self, nums, existing):
        if not nums:
            return [existing]
        else:
            b1 = self.powerset(nums[1:], existing+[nums[0]])
            b2 = self.powerset(nums[1:], existing)
            # print(b1)
            # print(b2)
            # print(b1+b2)
            # print("______")
            return b1+b2



    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all_sets = []
        # for i in range(len(nums)):
        #     n = nums[i]
        all_sets = self.powerset(nums, [])
        return all_sets

