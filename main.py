from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main():
    return render_template('homepage.html', title="Home", header="All you need to know about Minecraft")


@app.route('/getmc')
def getmc():
    return render_template('get-minecraft.html', title="Get Minecraft", header="Get Minecraft")


@app.route('/blogpost', methods=['GET', 'POST'])
def blog():
    return render_template('blog-posts.html', title="Blog Posts", header="Blog Posts")


@app.route('/newpost', methods=['GET', 'POST'])
def newblog():
    return render_template('new-blog-post.html', title="New Post", header="New Post")


@app.route('/viewpost', methods=['GET', 'POST'])
def viewblog():
    return render_template('blog-post.html', title="View Post", header="Blog Post")


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
