class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # evens = [nums[i] for i in range(len(nums)) if i%2 == 0 ]
        # odds = [nums[i] for i in range(len(nums)) if i%2 == 1 ]

        # evens.sort()
        # odds.sort(reverse = True)

        # result = []
        # even, odd = 0, 0

        # for i in range(len(nums)):
        #     if i%2 == 0:
        #         result.append(evens[even])
        #         even += 1
        #     else:
        #         result.append(odds[odd])
        #         odds += 1

        # return result