PART A: HAIL CAESAR!
====================

Encryption is the process of obscuring information to make it unreadable without special knowledge. For centuries, people have devised schemes to encrypt messages - some better than others - but the advent of the computer and the Internet revolutionized the field. These days, it's hard not to encounter some sort of encryption, whether you are buying something online or logging into a shared computer system. Encryption lets you share information with other trusted people, without fear of disclosure.

A cipher is an algorithm for performing encryption (and the reverse, decryption). The original information is called plaintext. After it is encrypted, it is called ciphertext. The ciphertext message contains all the information of the plaintext message, but it is not in a format readable by a human or computer without the proper mechanism to decrypt it; it should resemble random gibberish to those for whom it is not intended.

A cipher usually depends on a piece of auxiliary information, called a key. The key is incorporated into the encryption process; the same plaintext encrypted with two different keys should have two different ciphertexts. Without the key, it should be difficult to decrypt the resulting ciphertext into readable plaintext.

This assignment will deal with a well-known (though not very secure) encryption method called the Caesar cipher. In this problem set you will need to devise your own algorithms and will practice using recursion to solve a non-trivial problem.

CAESAR CIPHER
-------------

The basic idea of the Caesar cipher is that you pick an integer for a key, and shift every letter of your message by the key. For example, if your message was "hello" and your key was 2, "h" becomes "j", "e" becomes "g", and so on, because we are shifting every letter two spots to the right. Note we are using the English alphabet for this problem - that is, the following letters in the following order:

    >>> import string
    >>> print string.ascii_lowercase
    abcdefghijklmnopqrstuvwxyz

If you're interested in learning more about the Caesar cipher, check out this Wikipedia article.

We will use a variant of the standard Caesar cipher where we will treat upper and lower case letters separately, so upper case letters will always be mapped to upper case letters, and lower case letters will always be mapped to lower case letters. Thus, if "a" maps to "c", "A" will map to "C". Characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the space (' ') and all numerical characters (0 - 9).

WRAPPER FUNCTIONS
-----------------

Now that you are ready to start coding, you can look carefully at the code skeletons that we have provided for you. Do not be intimidated by the length of the function specifications we provide with the supplied code! Many of these problems rely on wrapper functions, an extremely useful coding concept that, when implemented correctly, often requires very little additional code. The idea of wrapper functions here is that the functions visible to a user take as arguments simple inputs, and then supply these arguments - plus other information - to functions visible only within the implementation to perform the computation.

Read the Wikipedia article on wrapper functions for more information.

Hints
-----

Upper and Lower Case Letters

Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".
If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:

    >>> import string
    >>> print string.ascii_lowercase
    abcdefghijklmnopqrstuvwxyz
    >>> print string.ascii_uppercase
    ABCDEFGHIJKLMNOPQRSTUVWXYZ

Characters to Ignore

A reminder from the introduction page - Characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the space (' ') and all numerical characters (0 - 9).

Test Cases
----------

    buildCoder(3)
    {'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
    buildCoder(9)
    {'A': 'J', 'C': 'L', 'B': 'K', 'E': 'N', 'D': 'M', 'G': 'P', 'F': 'O', 'I': 'R', 'H': 'Q', 'K': 'T', 'J': 'S', 'M': 'V', 'L': 'U', 'O': 'X', 'N': 'W', 'Q': 'Z', 'P': 'Y', 'S': 'B', 'R': 'A', 'U': 'D', 'T': 'C', 'W': 'F', 'V': 'E', 'Y': 'H', 'X': 'G', 'Z': 'I', 'a': 'j', 'c': 'l', 'b': 'k', 'e': 'n', 'd': 'm', 'g': 'p', 'f': 'o', 'i': 'r', 'h': 'q', 'k': 't', 'j': 's', 'm': 'v', 'l': 'u', 'o': 'x', 'n': 'w', 'q': 'z', 'p': 'y', 's': 'b', 'r': 'a', 'u': 'd', 't': 'c', 'w': 'f', 'v': 'e', 'y': 'h', 'x': 'g', 'z': 'i'}

    >>> applyCoder("Hello, world!", buildCoder(3))
    'Khoor, zruog!'
    >>> applyCoder("Khoor, zruog!", buildCoder(23))
    'Hello, world!'

    >>> applyShift('This is a test.', 8)
    'Bpqa qa i bmab.'
    >>> applyShift('Bpqa qa i bmab.', 18)
    'This is a test.'
