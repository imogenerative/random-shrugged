import atexit
import random

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from flask import Flask, render_template

pARAGRAPHS = Flask(__name__)

# sETTINGS
tHE_DURATION = 1800
tHE_FILE = "paragraphs.txt"

# rETURN A PARAGRAPH FROM THE TEXT
def dEFINE_PARAGRAPH():
    global tHE_PARAGRAPH
    with open(tHE_FILE) as tEXT:
        pARAGRAPHS = tEXT.readlines()
        tHE_PARAGRAPH = pARAGRAPHS[random.randint(0, len(pARAGRAPHS))]

        return tHE_PARAGRAPH

sCHEDULER = BackgroundScheduler()
sCHEDULER.start()
sCHEDULER.add_job(
    func=dEFINE_PARAGRAPH,
    trigger=IntervalTrigger(seconds=tHE_DURATION),
    id="tHE_PARAGRAPH",
    name="gET A RANDOM PARAGRAPH",
    replace_existing=True)
atexit.register(lambda: sCHEDULER.shutdown())

tHE_PARAGRAPH = dEFINE_PARAGRAPH()

@pARAGRAPHS.route('/')
def pARAGRAPH():
    return render_template("index.html", paragraph=tHE_PARAGRAPH)

