from django.shortcuts import render

# Create your views here.

def show_achievement(request):
    return render(request,"achievement/achievement.html")