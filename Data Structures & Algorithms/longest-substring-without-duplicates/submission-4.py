class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set =set()
        maxLen = 0
        left = 0
        right = 0
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[left])
                left = left + 1
            my_set.add(s[i])
            right+=1
            if maxLen < (right-left):
                maxLen = right -left

        return maxLen


