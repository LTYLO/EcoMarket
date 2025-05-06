from django.shortcuts import render


def menu(request):
   return render(request, "main.html")

def login(request):
   return render(request,"login.html" )

def registrer(request):
   return render(request, "sing_in.html" )

