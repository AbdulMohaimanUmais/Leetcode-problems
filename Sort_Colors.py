class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
# 1. Two pointers Approach       
        
        # zero, two = 0, len(nums) - 1

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[i], nums[zero] = nums[zero], nums[i]
        #         zero +=1
        
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] == 2:
        #         nums[i], nums[two] = nums[two], nums[i]
        #         two -=1


# 2. Three Pointers Approach        

        low, mid, high = 0, 0, len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low +=1
                mid +=1

            elif nums[mid] == 1:
                mid +=1
            
            else: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1
