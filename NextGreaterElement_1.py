class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        jo={}
        for i in range(len(nums2)):
            if len(stack)!=0 and nums2[i]>stack[-1]:
                jo[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        for num in stack:
            jo[num]=-1
        res=[jo[num] for num in nums1]
        return res
s=Solution()
s.nextGreaterElement([4,1,2],[1,3,4,2])