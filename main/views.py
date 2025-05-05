from django.shortcuts import render


def saludar(request):
   return render(request, "main.html")

