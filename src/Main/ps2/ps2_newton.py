def evaluate_poly(poly, x):
    resultat = 0
    res = ""
    for i in range(poly.__len__()):
        res += str(poly[i]) + "x^" + str(i) + " + "
        if i == 1:
            resultat = resultat + (poly[i] * x)
        else:
            resultat += poly[i] * (x ** i)
        res += " *" + str(x)
        res.join(",")
   # print(res[:-3])
    return resultat


def compute_deriv(poly):
    deriv = []
    if len(poly) < 2:
        return [0, 0]
    for a in range(1, len(poly)):
        deriv.append(float(a * poly[a]))
    return deriv


def computeroot(poly, x_0, epsilon):
    roots = []
    if abs(evaluate_poly(poly, x_0)) < epsilon:
        roots = x_0
    else:
        computeroot(poly, (x_0 - (evaluate_poly(poly, x_0)) / evaluate_poly(compute_deriv(poly), x_0)), epsilon)
    print("roots = " + str(roots))

computeroot((0.0, 0.0, 5.0, 9.3, 7.0), 2, 0.0001)
