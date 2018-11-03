# A. Understand the Problem

'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".


Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

'''

# B. Solve Manually
    # 1. Define a list of letters [a to z]
    # 1a. Define the morse code in a list
    # 2. Loop through the letters and morse code and zip the two lists
    # 3. Return the new dict
    # 4. In a second loop, for each word in the list:
    # 5. For letter in word:
    # 6. if letter in new dict then hold it's value, add to morsecodeword variable
    # 7. if next letter in new dict then hold it's value, add value to morsecodeword variable
    # 8. Return morsecodeword

def uniqueMorseRepresentations(self, words):
    morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--","--.."]
    alphabet = []
    new_word = []
    my_dict = {}

    # Get lowercase alphabet characters and append to alphabet list
    for letter in range(97, 123):
        alphabet.append((chr(letter)))

    # Zip the lists and add to dictionary
    for alpha, code in zip(alphabet, morse_list):
        my_dict[alpha] = code

    for key in words:
        #print("this is key: ", key)
        my_word = " "
        # print("This is first my_word ", my_word)
        for letter in key:
            #print("This is letter: ", letter)
            if letter in my_dict:
                my_word += my_dict.get(letter)
        #print("This is my word ", my_word)
        new_word.append(my_word)
        #print("This is final new_word list: ", new_word)

    distinct_words = set(new_word)
    # print("This is distinct words: ", distinct_words)

    count = len(distinct_words)
    return count



print(uniqueMorseRepresentations(None, ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]))
# "rwjje","aittjje","auyyn","lqtktn","lmjwn"


