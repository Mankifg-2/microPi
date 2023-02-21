fp = "out.txt"

def readd():
    with open(fp,"r") as f:
        data = f.read().splitlines()
        print(data)

readd()