from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import json
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

QUESTIONS_FILE = "questions.json"

def load_questions():
    with open(QUESTIONS_FILE) as f:
        return json.load(f)