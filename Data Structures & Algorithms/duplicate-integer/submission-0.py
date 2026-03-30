class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        duplicates = [x for x in count if count[x]>1]
        if(len(duplicates)==0):
            return False
        return True