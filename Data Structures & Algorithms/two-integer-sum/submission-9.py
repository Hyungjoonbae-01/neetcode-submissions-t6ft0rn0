class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            need = target - num
            print(seen)

            if need in seen:
                return [seen[need], i]


            seen[num] = i