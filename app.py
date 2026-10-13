from flask import Flask, render_template, request

app = Flask(__name__)
PASS_MARK = 35
MAX_MARK = 100
SUBJECTS = (("python", "Python", "PY"), ("c", "C Programming", "C"), ("dsa", "Data Structures & Algorithms", "DSA"))


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    name = ""
    marks = {key: "" for key, _, _ in SUBJECTS}
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        try:
            if not name:
                raise ValueError("Please enter the student's name.")
            parsed = {}
            for key, label, _ in SUBJECTS:
                raw = request.form.get(key, "").strip()
                if raw == "":
                    raise ValueError(f"Enter marks for {label}.")
                value = int(raw)
                if not 0 <= value <= MAX_MARK:
                    raise ValueError(f"{label} marks must be between 0 and 100.")
                parsed[key] = value
                marks[key] = value

            total = sum(parsed.values())
            passed_all = all(score >= PASS_MARK for score in parsed.values())
            result = {
                "status": "PASS" if passed_all else "NEEDS ATTENTION",
                "passed": passed_all,
                "total": total,
                "percentage": total / (len(SUBJECTS) * MAX_MARK) * 100,
                "average": total / len(SUBJECTS),
                "subjects": [
                    {"label": label, "short": short, "marks": parsed[key],
                     "passed": parsed[key] >= PASS_MARK,
                     "percent": parsed[key] / MAX_MARK * 100}
                    for key, label, short in SUBJECTS
                ],
            }
        except ValueError as exc:
            error = str(exc) or "Please enter valid whole-number marks."
        except (TypeError, OverflowError):
            error = "Please enter valid whole-number marks."

    return render_template("index.html", name=name, marks=marks, result=result,
                           error=error, pass_mark=PASS_MARK)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
