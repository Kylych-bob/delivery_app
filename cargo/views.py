from django.shortcuts import render
from geopy.distance import geodesic
from cargo.models import Price, Weight
from django.http import HttpResponse
from django.views.generic import ListView



def index(request):
    return render(request, 'cargo/input.html')



def dist(request):
    
    # Пользователь вводит Координаты/из базы извлекается цена
    a1 = request.POST['a1']
    a2 = request.POST['a2']
    b1 = request.POST['b1']
    b2 = request.POST['b2']
    weight_c = int(request.POST['c'])
    price_d = Price.objects.get(pk=1)
    price_d = price_d.money
    
    # Вычесление расстояния
    point_a = (a1,a2)
    point_b = (b1,b2)

    distance = int(geodesic(point_a, point_b).miles)
    
    # Вычесление суммы за определнное расстояние
    distance_price = distance * price_d
    weight_price = weight_c * price_d

    summ_price = distance_price + weight_price

    return render(request, 'cargo/result.html', {'result': summ_price, 'distance': distance})
 
