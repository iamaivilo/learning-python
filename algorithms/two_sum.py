class Solution:
    def twoSum(self, nums, target):
        snums = nums.copy()
        snums.sort()
        x = 0
        y = len(nums) - 1
        while x < y:
            if snums[x] + snums[y] >target:
                y -= 1
            elif snums[x] + snums[y] <target:
                x += 1
            elif snums[x] + snums[y] == target:
                found_x = find_index(nums, snums[x])
                found_y = find_index_from_the_end(nums, snums[y])
                return [found_x, found_y]

def find_index(nums, element):
    length = len(nums)
    for x in range(0, length):
        if nums[x] == element:
            return x

def find_index_from_the_end(nums, element):
    length = len(nums)
    for x in range(0,length):
        y = length - 1 - x
        if nums[y] == element:
            return y

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))