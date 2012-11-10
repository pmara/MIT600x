# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.

    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if len(aStr) > 1:
        return reverseString(aStr[1:]) + aStr[0]
    else:
        return aStr

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    if len(x) == 0:
        return True
    if len(word) == 0:
        return False

    if x[0] == word[0]:
        return x_ian(x[1:], word[1:])
    else:
        return x_ian(x, word[1:])

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    ### TODO.
    i = findSpaceAfter(text, lineLength - 1)
    if i == None:
        return text

    line = text[:i] + '\n'
    return line + insertNewlines(text[(i + 1):], lineLength)

def findSpaceAfter(text, length):
    if length >= len(text):
        return None
    elif text[length] == ' ':
        return length
    else:
        return findSpaceAfter(text, length + 1)

#def insertNewlinesRec(text, lineLength):
#    if lineLength == 0:
#        if text[0] == ' ':
#            return ''
#        else:
#            return text[0] + insertNewlinesRec(text[1:], lineLength)
#
#    insertNewlines(text[1:],

#print reverseString('hello')

#print x_ian('eric', 'meritocracy')
#print x_ian('john', 'mahjong')
#print x_ian('alvin', 'palavering')
#print x_ian('sarina', 'czarina')

print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
print insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20)
print insertNewlines('Random text to wrap again.', 5)

#print findSpaceAfter('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
