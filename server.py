from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.get('/')
def index():
    # form display
    return render_template('index.html')

@app.post('/process')
def plus2():
    session['visit_count'] += 1
    return redirect('/')

@app.post('/process')
def process():
    print(request.form)
    session['visit_count'] += (int(request.form['num']) - 1)
    return redirect('/')


@app.route('/reset')
def reset():
    
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

