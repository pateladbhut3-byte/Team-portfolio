from django.shortcuts import render
from .models import News

def home(request):
    news = News.objects.all()
    return render(request, 'index.html', {'news': news})
# Create your views here.
