# for i in range(len(nums)):
        #   for j in range(i+1, len(nums)):
        #     if nums[i] + nums[j] == target:
        #         return (i, j)
class Solution(object):
    def twoSum(self, nums, target):

        nums = [1,2,3,4,5,6]
        target = 10
        hash_map = {}
        for index, number in enumerate(nums):
            complement = target - number
        if complement in hash_map:
            return(hash_map[complement], index)
        hash_map[number] = index
        return False
