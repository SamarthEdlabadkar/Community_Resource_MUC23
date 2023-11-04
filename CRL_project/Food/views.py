from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def locations(request):
    return render(request, 'location.html')

def retail(request):
    return render(request,'retail.html')

def meal_plan(request):
    return render(request,'meal_plan.html')

def meal_exchange(request):
    return render(request,'meal_exchange.html')