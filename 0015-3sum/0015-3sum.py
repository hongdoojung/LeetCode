class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        num_dict = {}
        
        for i, num in enumerate(nums):
            num_dict[num] = i
        length = i + 1
        
        for i in range(length-2):
            part_sum = nums[i]
                
            for j in range(i+1, length-1):
                part_sum = nums[i] + nums[j]
                if -1 * part_sum in num_dict and not num_dict[-1 * part_sum] in (i,j):
                    part = [nums[i], nums[j], -1 * part_sum]
                    part.sort()
                    answer.add(tuple(part))
                    
        return list(answer)
