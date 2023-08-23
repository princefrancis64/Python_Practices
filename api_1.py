from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/abc',methods = ['GET','POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

@app.route('/abc1/prince',methods = ['GET','POST'])
def test2():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify((str(result)))

@app.route('/abc2/prince',methods = ['GET','POST'])
def test3():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify((str(result)))

if __name__=='__main__':
    app.run()



def test(a,b):
    return a+b


1.write a program to insert a record in sql table via api database
2.write a program to update a record via api
3.write a program to delete a record via api
4.write a program to fetch a record via api
5.All the above question you have to answer for mongodb as well