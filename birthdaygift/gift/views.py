from django.shortcuts import render,HttpResponse
from .models import Records
# Create your views here.
def index(request):

    return render(request,"index.html")
def gotolink(request,sender,receiver):
    if request.method=="GET":

        R=Records.objects.filter(Sender=sender).filter(Receiver=receiver).first()
        if R:
            return render(request,"index.html",{"Hint":R.Hint,"Sender":sender,"Receiver":receiver})
        else:
            return HttpResponse("your link is dead or dosenot exists")
    if request.method=="POST":
        R=Records.objects.filter(Sender=sender).filter(Receiver=receiver).first()
        if request.POST.get("Password", "")==R.Password:
            return render(request,"gift.html")
        else:
            return render(request,"index.html",{"Hint":R.Hint,"Sender":sender,"Receiver":receiver,"try":"Wrong Pasword try again"})

def generatelink(request):
    if request.method=="GET":
        return render(request,"generatelink.html")
    if request.method=="POST":
        Sender=request.POST.get("Sender", "")
        Receiver=request.POST.get("Receiver", "")
        Hint=request.POST.get("Hint", "")
        Password=request.POST.get("Password", "")
        q = Records(Sender=Sender,Receiver=Receiver,Hint=Hint,Password=Password)
        q.save()
        return render(request,"yourlink.html",{"Sender":Sender,"Receiver":Receiver})


