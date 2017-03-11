def build_coder(shift):
    alphabet =[' ', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','v','W','X','Y','Z']

    alpha    = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    shifted = dict()
    for i in range(alphabet.__len__()):
        if i+shift < alphabet.__len__():
            shifted[alphabet[i]]=alphabet[i+shift]
        else:

            newvalue = (i+shift)%(alphabet.__len__())
            shifted[alphabet[i]]=alphabet[newvalue]

    for i in range(alpha.__len__()):
        if i+shift < alpha.__len__():
            shifted[alpha[i]]=alpha[i+shift]
        else:
            nv = (i+shift)%(alpha.__len__())
            shifted[alpha[i]]=alpha[nv]
    return shifted
 #{' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
 #'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
 #'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
 #'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
 #'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
 #'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
 #'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
 #'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}

 #{' ': 'C', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
 #'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
 #'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'v', 'R': 'U', 'U': 'X',
 #'T': 'W', 'W': 'Z', 'Y': 'b', 'X': 'a', 'Z': 'c', 'a': 'd', 'c': 'f',
 #'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k',
 #'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't',
 #'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y',
