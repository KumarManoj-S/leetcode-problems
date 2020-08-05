## Add and Search Word - Data Structure Design

[Problem statement](https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3413/)


Design a data structure that supports the following two operations: 


```
void addWord(word) 
bool search(word) 
```

search(word) can search a literal word or a regular expression string
containing only letters `a-z` or `.` <br>A `.` means it can represent
any one letter.

**Example:**

``` 
addWord("bad") 
addWord("dad") 
addWord("mad") 
search("pad") -> false
search("bad") -> true 
search(".ad") -> true 
search("b..") -> true 
```

**Note**: You may assume that all words are consist of lowercase letters
`a-z`.