from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main():
    return render_template('homepage.html', title="Home")


@app.route('/getmc')
def getmc():
    return render_template('get-minecraft.html', title="Get Minecraft")


@app.route('/blogpost', methods=['GET', 'POST'])
def blog():
    return render_template('blog-posts.html', title="Blog Posts")


@app.route('/newpost', methods=['GET', 'POST'])
def newblog():
    return render_template('new-blog-post.html')


@app.route('/worldseed', methods=['GET', 'POST'])
def ws():
    return render_template('world-seeds.html', title="World Seeds")


@app.route('/newseed', methods=['GET', 'POST'])
def newworldseed():
    return render_template('new-world-seed.html')


@app.route('/buildideas', methods=['GET', 'POST'])
def bi():
    return render_template('build-ideas.html', title="Build Ideas")


@app.route('/buildform', methods=['GET', 'POST'])
def biform():
    return render_template('buildideaform.html', title="Build Ideas")


@app.route('/adminlogin', methods=['GET', 'POST'])
def login():
    return render_template('admin-login.html', title="Login")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Oops!"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
