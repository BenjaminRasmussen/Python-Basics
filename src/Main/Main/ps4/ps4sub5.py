from Main.ps4 import is_word, load_words, get_fable_string
from Main.ps4sub3 import apply_coder
from Main.ps4sub4 import apply_shift


wordlist = load_words()
def find_best_shift(wordlist, text):
    poplist=[]
    for i in range(27):
        streng = apply_shift(text, i)
        strengelist = streng.split()
        for j in range(strengelist.__len__()):
            if is_word(wordlist, strengelist[j]):
                #print str(strengelist[j]) + str(j) + " " + str(27-i)
                poplist.append(27-i)
    #making a list cuz then i can gimp this code for later ^^tehee
    return poplist.__getitem__(0)

print find_best_shift(wordlist, apply_shift("hello world", 27))