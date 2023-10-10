from pickle import load, dump


def count(ch, a, b):
    s = 0
    for i in range(len(ch)):
        if a <= ch[i] <= b:
            s += 1
    return s


def seq(ch, a, b):
    s = 0
    sf = 0
    for i in range(len(ch)):
        if a <= ch[i] <= b:
            s += 1
        else:
            if s > sf:
                sf = s
            s = 0
    if s > sf:
        sf = s
    return sf


def score(mp):
    l = len(mp)
    f = (
        l * 4
        + (l - count(mp, "A", "Z")) * 2
        + (l - count(mp, "a", "z")) * 3
        + (l - count(mp.upper(), "A", "Z")) * 5
    ) - (seq(mp, "A", "Z") + seq(mp, "a", "z")) * 2
    return f


def force(sc):
    if sc < 20:
        return "tres faible"
    elif sc < 40:
        return "Faible"
    elif sc < 60:
        return "moyen"
    elif sc < 80:
        return "fort"
    else:
        return "tres fort"


def gener():
    F = open("forceMDP.dat", "wb")
    mpf = open("Motspass.txt", "r")
    l = mpf.readline()
    while l != "":
        e = {}
        e["password"] = l
        e["score"] = score(l)
        e["force"] = force(e["score"])
        print(e)
        dump(e, F)
        l = mpf.readline()
    F.close()
    mpf.close()


def genfort():
    F = open("forceMDP.dat", "rb")
    MPF = open("MDPfort.txt", "w")
    tf = ""
    f = ""
    b = True
    while b:
        try:
            l = load(F)
            if l["force"] == "tres fort":
                tf += l["password"]
            elif l["force"] == "fort":
                f += l["password"]
        except:
            b = False
    F.close
    MPF.write(tf)
    MPF.write(f)
    MPF.close()


gener()
genfort()
