from flask import Flask, render_template, request
import os

app = Flask(__name__)

def read_timetable_file(filepath):
    """
    Reads a text file where each line is:
    subject,time,room, bgcolour
    Returns a list of dicts.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError("Timetable file not found.")

    timetable = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                subject, time, room, bgcolour = line.split("/")
                timetable.append({
                    "subject": subject.strip(),
                    "time": time.strip(),
                    "room": room.strip(),
                    "bgcolour": bgcolour.strip()
                })
            except ValueError:
                # Skip malformed lines
                continue

    return timetable


@app.route("/", methods=["GET", "POST"])
def index():
    timetable = None
    error = None

    if request.method == "POST":
        filename = request.form.get("filename", "")
        try:
            timetable = read_timetable_file(filename)
        except Exception as e:
            error = str(e)

    return render_template("index.html", timetable=timetable, error=error)


if __name__ == "__main__":
    app.run(debug=True)
