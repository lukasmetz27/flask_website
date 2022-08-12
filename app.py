from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="home")

@app.route("/project/")
def project():
    return render_template("project.html", title="project")

@app.route("/blogs/")
def blogs():
    return render_template("blogs.html", title="blogs")

@app.route("/aboutme/")
def aboutme():
    return render_template("aboutme.html", title="aboutme")



if __name__ == "__main__":
    app.run(debug=True)