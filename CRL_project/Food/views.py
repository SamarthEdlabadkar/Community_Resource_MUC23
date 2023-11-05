from django.shortcuts import get_object_or_404, render
from .models import Food_Places, Resources

# Create your views here.
def main_home(request):
    places = Resources.objects.all()
    return render(request, 'home.html',context={'places': places})

def home(request,**kwargs):
    if kwargs!= {}:
        match (kwargs['service']):
            case 'Food Services':
                retail_places = Food_Places.objects.all().filter(category__iexact='Retail')
                meal_exchange_places = Food_Places.objects.all().filter(category__iexact='Meal Exchange')
                meal_plan_places = Food_Places.objects.all().filter(category__iexact='Meal Plan')
                context = {'retail_places':retail_places,'meal_exchange_places':meal_exchange_places,'meal_plan_places':meal_plan_places} 
    return render(request,'food_home.html',context)


def detail(request, **kwargs):
    place = Food_Places.objects.values().filter(name=kwargs['name']).filter(category=kwargs['category'])
    context = [a for a  in place][0]
    
    return render(request,'detail.html', context=context)