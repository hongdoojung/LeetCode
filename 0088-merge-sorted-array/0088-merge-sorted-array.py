class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        for i2, num in enumerate(nums2):
            while True:
                if i1 >= m + i2 or num < nums1[i1]:
                    nums1.insert(i1, num)
                    nums1.pop(-1)
                    break
                else:
                    i1 += 1
    