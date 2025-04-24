from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
 app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/databasename"

db = SQLAlchemy(app)


#model
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

@app.route('/home')
def home():
    return 'Hello, World!'


@app.route('/')
def index():
    return render_template('index.html',name="Akshay")
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
