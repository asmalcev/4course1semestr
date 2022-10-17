from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from .models import News



def home(req):
	news = News.objects.all().order_by('-publication_date')

	return render(req, 'index.html', { 'news': news })

def news(req, id):
	news = News.objects.get(id=id)

	return render(req, 'index.html', { 'news': [news], 'newspage': True })

def http404(req):
	return render(req, '404.html')

def search(req):
	srequest = req.GET.get('srequest', '')

	news = News.objects.all() \
		.filter(Q(title__iregex=srequest) | Q(content__iregex=srequest)) \
		.order_by('-publication_date')

	return render(req, 'index.html', { 'news': news, 'srequest': srequest })