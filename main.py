from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main():
    return render_template('homepage.html')


@app.route('/getmc')
def getmc():
    return render_template('get-minecraft.html')


@app.route('/blogpost', methods=['GET', 'POST'])
def blog():
    return render_template('blog-posts.html')


@app.route('/worldseed', methods=['GET', 'POST'])
def ws():
    return render_template('world-seeds.html')


@app.route('/buildideas', methods=['GET', 'POST'])
def bi():
    return render_template('build-ideas.html')


@app.route('/adminlogin', methods=['GET', 'POST'])
def login():
    return render_template('admin-login.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
