import os, glob

result = []

def getpdfs(path):
    for x in os.walk(path):
        for y in glob.glob(os.path.join(x[0], '*.pdf')):
            result.append(y)

    print(result)

def main():
    getpdfs(os.getcwd())

if __name__ == "__main__":
    main()    