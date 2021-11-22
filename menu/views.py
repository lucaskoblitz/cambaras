from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'menu/home.html')

def p1(request):
	return render(request, 'menu/p1.html')

def p2(request):
	return render(request, 'menu/p2.html')

def p3(request):
	return render(request, 'menu/p3.html')