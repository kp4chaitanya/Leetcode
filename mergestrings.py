"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        Merge the characters in two strings alternately into a new string.

        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = list(word1)  # Convert word1 to a list of characters
        l2 = list(word2)  # Convert word2 to a list of characters
        l3 = []  # Initialize an empty list to store the merged characters

        i = 0
        while i < len(word1) and i < len(word2):
            # Append characters from both words to the end of l3
            l3.append(word1[i])
            l3.append(word2[i])
            i += 1

        # Append any remaining characters from the longer word to l3
        if i < len(word1):
            l3.extend(word1[i:])
        elif i < len(word2):
            l3.extend(word2[i:])

        return "".join(l3)  # Convert l3 back to a string and return it