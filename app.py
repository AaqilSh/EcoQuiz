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
    if 'index' not in session:
        session['index'] = 0
        session['score'] = 0
        random.shuffle(questions)
        session['question_order'] = questions

    current_index = session['index']
    total = len(session['question_order'])

    if request.method == "POST":
        selected_answer = request.form.get('answer')
        correct_answer = session['question_order'][current_index - 1]['answer']

        if selected_answer == correct_answer:
            session['score'] += 1

    if current_index >= total:
        score = session['score']
        session.clear()
        return render_template('result.html', score=score, total=total)
        
    question = session['question_order'][current_index]
    session['index'] += 1
    return render_template('quiz.html', question=question, current=current_index + 1, total=total)

@app.route("/result")
def result():
    score = session.get('score', 0)
    total = len(session.get('questions', []))
    return render_template("result.html", score=score, total=total)