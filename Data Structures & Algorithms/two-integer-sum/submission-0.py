class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        f_value = {}
        for ind, value in enumerate(nums):

            remain = target - value
            if remain in f_value:
                print(f_value)
                return [f_value[remain],ind]
            f_value[value] = ind
        # return [-1,-1]



        