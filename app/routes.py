from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/inventory')
def inventory():
    return render_template('inventory.html')
# @app.route('/login')
# @app.route('/report')
# @app.route('/sales')
# @app.route('/products')