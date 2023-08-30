from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app1.models import Teacher
import csv
def index(request):
    if len(Teacher.objects.all())==0:
            file0=open("E:\Project\pythonProject4\work2\info1.txt","r",encoding='utf-8')
            lines=file0.readlines()
            t=0
            for line in lines:
                t+=1
                list=line.rstrip().split(",")

                Teacher.objects.create(name=list[1],tittle=list[2],department=list[0],photo=list[3])

    ls=Teacher.objects.all()
    context={"teachers_list":ls}
    return render(request,"index.html",context)
    #return HttpResponse("hello world")

def searchName(request):
    name =request.POST["dname"]
    list=Teacher.objects.filter(name=name)
    #print(list)
    context = {"teachers_list": list}
    return render(request, "search.html", context)






#def user_list(request):
    #return render(request,"user_list.html")

#def req(request):
    #print(request.method)
    #return HttpResponse("re")