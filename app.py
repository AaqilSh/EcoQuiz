from flask import Flask, render_template, request, redirect, session
import json
import random
from utils import get_question_by_difficulty, update_difficulty

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
    session['questions_order'] = filtered
    session['index'] = 0
    session['current_difficulty'] = 'medium'
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
        session['answers'] = []

    current_index = session['index']
    question_order = session['question_order']
    total = len(session['question_order'])

    if current_index >= total:
        score = session['score']
        answers = session['answers']
        session.clear()
        return render_template('review.html', score=score, total=total, answers=answers)

    question = question_order[current_index]

    if request.method == "POST":
        if 'answer' in request.form:
            selected_answer = request.form.get('answer')
            question = session['question_order'][current_index]
            correct_answer = session['question_order'][current_index]['answer']
            fact = session['question_order'][current_index].get('fact', '')
            is_correct = selected_answer == correct_answer
            if is_correct:
                session['score'] += 1

            session['current_difficulty'] = update_difficulty(is_correct, session['current_difficulty'])

            session['answers'].append({
                "question": question['question'],
                "options": question['options'],
                "selected": selected_answer,
                "correct": correct_answer,
                "is_correct": is_correct,
                "fact": fact
            })

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

        difficulty = session.get("current_difficulty", "medium")
        session["question"] = get_question_by_difficulty(questions, difficulty)
        
        if 'next' in request.form:
            session['index'] += 1
            current_index = session['index']
          
            if current_index >= total:
                score = session['score']
                answers = session['answers']
                session.clear()
                return render_template('review.html', score=score, total=total, answers=answers)
        
    question = session['question_order'][current_index]
    return render_template('quiz.html', question=question, current=current_index + 1, total=total, show_result=False
)

@app.route("/next", methods=["POST"])
def next_question():
    session["q_index"] += 1
    if session["q_index"] >= len(questions):
        return redirect("/result")  
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