class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low = min(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] + low > target:
                continue
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]

        return ans 