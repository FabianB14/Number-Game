from flask import Flask, render_template, redirect,session,request
import random
app = Flask(__name__)
app.secret_key ="can't see me"
@app.route('/')
def index():
    

            
    if 'user' in session and 'comp' in session:
        if int(session['comp'])== int(session['user']):
            session['display'] ='Great you win!!'
            
        if int(session['comp']) > int(session['user']):
            session['display'] = 'Too low!!'
        if int(session['comp']) < int(session['user']):
            session['display'] = 'Too High!!'
        
    return render_template('index.html')
@app.route('/play', methods=["POST"])
def play():    
    if request.form["user"] == "":
        return redirect("/")
    if "comp" not in session:
        session['comp'] = random.randrange(1,50)
        print(session['comp'])
    session['user'] = int(request.form ['user'])
    print(session['user'])
        
    
    return redirect("/" )
# @app.route("/clear")
# def clear():
#     session.clear()
#     return redirect("/")
if __name__=="__main__":
    app.run(debug=True)