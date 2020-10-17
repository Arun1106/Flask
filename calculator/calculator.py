from flask import Flask,redirect,url_for,request
app=Flask(__name__)
@app.route('/operations/<name>/<int:x>/<int:y>')
def operations(name,x,y):
    if name=='+':
        z=x+y
    elif name=='-':
        z=x-y
    elif name=='*':
        z=x*y
    else:
        z=x/y
    return 'result %d' %z
        
@app.route('/calculator',methods=['POST','GET'])
def new_user():
    if request.method=="POST":
        x1=request.form['name1']
        x2=request.form['name2']
        x3=request.form['name3']
        return redirect(url_for('operations',name=x3,x=x1,y=x2))
        
        
    
    
if __name__=="__main__":
    app.run()
