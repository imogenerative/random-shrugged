import atexit, os, random

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from flask import Flask, render_template

pARAGRAPHS = Flask(__name__)

# sETTINGS
tHE_DURATION = 10
tHE_FILE = "paragraphs.txt"

# rETURN A PARAGRAPH FROM THE TEXT
def dEFINE_PARAGRAPH():
    def aCTUAL_INES(file):
        for line in file:
            line = line.rstrip()
            if line:
                yield line
    pARAGRAPHS = ()

    global tHE_PARAGRAPH
    with open(tHE_FILE) as file:
        for line in aCTUAL_LINES(file):
            pARAGRAPHS.append(line)
    tHE_PARAGRAPH = pARAGRAPHS[random.randint(0, len(pARAGRAPHS))]

    return tHE_PARAGRAPH

# tHE SCHEDULER
sCHEDULER = BackgroundScheduler()
sCHEDULER.start()
sCHEDULER.add_job(
    func=dEFINE_PARAGRAPH,
    trigger=IntervalTrigger(seconds=tHE_DURATION),
    id="tHE_PARAGRAPH",
    name="gET A RANDOM PARAGRAPH",
    replace_existing=True)
atexit.register(lambda: sCHEDULER.shutdown())

@pARAGRAPHS.before_first_request
def fIRST_PARAGRAPH():
    global tHE_PARAGRAPH
    tHE_PARAGRAPH = dEFINE_PARAGRAPH()

    return tHE_PARAGRAPH

@pARAGRAPHS.route('/')
def pARAGRAPH():
    return render_template("index.html", paragraph=tHE_PARAGRAPH)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    pARAGRAPHS.run(host="0.0.0.0", port=port)
