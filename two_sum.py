class Solution(object):
    def twoSum(self, nums, target):
 
        mpp = {} 

        for i, num in enumerate(nums): 
            needed = target - num
            if needed in mpp:
                return [mpp[needed], i]  
            mpp[num] = i

        return []

if __name__ == "__main__":
    arr = [2, 6, 5, 8, 11]
    target = 14

    obj = Solution()
    ans = obj.twoSum(arr, target)
    print("Indices of two numbers:", ans)

    if ans: 
        print("Numbers are:", arr[ans[0]], "and", arr[ans[1]])
