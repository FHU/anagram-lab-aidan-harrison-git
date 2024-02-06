#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    if word1.isspace() == True or word2.isspace() ==True:
        return False
    comparison1 = word1.lower()
    comparison2 = word2.lower()
    list1 = comparison1.split()
    list2 = comparison2.split()
    xwhite1 = ''.join(list1)
    xwhite2 = ''.join(list2)
    if len(xwhite1) != len(xwhite2):
        return False
    else:
        for letter in xwhite1:
            if xwhite1.count(letter) == xwhite2.count(letter):
                pass
            else:
                return False

    return True

if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word1 = input()
    word2 = input()
    print(anagram(word1, word2))
    
# test change to see if autograde still skipping