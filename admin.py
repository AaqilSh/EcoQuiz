from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from functools import wraps
import json
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

QUESTIONS_FILE = "questions.json"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

def load_questions():
    with open(QUESTIONS_FILE) as f:
        return json.load(f)
    
def save_questions(questions):
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=2)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route("/")
@admin_required
def dashboard():
    questions = load_questions()
    return render_template("admin/dashboard.html", questions=questions)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('admin/login.html')

@admin_bp.route("/add", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        question = request.form["question"]
        options = request.form.getlist("options")
        answer = request.form["answer"]
        difficulty = request.form["difficulty"]
        fact = request.form["fact"]

        questions = load_questions()
        questions.append({
            "question": question,
            "options": options,
            "answer": answer,
            "difficulty": difficulty,
            "fact": fact
        })
        save_questions(questions)
        flash("Question added successfully!", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/add_question.html")

@admin_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin.login'))
