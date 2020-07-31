[Problem statement](https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3406/)

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "catsanddog"<br> wordDict = \["cat", "cats", "and", "sand",
"dog"]<br> Output: \[ "cats and dog", "cat sand dog" ] 

Example 2:

Input: s = "pineapplepenapple"<br> wordDict = \["apple", "pen", "applepen",
"pine", "pineapple"]<br> Output: \[
  "pine apple pen apple",   "pineapple pen apple",
  "pine applepen apple" ]<br> Explanation: Note that you are allowed to
reuse a dictionary word. 

Example 3:

Input: s = "catsandog"<br> wordDict = \["cats", "dog", "sand", "and", "cat"]<br>
Output: \[]