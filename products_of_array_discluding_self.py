import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = [1]
        right = nums[1:]
        for i in range(len(nums)):
            
            if right == []:
                res.append(math.prod(nums[:-1]))
                return res

            product = math.prod(left) * math.prod(right)
            res.append(product)
            left.append(nums[i])
            right.pop(0)

            print (product)
        return res
            
            


