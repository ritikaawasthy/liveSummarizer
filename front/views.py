from django.shortcuts import render
from django.http import HttpResponse
from summarizer import Summarizer
# Create your views here.
def home(request):
    return render(request,'home.html')

def summarize(request):
    article = request.POST['txt']
    res= bertSummary(article)
    #res="This thing works"
    return render(request,'summarize.html',{'result':res})

def bertSummary(text):
    model = Summarizer()
    return(model(text))
