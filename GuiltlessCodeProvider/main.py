from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/download')
def download():
    path = './Provide/code.py'
    return send_file(path, as_attachment=True)

@app.route('/agentcode')
def agentcode():
    path = './Provide/agentcode.py'
    return send_file(path, as_attachment=True)

@app.route('/requirements')
def requirementsfile():
    path = './Provide/requirements.txt'
    return send_file(path, as_attachment=True)

@app.route('/poetry')
def poetry():
    path = './Provide/poetry.lock'
    return send_file(path, as_attachment=True)

@app.route('/pyproject')
def pyproject():
    path = './Provide/pyproject.toml'
    return send_file(path, as_attachment=True)
    
app.run(host='0.0.0.0', port=81)