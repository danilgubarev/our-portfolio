from django.shortcuts import render

# Create your views here.
def show_hobbi(request):
    return render(request,"hobbi/hobbi.html")