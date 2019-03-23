from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ahmed',
        'title': 'FUN',
        'content': 'First post content',
        'date_posted': 'March 23,2019'
    },
    {
        'author': 'Group11',
        'title': 'FUN FUN',
        'content': 'Second post content',
        'date_posted': 'March 23,2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
