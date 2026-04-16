class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = []
        for i,num in enumerate(nums):
            snums.append([num,i])
        snums.sort()
        i = 0
        j = len(nums)-1
        while i<j:
            if snums[i][0] + snums[j][0] == target:
                return [min(snums[i][1],snums[j][1]),max(snums[i][1],snums[j][1])]
            elif snums[i][0] + snums[j][0] > target:
                j = j-1
            else:
                i = i+1
        return[]