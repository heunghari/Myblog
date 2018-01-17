from django.shortcuts import render, get_object_or_404
from .models import About
# Create your views here.
def about(request):
	content = About()
	return render(request, 'sitepages/about.html', {'content': content})