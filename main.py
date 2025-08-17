from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from wtforms import PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import subprocess
import os
from config import rootPass
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

class LoginForm(FlaskForm):
    name = PasswordField('', validators=[DataRequired()])
    submit = SubmitField('Login')

class LockComp(FlaskForm):
    lock = SubmitField('Заблокировать компьютер')
    unlock = SubmitField('Разблокировать компьютер')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm
    if request.method == 'POST' :
        rootpass_fromForm = request.form.get('pass')
        # rootPass = rootPass
        if rootpass_fromForm == rootPass:
            return redirect('dashboard')
    return render_template('index.html', form=form())

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    form = LockComp
    def is_process_running(process_name):
        try:
            # Для Windows (если process_name — имя исполняемого файла):
            output = subprocess.check_output(["tasklist"], text=True)
            return process_name.lower() in output.lower()
        except subprocess.CalledProcessError:
            return False

    if is_process_running('SystemLocker.exe'):
        status = 'Заблокирован'
        # return jsonify({"status": "Заблокирован"})
    else:
        status = 'Разблокирован'
        # return jsonify({"status": "Разблокирован"})

    if form.validate_on_submit and 'lock' in request.form:
        subprocess.Popen('C:/Users/Nikita/Documents/family-link/build/exe.win-amd64-3.13/SystemLocker.exe')
        return redirect('dashboard')
    elif form.validate_on_submit and 'unlock' in request.form:
        os.system('taskkill /im SystemLocker.exe* /f')
        return redirect('dashboard')
    return render_template('dashboard.html', form=form(), status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

# 8212, 1868
# 9656