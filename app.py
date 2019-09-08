from flask import Flask,render_template,request,url_for,redirect

from Spellcheck import spell_check,corrected,delete
app=Flask(__name__)

@app.route('/')

def index():
    correct=corrected()
    return render_template("index.html",correct=correct)

@app.route('/' ,methods=['GET','POST'])

def spell():
     spell_check(text=request.form['incor'])
     return redirect(url_for('index'))

@app.route('/dele',methods=['POST'])

def dele():
    delete()
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)

