from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Ezeibe Uchechukwu",
        "title": "Blog post 1",
        "content": "First post contect",
        "date_posted": "November 9, 2023"
    },

    {
        "author": "Okoro Emeka",
        "title": "Blog post 2",
        "content": "Second post contect",
        "date_posted": "November 10, 2023"
    },

    {
        "author": "Jennifer Mark",
        "title": "Blog post 3",
        "content": "Third post contect",
        "date_posted": "November 11, 2023"
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About us')

if __name__ == '__main__':
    app.run(debug=True)