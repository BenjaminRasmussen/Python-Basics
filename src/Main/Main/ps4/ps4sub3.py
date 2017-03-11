from Main.ps4sub1 import build_coder


def apply_coder(text, coder):
    newstring = ''
    for i in range(text.__len__()):
        if coder.get(text[i]):
          newstring = newstring + coder.get(text[i])
        else:
            newstring = newstring + text[i]
    return newstring
