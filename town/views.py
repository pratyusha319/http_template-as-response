from django.shortcuts import render

# Create your views here.
def mytown(request):
    return render(request,'mytown.html')