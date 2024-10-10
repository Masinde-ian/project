from app import app
from flask import render_template

@app.route('/')
@app.route('/inventory')
@app.route('/login')
@app.route('/report')
@app.route('/sales')
def index():
    return render_template('home.html')