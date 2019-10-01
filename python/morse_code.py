class Solution:
    def uniqueMorseRepresentations(self, words) -> int:

        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',            # 26 characters long alphabet
                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",   # 26 characters long morse
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        result = []

        for word in words:
            temp = ""                       # set temp empty after every word
            for char in word:
                index = chars.index(char)   # get an index of character
                temp += morse[index]        # add morse equivalent to the temp

            if temp not in result:          # if temp not in result, add it
                result.append(temp)

        return len(result)                  # return the length
