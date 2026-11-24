class Solution:
    def merge_sort(self,nums):
        if len(nums)<= 1:
            return nums
        mid = len(nums)//2
        left , right = self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:])
        result , i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]

    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = self.merge_sort(nums)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

        