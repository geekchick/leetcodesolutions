'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
    def twoSumTarget(self, nums, target):
        for index, item in enumerate(nums):
            print(index, item)
            if item <= target or item >= target:
                print("This is item: ", item)
                remainder = target - item
                print("This is remainder: ", remainder)
                item_index = index
                print("This is item_index: ", item_index)
                if remainder in nums[item_index + 1:]:
                    remainder_index = nums.index(remainder, item_index + 1, len(nums))

                    print("This is remainder index:" ,remainder_index)
                    print("True")
                    retur n(item_index ,remainder_index)
                else:
                    print("This is the FIRST ELSE")
                    continue

            else:
                print("This is the SECOND ELSE")
                continue



    def twoSumEnum(self, nums, target):

        for i, a_item in enumerate(nums):
            print("This is i: ", i)
            print(i, a_item)
            for j, b_item in enumerate(nums[i + 1:]):
                print("This is j")
                print(i + 1, b_item)
                sum = a_item + b_item
                print("This is the sum: ", sum)
                if sum == target:
                    print("yes")
                    retur n(i)
                else:
                    i = i + 1
                    j = i + 1
                    continue






        def twoSum(self, nums, target):
            for a_item in nums:
                print("This is a_item: ", a_item)
                i_index = nums.index(a_item)
                print("This is i_index: ", i_index)
                for b_item in nums[i_index + 1:]:
                    print("This is b_item: ", b_item)
                    if len(nums) == 2:
                        j_index_before = nums.index(b_item)
                        j_index = j_index_before + 1
                    elif len(nums) > 2:
                        j_index = nums.index(b_item)
                    print("This is j_index: ", j_index)
                    sum = a_item + b_item
                    print("This is the sum: ", sum)
                    if sum == target:
                        print("The sum equal the target: ", sum)
                        return (i_index, j_index)
                    else:
                        print("The sum does NOT equal the target")
                        continue



s = Solution()
# print(s.twoSumTarget([0,4,3,0], 0))
print(s.twoSumTarget([-1 ,-2 ,-3 ,-4 ,-5] ,-8))
# print(s.twoSumTarget([3, 10, 4, 3], 6))
# print(s.twoSumTarget([2, 7, 11, 15], 9))
# print(s.twoSumTarget([3, 3], 6))
# print(s.twoSumTarget([3, 4, 3], 6))
# print(s.twoSum([2, 7, 11, 15], 26))
# print(s.twoSumEnum([3, 4, 3], 6))