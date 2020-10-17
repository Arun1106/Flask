from flask import Flask,redirect,url_for,request
app=Flask(__name__)
@app.route('/login/<name>')
def login(name):
    return'welcome %s' %name
@app.route('/main',methods=['POST','GET'])
def new_user():
    if request.method=="POST":
        user=request.form['name1']
        return redirect(url_for('login',name=user))
        
        
    
    
if __name__=="__main__":
    app.run()
