class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        length = len(nums)
        for i in range(length):
            if nums[i-x] == val:
                del nums[i-x]
                x += 1
        # print(nums, x)
        return length - x
