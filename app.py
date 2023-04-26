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
        {'title': 'Article 1', 'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
        {'title': 'Article 2', 'content': 'Nullam gravida nibh eu eleifend ultricies.'},
        {'title': 'Article 3', 'content': 'Praesent tristique mauris eu neque semper, at volutpat mauris blandit.'},
        {'title': 'Article 4', 'content': 'Suspendisse ac turpis ut dolor consequat malesuada.'},
        {'title': 'Article 5', 'content': 'Sed eget magna ut leo molestie fringilla.'},
    ]
    return render_template('news.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)