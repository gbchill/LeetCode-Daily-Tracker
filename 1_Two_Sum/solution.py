class Solution:
    def twoSum(self, nums, target):
        # Step 1: Create a hashmap to store the numbers we have seen so far.
        hashmap = {}
        
        # Step 2: Iterate through the list `nums` with the help of `enumerate`.
        for index, num in enumerate(nums):
            
            # Step 3: Calculate the difference 
            diff = target - num
            
            # Step 4: Check if the complement exists in the hashmap.
            if diff in hashmap:
                # Step 5: If found, return the indices of both numbers.
                return [hashmap[diff], index]
            
            # Step 6: If not found, store the current number and its index in the hashmap.
            hashmap[num] = index


solution = Solution()


test_nums = [2, 7, 11, 15]
test_target = 9

# Expected result is [0, 1] because 2 + 7 = 9
result = solution.twoSum(test_nums, test_target)
print(result) # Output: [0, 1]
