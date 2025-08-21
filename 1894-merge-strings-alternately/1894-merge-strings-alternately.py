class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        #taking the range till when the loop will run
        w1 = len(word1)
        w2 = len(word2)


        #intitating the pointers for each of the words
        p1 = 0
        p2 = 0

        new_word=[]

        #declaring which word it is currently at
        word = 1

        while p1<w1 and p2<w2:
            if word == 1:
                new_word.append(word1[p1])
                p1+= 1
                word = 2
            else:
                new_word.append(word2[p2])
                p2+= 1
                word = 1
        # now once depleted, the rest will be appended
        while p1<w1:
            new_word.append(word1[p1])
            p1+= 1 
        
        while p2<w2:
            new_word.append(word2[p2])
            p2+= 1 

        return ''.join(new_word)
            