from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'SOFIYA','age':10}
    return render(request,'jinga.html',context=d)    