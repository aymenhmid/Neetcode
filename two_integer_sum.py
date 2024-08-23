class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            x = target - nums[i]
            indexes = [index for index, value in enumerate(nums) if value == x and index != i]
            if len(indexes) == 1:
                return [min(i,indexes[0]),max(i,indexes[0])]
#using hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        
