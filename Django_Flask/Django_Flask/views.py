from django.shortcuts import render
from urllib import request as req
import json

def home(request):
    return render(request,"index.html")


def allfilmsrest(request):
    # this api response from mongodb cloud atlas database 
    response = req.urlopen("http://127.0.0.1:7000/films/all")
    data = response.read()
    info = json.loads(data)
    context = {'info': info}
    return render(request, "Showallfilms.html", context)

def allaccrest(request):
    # this api response from mysql cloud aws database 
    response = req.urlopen("http://127.0.0.1:5000/accounts/alldata")
    data = response.read()
    info = json.loads(data)
    context = {'info': info}
    return render(request, "Showallacc.html", context)

def searchaccno(request):
    if request.method=="POST":
        ano=request.POST.get("accno")
        response = req.urlopen("http://127.0.0.1:6000/accounts/accno/"+ano)
        data = response.read()
        info = json.loads(data)
        context = {'info': info}
    return render(request,"showAccInfo.html",context)
