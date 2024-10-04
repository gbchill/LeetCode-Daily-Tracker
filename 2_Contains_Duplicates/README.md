# Contains Duplicates

## Problem

Given an array of integers nums, determine if any integer is repeated within the list.

Return True if any number appears at least twice in the list, otherwise return False.

## Difficulty

Easy

## Topic

Array, Hash Set

## Solving Process

Optimal

## Date Solved

October 4, 2024

## Revisit

No revisit.

## Notes

- The solution uses a hashset to store each number we encounter while iterating through the list.
- If a number is found in the hashset, it indicates that the number has already appeared, so we return True.
- If no duplicates are found by the end of the iteration, we return False.
- Time complexity: O(n)
- Space complexity: O(n)

The time complexity of the solution is O(n) because we iterate through the list of numbers once, and lookups in a hashset take constant time. The space complexity is also O(n) since we store each unique number in the hashset, requiring space proportional to the number of elements in the input list.


