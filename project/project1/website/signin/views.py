from django.shortcuts import render

# Create your views here.
import mysql.connector as sql
u=''
p=''
def signin(request):
    global u,p
    if request.method=="POST":
        mycon= sql.connect(host="localhost" , user="root" , password="12345678" , database="hubnet")
        mycur=mycon.cursor()
        d=request.POST
        for key,values in d.items():
            if(key=="email"):
                u=values
            if(key=="pas"):
                p=values
        q="select * from student where email='{}' and password='{}'".format(u,p)
        mycur.execute(q)
        data=tuple(mycur.fetchall())
        if data==():
            return render (request, "error.html")
        else:
            return render (request, "welcome.html")
    return render(request, "signin.html")


