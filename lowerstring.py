# A. Understand the Problem
'''
Implement function ToLowerCase() that has a string parameter str
and returns the same string in lowercase.
'''

# B. Solve Problem Manually
    # 1. Take in a string "ZeBRa"
    # 2. Get the first letter "Z", check if it's lower case, if it is make it lower case add to new string
    # 3. Get the second letter "e", check if it's lower case, if it is make it lower case add to new string
    # 4. Get the third letter "B", check if it's lower case, if it is make it lower case add to new string
    # 5. Get the fourth letter "R", check if it's lower case, if it is make it lower case add to new string
    # 6. Get the first letter "a", check if it's lower case, if it is make it lower case add to new string

# C. Optimize the Manual Solution
    # 1. Take in a string
    # 2. Create an empty string
    # 3. Loop through each letter in the string
    # 4. If it's uppercase change letter to lowercase, add to empty string and continue through the loop
    # 5. If it's lowercase, add to empty string and continue through the loop
    # 6. Return new string

# D. Pseudocode
    # def lowerString(str):
        # word = ""
        # for each letter in str:
            # if letter is uppercase:
                # make letter lowercase
                # word += letter
            # else:
                # word += letter
        # str = word
        # return str

# E. Code
class Solution:
    def toLowerCase(self, str):
        word = ""
        for letter in str:
            if letter.isupper():
                word += letter.lower()
            else:
                word += letter
        str = word

        return str

s = Solution()
print(s.toLowerCase("ZeBRa"))