# Convert any String to Binary and Binary to String

def str2bin(s=None):
    '''
    convert string in Binary
    :param s: String Value
    :return: list of Binary

    ord() for ASCII ( American Standard Code for Information Interchange )
    bin() for Convert ASCII "int" Number to a Binary string prefixed with 0b
    [2:] for split 0b from binary
    .zfill(8) for adding 0 at the beginning to fill up  the gape make it 8 bit
    also we can use .rJust(8,"0") will also work as .zfill(8)
    '''
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bin2str(b=None):
    '''
    Return binary to string
    :param b: list of binary
    :return: convert binary list to string value

    ''.join() method takes all the list in an iterable and joins them into one string
    chr() will returns string representing ASCII Value in to a character
    int(binaryValue, 2) method first will be the binary value and next is the base 2 to convert binary numbers into ASCII Value
    '''
    return ''.join([chr(int(x,2)) for x in b])

#s = "Bangladesh"
s = input("Type anything: ")
s2b = str2bin(s)
b2s = bin2str(s2b)

print(s2b)
print(b2s)