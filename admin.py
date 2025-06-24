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
