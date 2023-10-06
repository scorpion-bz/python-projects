from pickle import load, dump
from random import randint


def gencor(g, f):
    ch = f.readline()
    while ch != "":
        x = {}
        nm = ch[: ch.find("-")]
        pr = ch[ch.find("-") + 1 :]
        x["nom"] = nm + " " + pr
        x["email"] = nm + "." + pr + "@" + diff(ord(nm[0]), ord(pr[0]))
        x["pass"] = pr[0] + str(ord(nm[0])) + chr(randint(65, 65 + 26))
        dump(x, g)
        ch = f.readline()


def diff(a, b):
    d = abs(a - b)
    if d <= 6:
        return "Planet.tn"
    elif 7 <= d <= 12:
        return "Topnet.tn"
    elif 13 <= d <= 18:
        return "Google.fr"
    else:
        return "Yahoo.fr"


def aff(g):
    f = True
    while f:
        try:
            ch = load(g)
            print(ch)
        except:
            f = False


def lis(g, s):
    f = True
    ser = input("server ?   ")
    if exist(ser, s):
        while f:
            try:
                ch = load(g)
                if ch["email"][ch["email"].find("@") + 1 :] == ser:
                    print(ch["nom"])
            except:
                f = False


def exist(a, s):
    ch = s.readline()
    while ch != "" and ch.find(a) == -1:
        ch = s.readline()
    return ch != ""


f = open("NOMPR.txt", "r")
g = open("CORDON.dat", "wb")
gencor(g, f)
f.close()
g.close()
g = open("CORDON.dat", "rb")
aff(g)
g.close()
g = open("CORDON.dat", "rb")
s = open("SERVEUR.txt", "r")
lis(g, s)
g.close()
s.close()
