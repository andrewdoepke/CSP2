from flask import Flask, render_template, request
import sqlite3 as sql

from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main():
    return render_template('homepage.html', title="Home", header="All you need to know about Minecraft")


@app.route('/getmc')
def getmc():
    return render_template('get-minecraft.html', title="Get Minecraft", header="Get Minecraft")


# noinspection PyBroadException
@app.route('/blogpost', methods=['GET', 'POST'])
def blog():
    try:
        with sql.connect("static/database/database.db") as conn:
            curr = conn.cursor()
            conn.row_factory = sql.Row

            curr.execute("SELECT * FROM blogs;")
            hi = curr.fetchall()
    except:
        print("OH No")
    finally:
        return render_template('blog-posts.html', title="Blog Posts", header="Minecraft Blog", posts=list(hi))
        conn.close()


@app.route('/newpost', methods=['GET', 'POST'])
def newblog():
    return render_template('new-blog-post.html', title="New Post", header="New Post")


@app.route('/viewpost/<posti>', methods=['GET', 'POST'])
def viewblog(posti):
    try:
        with sql.connect("static/database/database.db") as conn:
            curr = conn.cursor()
            conn.row_factory = sql.Row
            curr.execute("SELECT subject, body FROM blogs WHERE blogid == ?;", posti)
            hi = curr.fetchone()

            curr.execute("SELECT * FROM comments WHERE blogid == ?", posti)
            com = curr.fetchall()
    finally:
        return render_template('blog-post.html', title="Blog Posts", header="Minecraft Blog", post=hi, comments=list(com))
        conn.close()


@app.route('/worldseed', methods=['GET', 'POST'])
def ws():
    return render_template('world-seeds.html', title="World Seeds", header="World Seeds")


@app.route('/newseed', methods=['GET', 'POST'])
def newworldseed():
    return render_template('new-world-seed.html', title="New Seed", header="New Seed")


@app.route('/viewseed', methods=['GET', 'POST'])
def viewws():
    return render_template('world-seed.html', title="View Seed", header="View Seed")


@app.route('/buildideas', methods=['GET', 'POST'])
def bi():
    return render_template('build-ideas.html', title="Build Ideas", header="Build Ideas")


@app.route('/buildform', methods=['GET', 'POST'])
def biform():
    return render_template('buildideaform.html', title="Submit an Idea", header="Submit a Build Idea")


@app.route('/adminlogin', methods=['GET', 'POST'])
def login():
    return render_template('admin-login.html', title="Login", header="Login")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Oops!", header="Oh No!"), 404


@app.route('/addblog', methods=['POST', 'GET'])
def addblog():
    if request.method == 'POST':
        try:
            title = request.form['subject']
            body = request.form['body']

            with sql.connect("static/database/database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO blogs (subject, body) VALUES(?, ?);", (title, body))

                con.commit()
                print("Record successfully added")
        finally:
            con.close()
            return redirect("/blogpost")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
