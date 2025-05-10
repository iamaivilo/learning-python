class Solution:
    def twoSum(self, nums, target):
        My_boogers = {}
        for x in range (0,len(nums)):
            if nums[x] in My_boogers: 
                My_boogers[nums[x]].append(x) 
            else:
                My_boogers[nums[x]] = [x]

        for element in nums:
            if target - element == element:
               # the target is 2 time of the element being checked.
               # it will return only when there are two equal numbers in the list/nums
                if len(My_boogers[target - element]) == 2:
                    return My_boogers[target - element]
            elif target - element in My_boogers:
                if len(My_boogers[target - element]) == 1:
                    return[My_boogers[target - element][0],My_boogers[element][0]]
                if len(My_boogers[target - element]) == 2:
                    return My_boogers[target - element]
                if len(My_boogers[target - element]) > 2:
                    return My_boogers[target - element][0:1]


nums = [3,2,4]
print (Solution().twoSum(nums, 6))