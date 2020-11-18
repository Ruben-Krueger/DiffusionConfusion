
def evaulate(arterial_blood, tissue, venous_blood, iters):

    a, t, v = [], [], []

    for i in range(iters):
        arterial_blood.update(1) 
        tissue.update(1)
        venous_blood.update(1)

        a += [arterial_blood.c]
        t += [tissue.c]
        v += [venous_blood.c]
