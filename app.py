# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personaje/crear')
def crearPersonaje():
    return render_template('personajes.html')

if __name__ == '__main__':
    app.run(debug=True)