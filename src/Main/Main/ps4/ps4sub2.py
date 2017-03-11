def build_decoder(shift):
    uppercase =[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','v','W','X','Y','Z']
    lowercase =[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decodelib = dict()

    for i in range(uppercase.__len__()):
        if i-shift < 0:
            newshift=uppercase.__len__()-(shift-i)
            decodelib[uppercase[i]]=uppercase[newshift]
        else:
            decodelib[uppercase[i]]=uppercase[i-shift]

    for j in range(lowercase.__len__()):
        if j-shift < 0:
            ns=lowercase.__len__()-(shift-j)
            decodelib[lowercase[j]]=lowercase[ns]
        else:
            decodelib[lowercase[j]]=lowercase[j-shift]

    return decodelib
print (build_decoder(3))


 #{' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
 #'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
 #'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
 #'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
 #'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
 #'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
 #'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
 #'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}


 #{' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
 #'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
 #'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
 #'T': 'Q', 'W': 'T', 'Y': 'v', 'X': 'U', 'Z': 'W', 'a': 'w', 'c': ' ',
 #'b': 'v', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f', 'h': 'e',
 #'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k', 'q': 'n',
 #'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't', 'v': 's',
 #'y': 'v', 'x': 'u', 'z': 'w'}
