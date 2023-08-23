from flask import Flask,request,jsonify
import mysql.connector as conn
mydb = conn.connect(host = 'localhost',user = 'root',passwd = 'Letsgo1247')
cursor = mydb.cursor(dictionary=True)
# cursor.execute("select * from ineuron.attribute")
# for i in cursor.fetchall():
#     print(i)

# cursor.execute("use ineuron")
# cursor.execute("select * from attribute")
# for i in cursor.fetchall():
#     print(i)
app = Flask(__name__)
@app.route('/testfun')
def test():
    get_name = request.args.get("get_name")
    mobile_number  = request.args.get("mobile")
    mail_id = request.args.get('mail_id')
    return "this is my first function for get {} {} {}".format(get_name,mobile_number,mail_id)

@app.route('/test1fun')
def test1():
    l=[]
    get_db_name = request.args.get('database')
    get_table_name = request.args.get('table')
    cursor.execute(f"use {get_db_name}")
    cursor.execute(f"select * from {get_table_name}")
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))



if __name__=='__main__':
    app.run(port = 5002)

