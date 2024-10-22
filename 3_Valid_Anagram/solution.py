class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First, check if the lengths of both strings are the same.
        # If they aren't, it's impossible for them to be anagrams.
        if len(s) != len(t):
            return False  # If lengths differ, return False immediately

        # Initialize two dictionaries to count the frequency of each character
        # countS will hold the counts of characters from string s
        # countT will hold the counts of characters from string t
        countS, countT = {}, {}

        # Loop through both strings using the index (i) to count characters
        # The loop goes over each character in both strings by their indices
        for i in range(len(s)):
            # For string s: count the occurrences of each character
            # If the character exists in countS, increment its count by 1
            # If it doesn't exist, start its count at 1
            countS[s[i]] = 1 + countS.get(s[i], 0)
            
            # For string t: count the occurrences of each character
            # Similar to countS, increment the count in countT for each character
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Now compare the character counts between countS and countT
        # Loop through each character in countS
        for c in countS:
            # If the count of a character in s (countS) is not equal to the count in t (countT)
            # This means the two strings are not anagrams, so return False
            if countS[c] != countT.get(c, 0):  # use .get() to handle missing keys
                return False  # Return False if any character count doesn't match

        # If all character counts match, return True
        # This means the two strings are anagrams
        return True


# Test cases
solution = Solution()

# Test case 1: Expected True
test_s1 = "anagram"
test_t1 = "nagaram"
result1 = solution.isAnagram(test_s1, test_t1)
print(result1)  # Output: True

# Test case 2: Expected False
test_s2 = "rat"
test_t2 = "car"
result2 = solution.isAnagram(test_s2, test_t2)
print(result2)  # Output: False
