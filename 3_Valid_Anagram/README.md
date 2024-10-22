# Valid Anagram

## Problem

Given two strings `s` and `t`, determine if `t` is an anagram of `s`.

An **anagram** is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

Return `True` if `t` is an anagram of `s`, otherwise return `False`.

## Difficulty

Easy

## Topic

String, Hash Map

## Solving Process

Optimal

## Date Solved

October 22, 2024

## Revisit

2

## Notes

- The solution uses two hash maps (dictionaries) to count the frequency of each character in both strings.
- If the counts of characters differ between the two strings, we return `False`.
- If the counts match, meaning both strings have the same characters in the same frequencies, we return `True`.
- **Time complexity**: O(n)
- **Space complexity**: O(1)

The time complexity is O(n) because we iterate over both strings, `s` and `t`, which are of length `n`. The space complexity is O(1) because the number of possible characters is constant (e.g., 26 lowercase English letters).
