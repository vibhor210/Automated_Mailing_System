from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from Email_Sender.settings import EMAIL_HOST_USER

def index(request):
    if request.method =="POST":
        mail = (request.POST.get("mail"))
        subject = request.POST.get("subject")
        msg = request.POST.get("msg")
        send_mail(subject,msg, EMAIL_HOST_USER, mail, fail_silently = False)
        return HttpResponseRedirect("/")

    return render(request,"index.html")