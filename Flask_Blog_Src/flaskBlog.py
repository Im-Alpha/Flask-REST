from flask import Flask, render_template

app = Flask(__name__) # name of the module, flask knows where too look for files

posts =[
    {
        'author': 'Jacob Delgado',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 16, 2024'
    },
    {
        'author': 'Keiwa on the Kob',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 18, 2024'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)
    
    