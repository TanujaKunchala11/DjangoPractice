from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hello(request):
    return HttpResponse("<h1 align='center'>Hello World</h1>")
def Sample(request):
    return HttpResponse("<h2 style=color:green;background-color:yellow;font-size:45px><center>Django Internship</center></h2>")
def dyn(request,id):
    return HttpResponse("<h2><center>My Rollnumber is:{}</center></h2>".format(id))
def name(request,name):
    return HttpResponse("<h1 style=color:navy;background-color:green;font-style:italic><center>My Name is :{}</center></h1>".format(name))
def task(request,id,name):
    return HttpResponse("<h2><center>my rollnumber is:{} and my name is:{}</center></h2>".format(id,name))
def table(request):
    return render(request,'table.html',{})
def details(request,id,name):
    return render(request,'details.html',{'i':id,'n':name})
def external(request):
    if request.method == "POST":
        na=request.POST['uname']
        mb=request.POST['mbl']
        em=request.POST['eml']
        ps=request.POST['psw']
        cps=request.POST['cpsw']
        return render(request,'data.html',{'n':na,'m':mb,'e':em,'p':ps,'cp':cps})
    return render(request,'external.html')
def boot(request):
	return render(request,'boot.html')