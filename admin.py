from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import json
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

QUESTIONS_FILE = "questions.json"

def load_questions():
    with open(QUESTIONS_FILE) as f:
        return json.load(f)
    
def save_questions(questions):
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=2)

@admin_bp.route("/")
def dashboard():
    questions = load_questions()
    return render_template("admin/dashboard.html", questions=questions)

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