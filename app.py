from flask import Flask, render_template, request, redirect, jsonify, session
import sqlite3

app = Flask(__name__)
app.secret_key = "lightofeducation123"


# database
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def loading():
    return render_template("loading.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":
        phone = request.form.get("phone")
        password = request.form.get("password")

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE phone=? AND password=?",
            (phone, password)
        )

        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = phone
            return redirect("/dashboard")
        else:
            error = "আপনার পাসওয়ার্ড ভুল হয়েছে"

    return render_template("login.html", error=error)

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    error = ""

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        password = request.form.get("password")

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        try:
            c.execute(
                "INSERT INTO users (name, phone, password) VALUES (?, ?, ?)",
                (name, phone, password)
            )

            conn.commit()

            session["user"] = phone

            return redirect("/dashboard")

        except:
            error = "এই নাম্বার দিয়ে already একাউন্ট করা হয়েছে"

        finally:
            conn.close()

    return render_template("register.html", error=error)


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


@app.route("/page1")
def page1():
    return render_template("page1.html")


@app.route("/bangla")
def bangla():
    return render_template("bangla.html")


@app.route("/english")
def english():
    return render_template("english.html")


@app.route("/page30")
def page30():
    return render_template("page30.html")


@app.route("/page31")
def page31():
    return render_template("page31.html")


@app.route("/page32")
def page32():
    return render_template("page32.html")


@app.route("/page33")
def page33():
    return render_template("page33.html")


@app.route("/page34")
def page34():
    return render_template("page34.html")


@app.route("/page35")
def page35():
    return render_template("page35.html")


@app.route("/page36")
def page36():
    return render_template("page36.html")


@app.route("/page37")
def page37():
    return render_template("page37.html")


@app.route("/page38")
def page38():
    return render_template("page38.html")


@app.route("/page39")
def page39():
    return render_template("page39.html")


@app.route("/page42")
def page42():
    return render_template("page42.html")


@app.route("/page43")
def page43():
    return render_template("page43.html")


@app.route("/page44")
def page44():
    return render_template("page44.html")


@app.route("/page45")
def page45():
    return render_template("page45.html")


@app.route("/page46")
def page46():
    return render_template("page46.html")


@app.route("/page47")
def page47():
    return render_template("page47.html")


@app.route("/page48")
def page48():
    return render_template("page48.html")


@app.route("/page49")
def page49():
    return render_template("page49.html")


@app.route("/page40")
def page40():
    return render_template("page40.html")


@app.route("/page41")
def page41():
    return render_template("page41.html")


@app.route("/math")
def math():
    return render_template("math.html")


@app.route("/science")
def science():
    return render_template("science.html")


@app.route("/computer")
def computer():
    return render_template("computer.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/assignment")
def assignment():
    return render_template("assignment.html")


@app.route("/video")
def video():
    return render_template("video.html")


@app.route("/progress")
def progress():
    return render_template("progress.html")


@app.route("/gk")
def gk():
    return render_template("gk.html")


@app.route("/creative")
def creative():
    return render_template("creative.html")


@app.route("/page2")
def page2():
    return render_template("page2.html")


@app.route("/page3")
def page3():
    return render_template("page3.html")


@app.route("/page4")
def page4():
    return render_template("page4.html")


@app.route("/page5")
def page5():
    return render_template("page5.html")


@app.route("/page6")
def page6():
    return render_template("page6.html")


@app.route("/page7")
def page7():
    return render_template("page7.html")


@app.route("/page21")
def page21():
    return render_template("page21.html")


@app.route("/page20")
def page20():
    return render_template("page20.html")


@app.route("/page22")
def page22():
    return render_template("page22.html")


@app.route("/page9")
def page9():
    return render_template("page9.html")


@app.route("/page8")
def page8():
    return render_template("page8.html")


@app.route("/page10")
def page10():
    return render_template("page10.html")
   
   
@app.route("/page100")
def page100():
    return render_template("page100.html")


@app.route("/otp")
def otp():
    return render_template("otp.html")


@app.route("/send_otp", methods=["POST"])
def send_otp():
    phone = request.form.get("phone")
    return redirect("/otp")

@app.route("/read_book")
def read_book():
    return render_template("read_book.html")
    
videos = [
    {
         "title": "বাংলা ",
        "file": "video1.mp4",
        "thumb": "thumb1.jpg"
    },
    {
        "title": "বাংলা ব্যাকরণ",
        "file": "video2.mp4",
        "thumb": "thumb2.jpg"
    },
    {
        "title": "কবিতা",
        "file": "video3.mp4",
        "thumb": "thumb3.jpg"
    }
]

@app.route("/videos")
def videos_page():
    return render_template("videos.html", videos=videos)

@app.route("/video/<filename>")
def play_video(filename):
    return render_template("player.html", filename=filename)


@app.route("/verify", methods=["POST"])
def verify():
    otp = request.form.get("otp")

    if otp == "4444":
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


if __name__ == "__main__":
    app.run(debug=True)
    
    
