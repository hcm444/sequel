from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_sql', methods=['POST'])
def execute_sql():
    try:
        query = request.form['sql_query']
        connection = sqlite3.connect('movies.db')
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return render_template('index.html', result=result, query=query)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
