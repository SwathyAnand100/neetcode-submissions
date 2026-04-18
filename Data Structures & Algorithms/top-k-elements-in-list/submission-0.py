class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i]+=1

        sorteddict = dict(sorted(my_dict.items(), key = lambda item: item[1], reverse = True))
        return list(sorteddict.keys())[:k]