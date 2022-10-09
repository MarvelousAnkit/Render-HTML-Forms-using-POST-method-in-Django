from django.shortcuts import render

# Create your views here.
import mysql.connector as sql
u=''
p=''
def signup(request):
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
        q="insert into student values('{}' , '{}')".format(u,p)
        mycur.execute(q)
        mycon.commit()
    return render(request, "signup.html")


