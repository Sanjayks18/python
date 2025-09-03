class Solution(object):
    def majorityElement(self, nums):
       
        n=len(nums)
        freq={}
        for elem in nums:
            freq[elem]=freq.get(elem,0)+1
        for key,val in freq.items():
            if val > (n//2):
                return key
obj = Solution()

nums = [2, 2, 3, 4, 2, 5, 2, 2, 6]
print(obj.majorityElement(nums))