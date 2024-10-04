class Solution:
    def twoSum(self, nums):
        # Step 1: Create a hashset to store the numbers we have seen so far
        hashset = set()
        # Step 2: Iterate through the list nums
        for num in nums: 
            # Step 3: Check if the number already exists in the hashset
            if num in hashset:
                return True
            # Step 4: If not found, add the current number to the hashset
            hashset.add(num)
        return False


solution = Solution()

test_nums1 = [2, 7, 11, 15]
test_nums2 = [2, 7, 11, 15, 2]

# Expected result is False because [2] is not repeated
result1 = solution.twoSum(test_nums1)
# Expected result is True because [2] is repeated
result2 = solution.twoSum(test_nums2)

print(result1)  # Output: False
print(result2)  # Output: True
