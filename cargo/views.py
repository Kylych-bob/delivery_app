from django.shortcuts import render
from geopy.distance import geodesic


from django.http import HttpResponse



def index(request):
    return HttpResponse('page found')




def dist(request):
    
    a1 = request.GET.get('a1')
    a2 = request.GET.get('a2')
    b1 = request.GET.get('b1')
    b2 = request.POST.get('b2')

   
    # b2 = request.POST.get('num1')


    print(a1,a2, b1,b2)
    point_a = (a1,a2)
    point_b = (b1,b2)

    res = geodesic(point_a, point_b).miles




    # a = int(num1)
    # b = int(num2)
    # res = a1 + b1
    # print(res)
    print(type(res))
    return render(request, 'cargo/result.html', {'result': res})
 
