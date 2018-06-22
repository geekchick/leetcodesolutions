# A. Understand the Problem
'''

You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels. (OUTPUT)

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

# B. Solve the Problem Manually
    # Set count to 0
    # 1. Take "a" from J
    # 2. For each letter in J compare to for each letter in S
    # 2. Check "a" against "a" in S
    # 4. If a is equal to a, then add 1 to count
    # 5. If a not equal to a then continue comparing a in J to characters in S
    # 6. Once the loop is finished, grab the next character in J
    # 7. Take "A" from J
    #    For each letter in J compare to for each letter in S
    # 8. Check "A" against "a" in S
    # 9. if "A" is equal to "a" then add 1 to count
    # 10. if "A" is not equal to "a" then continue comparing "A" in J to characters in S

# C. Optimize the manual solution
    # 1. Loop through each letter in J
    # 2. For each letter in J loop through each letter in S
    # 3. Check letter in J against letter in S
    # 4. If letter in J equal to letter in S, add 1 to count
    # 5. Else, if letter in J not equal to letter in S, keep comparing same J to other in S
    # 6. return count

# D. Pseudocode
        # def numJewelsInStones(self, J, S):
            # count = 0
            # for each letter_J in J:
                # check against for each letter_S in S:
                    # if letter_J == letter_S:
                        # count = count + 1
                    # Else:
                        # continue
            # return count

# E. Code
class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        if J.isalpha() and S.isalpha() and len(J) < 51 and len(S) < 51:
            for letter_J in J:
                for letter_S in S:
                    if letter_J == letter_S:
                        count = count + 1
                    else:
                        continue
        else:
            raise ValueError("Error")

        return count

    print(numJewelsInStones(None, "z", "ZZ"))




