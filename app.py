from flask import Flask, render_template, request, redirect, url_for
from database import db
from models import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.query.all()  # Mengambil semua data user dari database
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    if name:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
