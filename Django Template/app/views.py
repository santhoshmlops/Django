from django.shortcuts import render

# Create your views here.
def Indexview(request):
    return render(request,"app/forms.html")