from flask import Flask, render_template, request, redirect, session
import json
import random

app = Flask(__name__)
app.secret_key = "ecoquizsecret"  

def load_questions():
    with open("questions.json") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start")
def start_quiz():
    difficulty = request.args.get("difficulty", "easy")
    all_questions = load_questions()
    filtered = [q for q in all_questions if q["difficulty"] == difficulty]
    random.shuffle(filtered)
    session['questions'] = filtered
    session['current'] = 0
    session['score'] = 0
    return redirect("/quiz")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selected = request.form.get("answer")
        current_q = session['questions'][session['current']]
        if selected == current_q["answer"]:
            session['score'] += 1
        session['current'] += 1

    if session['current'] >= len(session['questions']):
        return redirect("/result")
    
    question = session['questions'][session['current']]
    return render_template("quiz.html", question=question, current=session['current'] + 1, total=len(session['questions']))
