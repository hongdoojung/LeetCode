class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        duplicated = 0
        length = len(nums)
        for i in range(1, length):
            if nums[i-x] == nums[i-1-x]:
                duplicated += 1
                if duplicated >= 2:
                    del nums[i-x]
                    x += 1
            else:
                duplicated = 0
        return length - x
