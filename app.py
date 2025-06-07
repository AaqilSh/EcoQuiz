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
    questions=load_questions()
    if 'index' not in session:
        session['index'] = 0
        session['score'] = 0
        random.shuffle(questions)
        session['question_order'] = questions

    current_index = session['index']
    total = len(session['question_order'])

    if 'answers' not in session:
    session['answers'] = []

    if request.method == "POST":
        if 'answer' in request.form:
            selected_answer = request.form.get('answer')
            correct_answer = session['question_order'][current_index]['answer']
            fact = session['question_order'][current_index].get('fact', '')
            is_correct = selected_answer == correct_answer
            if is_correct:
                session['score'] += 1

            question = session['question_order'][current_index]
            return render_template(
                'quiz.html',
                question=question,
                current=current_index + 1,
                total=total,
                selected=selected_answer,
                correct=correct_answer,
                show_result=True,
                is_correct=is_correct,
                fact=fact
            )
        elif 'next' in request.form:
            session['index'] += 1
            current_index = session['index']
          
            if current_index >= total:
                score = session['score']
                session.clear()
                return render_template('result.html', score=score, total=total)
        
    question = session['question_order'][current_index]
    return render_template('quiz.html', question=question, current=current_index + 1, total=total, show_result=False
)

@app.route("/next", methods=["POST"])
def next_question():
    session["q_index"] += 1
    if session["q_index"] >= len(questions):
        return redirect("/result")  # Redirect to final result page
    return redirect("/")


@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('quiz'))

@app.route("/result")
def result():
    score = session.get('score', 0)
    total = len(session.get('questions', []))
    return render_template("result.html", score=score, total=total)