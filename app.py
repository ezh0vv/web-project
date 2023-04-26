from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    now = datetime.datetime.now()
    return render_template('home.html', now=now)

@app.route('/news')
def news():
    articles = [
        {'title': 'Article 1', 'content': 'Real Madrid" beat "Liverpool" 2:5 at "Anfield".'},
        {'title': 'Article 2', 'content': 'Manchester City" defeated "Bayern Munich" 3:0.'},
        {'title': 'Article 3', 'content': '"Inter" and "Benfica" played to a 3:3 draw.'},
        {'title': 'Article 4', 'content': '"Real Madrid" beat "Barcelona" 4:0.'}
    ]
    return render_template('news.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
