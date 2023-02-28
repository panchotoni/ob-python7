def suma(a,b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    return a / b
def horis(a):
    if a >= 19 and a <= 24:
        return "Es hora de irse del job"
    elif a < 19 and a >= 0:
        falta = a - 19
        abs(falta)
        return "Es hora de jobear, te quedan: ", abs(falta)
    else:
        return "El dia tiene 24 hs estupido"

