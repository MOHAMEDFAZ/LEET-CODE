class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        for i in nums:
            if i==0:
                count0+=1
                nums.remove(0)
                nums.append(0)
        
