from flask import Flask, render_template, request, session, redirect
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name.strip() == '' and email.strip() == '':
            return "<h1>Invalid input</h1>"
        session['username'] = name
        session['usermail'] = email
        return redirect('/answer') 
    return render_template('index.html')

@app.route("/answer")
def showResult():
    username = session.get('username')
    usermail = session.get('usermail')
    return render_template('answer.html', username=username, usermail=usermail)

if __name__ == '__main__':
    app.run(debug=True)