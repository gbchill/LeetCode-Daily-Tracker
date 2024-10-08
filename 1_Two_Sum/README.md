# Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

Assume that each input would have **exactly one solution**, and you may not use the same element twice.

## Difficulty

Easy

## Topic

Array, Hash Map

## Solving Process

Optimal

## Date Solved

October 3, 2024

## Revisit

2

## Notes

- The solution uses a hash map to store the difference between the target and the current number.
- If the difference exists in the hash map, return the indices of the current number and the stored difference.
- Time complexity: O(n)
- Space complexity: O(n)

The time complexity of the solution is O(n) because we iterate through the list of numbers once, and lookups in a hash map take constant time. The space complexity is also O(n) since we store each number and its index in the hash map, which requires additional space proportional to the number of elements in the input list.
