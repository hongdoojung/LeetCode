class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        div_k = k % length
        nums[:] = nums[length-div_k:] + nums[:length-div_k]
