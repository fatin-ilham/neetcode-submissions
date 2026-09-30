class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        dict1 = set(nums)
        longest = 0

        for i in dict1:
            if (i-1) not in dict1:
                length = 1
                while (i+length) in dict1:
                    
                    length += 1
                longest = max(length, longest)
        return longest




        
        