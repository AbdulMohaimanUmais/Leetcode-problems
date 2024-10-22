class Solution(object):
    def containsDuplicate(self, nums):

    # 1. Bruteforce Technique

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False     


# 2. Sort Method

        # nums.sort()
        # for num in range(len(nums)-1):
        #     if nums[num] == nums[num+1]:
        #         return True
        # return False     


# 3. Hash_Map Method

        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         return True
        #     hashmap[num] = 1
        # return False

# 4. Set Method

        number = set()
        for num in nums:
            if num in number:
                return True
            number.add(num)
        return False