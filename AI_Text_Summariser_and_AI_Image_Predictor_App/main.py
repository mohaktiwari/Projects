from flask import Flask,render_template,request,jsonify,session
from summarizer import summarize_text
from AiorNot import labels
import os
import ast

app=Flask(__name__)

secret_key = os.urandom(24)
app.secret_key =secret_key

@app.route("/")
def textSummarizer():
    return render_template('textSummarizer.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text_to_summarize = request.form.get('text_to_summarize')
    session['text_to_summarize'] = text_to_summarize

    if 200 < len(text_to_summarize) < 100000:
        summary =summarize_text(text_to_summarize)
    else:
        summary = "The input text must be between 200 and 100000 characters."

    session['summary'] = summary

    return render_template('textSummarizerres.html', 
                           summary=session.get('summary', ''), 
                           text_to_summarize=session.get('text_to_summarize', ''))

@app.route("/aiPredictor")
def aiPredictor():
    return render_template('aiorNothome.html')

@app.route('/label', methods=['POST'])
def label():
    img=request.form.get('image')
    val=labels(img)
    lst = ast.literal_eval(val)
    return render_template('aiorNot.html', lst=lst, img=img)

if __name__==('__main__'):
    app.run(debug=True)