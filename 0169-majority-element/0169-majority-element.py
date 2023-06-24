class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_dict = {}
        length = len(nums)
        for num in nums:
            before = majority_dict.get(num, 0)
            majority_dict.update({num: before + 1})
            if before + 1 > length/2:
                break
        return num
    