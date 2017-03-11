from Main.ps4sub1 import build_coder


def apply_shift(text, shift):
    lib = build_coder(shift)
    tekst = ''
    for i in range(text.__len__()):
        if lib.get(text[i]):
            tekst += lib[text[i]]
        else:
            tekst += text[i]
    return tekst

