from Main.ps4sub4 import apply_shift


def apply_shifts(text, shifts):

    pivots = list()
    shiftlist = list()
    newstring = ''
    for i in range(shifts.__len__()):
        if shifts.__getitem__(i):
            pivots.append(shifts.__getitem__(i).__getitem__(0))
            shiftlist.append(shifts.__getitem__(i).__getitem__(1))
        print "pivots: " + str(pivots)
        print "shifts: " + str(shiftlist)

    for j in range(pivots.__len__()):
        apply_shift(text, shiftlist.__getitem__(j))
        print text




apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18),(12, 16)])