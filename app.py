from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    name = ""
    python_marks = c_marks = dsa_marks = None

    if request.method == 'POST':
        try:
            name = request.form['name']
            python_marks = int(request.form['python'])
            c_marks = int(request.form['c'])
            dsa_marks = int(request.form['dsa'])

            if python_marks < 35 or c_marks < 35 or dsa_marks < 35:
                result = "Fail"
            else:
                result = "Pass"
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('index.html', result=result, name=name,
                           python_marks=python_marks, c_marks=c_marks, dsa_marks=dsa_marks)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
