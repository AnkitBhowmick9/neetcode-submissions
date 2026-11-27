from collections import defaultdict
from typing import List
class Solution:
    def merge_sort(self, strs: List[str]) -> List[str]:
        if len(strs)<= 1:
            return strs
        mid = len(strs)//2
        left, right = self.merge_sort(strs[:mid]), self.merge_sort(strs[mid:])
        result , i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]

        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        group_ana = defaultdict(list)
        for c in strs:
            key = "".join(self.merge_sort(list(c)))
            # print(key,c)
            group_ana[key].append(c)
        return list(group_ana.values())



        