import sys
from flask import Flask,render_template
from utils import SCORES_FILE_NAME

app = Flask(__name__)

def score_server ():
    try:
        f = open(SCORES_FILE_NAME,mode='r')
        score = int(f.read())
        return render_template('score.html',SCORE=score)
        f.close()
    except:
        return render_template('error.html',ERROR=(sys.exc_info()[0]))

@app.route("/")
def home():
    return score_server()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)