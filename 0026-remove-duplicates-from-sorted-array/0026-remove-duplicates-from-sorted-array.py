class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        length = len(nums)
        for i in range(1, length):
            if nums[i-x] == nums[i-1-x]:
                nums.pop(i-x)
                x += 1
        return length - x
