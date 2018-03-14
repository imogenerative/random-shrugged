import atexit, os, random

from flask import Flask, render_template

pARAGRAPHS = Flask(__name__)

# sETTINGS
tHE_FILE = "markov.txt"

# rETURN A PARAGRAPH FROM THE TEXT
def dEFINE_PARAGRAPH():
    def aCTUAL_LINES(file):
        for line in file:
            line = line.rstrip()
            if line:
                yield line
    pARAGRAPHS = []

    with open(tHE_FILE) as file:
        for line in aCTUAL_LINES(file):
            pARAGRAPHS.append(line)
    tHE_PARAGRAPH = pARAGRAPHS[random.randint(0, len(pARAGRAPHS))]

    return tHE_PARAGRAPH

@pARAGRAPHS.route('/')
def pARAGRAPH():
    return render_template("index.html", paragraph=dEFINE_PARAGRAPH())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    pARAGRAPHS.run(host="0.0.0.0", port=port)
