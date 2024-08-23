class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        if len(list(set(nums))) != len(nums):
            return True
        return False
#2nd approach
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
