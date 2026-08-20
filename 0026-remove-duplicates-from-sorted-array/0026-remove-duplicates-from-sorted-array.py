class Solution(object):
    def removeDuplicates(self, nums):
        new_num = []
        for x in nums:
            if x not in new_num:
                new_num.append(x)
        
        for i in range(len(new_num)):
            nums[i] = new_num[i]

        return len(new_num)
        