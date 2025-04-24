from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html',context="Home, I am here to help us for the going to the account help")
if __name__ == '__main__':
    app.run(debug=True)
