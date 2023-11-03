from flask import Flask,render_template,request
import pymysql


app=Flask(__name__)
conn=pymysql.connect(host='localhost',user='root')


@app.route('/',methods=['POST','GET'])
def form():
    row=""
    p=""
    f=""  
    query=""
    if request.method=='POST':
        query=request.form.get("query") 
        
#___________________creating database ______________________
    
        if ("create database" in query) or ("CREATE DATABASE" in query):
            with conn.cursor() as cur:
                cur.execute(query)
                row=cur.fetchall()
                conn.commit()
                print(row)
            return render_template("query.html",type="create database",data=row)
        
#_______________ switching to database query ____________________
        
        elif ("use" in query) or ("USE" in query):
            with conn.cursor() as cur:
                row=cur.execute(query)
                conn.commit()
            return render_template("query.html",type="use",data=query)
        
#_______________ select query ____________________
        
        elif ("select" in query) or ("SELECT" in query):
            with conn.cursor() as cur:
                cur.execute(query)
                row=cur.fetchall()
                print(row)
            return render_template("query.html",type="select",data=row)
        
#_______________ describe query ____________________
        
        elif ("describe" in query) or ("DESCRIBE" in query):
            with conn.cursor() as cur:
                r=cur.execute(query)
                p=cur.fetchall()
                print(p)
            return render_template("query.html",type="describe",data=p)
        
#_______________ delete query ____________________
        
        elif ("delete" in query) or ("DELETE" in query):
            with conn.cursor() as cur:
                cur.execute(query)
                print("delete query ran")
                return render_template("query.html",type="show",data=row)

                
#_______________ show query ____________________

        elif ("show" in query) or ("SHOW" in query):
            with conn.cursor() as cur:
                cur.execute(query)
                row=cur.fetchall()
                print("------------")
                print(row)
                print(type(row))
            return render_template("query.html",type="show",data=row)
        
#_______________ drop table query ____________________
        
        elif ("drop" in query) or ("DROP" in query):
            with conn.cursor() as cur:
                cur.execute(query)
                row=cur.fetchall()
                conn.commit()
                print(row)
                print("table dropped")
            return render_template("query.html",type="drop",data=row)
        
#_______________ create table query ____________________
        
        elif ("create table" in query) or ("CREATE TABLE" in query):
            with conn.cursor() as cur:
                cur.execute(query)
                data=cur.fetchall()
                conn.commit()
            with conn.cursor() as cur:
                describe="describe table %s"
                cur.execute
            return render_template("query.html",type="create table",data=data)
        
                
        else:
            with conn.cursor() as cur:
                cur.execute(query)
                f=cur.fetchall()
                print(f)
                print(request)
        return render_template("query.html",f=f)

    return render_template("query.html")
    
            
    
if __name__=="__main__":
    app.run(debug=True)
