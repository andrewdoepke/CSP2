from flask import Flask, render_template, request
import sqlite3 as sql

from werkzeug.utils import redirect

app = Flask(__name__)

database = "static/database/database.db"

keep_database = 0
# if you set this to 1, it keeps the database. Use this for testing but for Github sake right now,
# keep this at 0 so it clears the database before running. This will prevent duplicates if you need it

if keep_database != 1:
    with sql.connect(database) as conn:
        curr = conn.cursor()
        curr.execute("DELETE FROM comments")
        curr.execute("DELETE FROM blogs")
        curr.execute("UPDATE blogs SET blogid=0")
        curr.execute("UPDATE comments SET commid=0")
        curr.execute("UPDATE Cards SET likes=0, dislikes=0")


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
        with sql.connect(database) as con:
            cur = con.cursor()
            con.row_factory = sql.Row

            cur.execute("SELECT * FROM blogs;")
            hi = cur.fetchall()
    except:
        print("OH No")
    finally:
        return render_template('blog-posts.html', title="Blog Posts", header="Minecraft Blog", posts=list(hi))


@app.route('/newpost', methods=['GET', 'POST'])
def newblog():
    return render_template('new-blog-post.html', title="New Post", header="New Post")


@app.route('/viewpost/<posti>', methods=['GET', 'POST'])
def viewblog(posti):
    try:
        with sql.connect(database) as con:
            curs = con.cursor()
            con.row_factory = sql.Row
            curs.execute("SELECT * FROM blogs WHERE blogid == ?;", [posti])
            hi = curs.fetchone()
            curs.execute("SELECT * FROM comments WHERE blogid == ?", [posti])
            com = curs.fetchall()
    finally:
        return render_template('blog-post.html', title="Blog Posts", header="Minecraft Blog", post=hi,
                               comments=list(com))


@app.route('/comment/<posti>', methods=['GET', 'POST'])
def comment(posti):
    if request.method == 'POST':
        try:
            commen = request.form['comment']
            myname = request.form['myname']

            with sql.connect(database) as con:
                cur = con.cursor()

                cur.execute("INSERT INTO comments (blogid, comment, name) VALUES(?, ?, ?);", (posti, commen, myname))

                con.commit()
                print("Record successfully added")
        finally:
            con.close()
            return redirect('/viewpost/%s' % posti)


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
    cards = makecards()
    return render_template('build-ideas.html', title="Build Ideas", header="Build Ideas", cards=cards)


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

            with sql.connect(database) as con:
                cur = con.cursor()

                cur.execute("INSERT INTO blogs (subject, body) VALUES(?, ?);", (title, body))

                con.commit()
                print("Record successfully added")
        finally:
            con.close()
            return redirect("/blogpost")


class Card:
    def __init__(self, frontcode, backcode, cid, ratio):
        self.frontcode = frontcode
        self.backcode = backcode
        self.cid = cid
        self.ratio = ratio


@app.route('/like/<cardid>', methods=['POST', 'GET'])
def like(cardid):
    try:
        with sql.connect(database) as con:
            curs = con.cursor()
            curs.execute("SELECT * FROM Cards WHERE cardid == ?", [cardid])
            curs.execute("UPDATE Cards SET likes = likes + 1 WHERE cardid == ?", [cardid])
    finally:
        con.close()
        return redirect('/buildideas')


@app.route('/dislike/<cardid>', methods=['POST', 'GET'])
def dislike(cardid):
    try:
        with sql.connect(database) as con:
            curs = con.cursor()
            curs.execute("SELECT * FROM Cards WHERE cardid == ?", [cardid])
            curs.execute("UPDATE Cards SET dislikes = dislikes + 1 WHERE cardid == ?", [cardid])
    finally:
        con.close()
        return redirect('/buildideas')


def makecards():
    try:
        with sql.connect(database) as con:
            cur = con.cursor()
            con.row_factory = sql.Row
            cur.execute("SELECT * FROM Cards")
            hi = cur.fetchall()
            ratios = []
            for a in hi:
                likes = a[1]
                disl = a[2]
                if disl == 0:
                    ratios.append(100)
                else:
                    ratio = likes / (likes + disl)
                    ratio = format(ratio, '.2f')
                    ratios.append(ratio)
    finally:
        con.close()

    card0 = Card("""<div class = "card-image">
    <img class = "card-image" src = "/static/images/house-build.jpg" alt = "House Build" class = "build-img"  id = "house">
    </div>
    <div class="card-description">
    <h2 class = "text-desc">Starter House</h2>
    </div>""",
                 """<div class = "build-material">
                    <a href = "https://youtu.be/jUmIeyMsYXE?t=34" target="_blank"><h3 class = "tutorial">Tutorial</h3></a>
                    <ul>
                        <li>Birch Wood Planks</li>
                        <li>Birch Fence</li>
                        <li>Glass Pane</li>
                        <li>Oak Door</li>
                        <li>Oak Wood Stairs</li>
                        <li>Birch Wood Slab</li>
                        <li>Oak Wood Slab</li>
                    </ul>
                </div>""", 0, ratios[0])

    card1 = Card("""<div class = "card-image">
                <img class = "card-image" src = "/static/images/aquarium-build.jpg" alt = "Aquarium Build" class = "build-img" id = "aquarium">
            </div>
            <div class="card-description">
                <h2 class = "text-desc">Wall-less Aquarium</h2>
            </div>""",
                 """<div class = "build-material">
                <a href = "https://youtu.be/wQI5lww6j9I" target="_blank"><h3 class = "tutorial">Tutorial</h3></a>
                <ul>
                    <li>Water Bucket</li>
                    <li>Smooth Quartz Stairs</li>
                    <li>Glass</li>
                    <li>Kelp (<i>Optional</i>)</li>
                    <li>Sea Grass (<i>Optional</i>)</li>
                    <li>Coral (<i>Optional</i>)</li>
                    <li>Fish (<i>Optional</i>)</li>
                </ul>
            </div>""", 1, ratios[1])
    card2 = Card("""<div class = "card-image">
                    <img class = "card-image" src = "/static/images/stable-build.jpg" alt = "Horse Stable Build" class = "build-img" id = "stable">
                </div>
                <div class="card-description">
                    <h2 class = "text-desc">Horse Stable</h2>
                </div>""",
                 """	<div class = "build-material">
                    <a href = "https://youtu.be/PPAa2T1pBto" target="_blank"><h3 class = "tutorial">Tutorial</h3></a>
                    <ul>
                        <li>Spruce Log</li>
                        <li>Dark Oak/Spruce Stairs</li>
                        <li>Dark Oak/Spruce Slab</li>
                        <li>Dark Oak/Spruce Fence</li>
                        <li>Lantern</li>
                        <li>Hay Bale</li>
                        <li>Spruce Fence Gate</li>
                    </ul>
                </div>""", 2, ratios[2])
    card3 = Card("""<div class = "card-image">
                    <img class = "card-image" src = "/static/images/boat-build.jpg" alt = "Boat Build" class = "build-img" id = "boat">
                </div>
                <div class="card-description">
                    <h2 class = "text-desc">Boat House</h2>
                </div>""",
                 """<div class = "build-material">
                <a href = "https://youtu.be/kNFsOqg7aUo" target="_blank"><h3 class = "tutorial">Tutorial</h3></a>
                <ul>
                    <li>Spruce Trapdoor</li>
                    <li>Oak Trapdoor</li>
                    <li>Spruce Slab</li>
                    <li>Spruce Stairs</li>
                    <li>Spruce Fence</li>
                    <li>Spruce Fence Gate</li>
                    <li>Ladder</li>
                    <li>Oak Door</li>
                    <li>Stripped Spruce Log</li>
                    <li>Campfire</li>
                    <li>Water Bucket</li>
                </ul>
            </div>""", 3, ratios[3])

    card4 = Card("""<div class = "card-image">
                    <img class = "card-image" src = "/static/images/nether-build.jpg" alt = "Nether Base Build" class = "build-img" id = "nether">
                </div>
                <div class="card-description">
                    <h2 class = "text-desc">Nether Base</h2>
                </div> """,
                 """	<div class = "build-material">
                    <a href = "https://youtu.be/3UndiBacPvw?t=314" target="_blank"><h3 class = "tutorial">Tutorial</h3></a>
                    <ul>
                        <li>Basalt</li>
                        <li>Nether Bricks</li>
                        <li>Nether Brick Stairs</li>
                        <li>Nether Brick Slab</li>
                        <li>Crimson Planks</li>
                        <li>Crimson Slab</li>
                        <li>Crimson Trapdoor</li>
                        <li>Crimson Stem</li>
                        <li>Crimson Fence</li>
                    </ul>
                </div>""", 4, ratios[4])

    cards = [card0, card1, card2, card3, card4]
    return cards


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    app.jinja_env.auto_reload = True
