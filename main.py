import os
from flask import Flask, render_template, request, redirect, url_for
# render_template: for data dymanic rendering with Jinja2 template engine
# request: object that encapsulates data coming from client's request
# redirect: util fn that returns a response object
# url_for: fn that generates URLs for endpoints
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tech_stack')
    tech_stack = cur.fetchall()
    cur.close()
    return render_template('index.html', tech_stack=tech_stack)

@app.route('/add', methods=['POST'])
def add():
    new_component = request.form.get('new_component')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO tech_stack (component) VALUES (%s)', [new_component])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)