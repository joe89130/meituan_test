#_*_coding:utf-8_*_
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponse
from HR import models
from django.template import RequestContext


#上传出差信息函数
'''
def upload(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['business']
    return render(request, "hr.html", ctx)
'''

def upload(request):
    return render_to_response('hr.html')


def index(request):

    template = get_template ('hr.html')

    trips = models.Trip.objects.all()
    directors = models.Director.objects.all()
    citys = models.City.objects.all()


    print('good') 
    #print(trips)
    print('*'*50)
    print(directors)
    print('*'*60)
    print(citys)
    print('*'*70)   
    try:
        urdirector = request.POST.getlist('dire')
        print("负责人取出成功")
        urbusiness = request.POST.get('comment')
        print("出差详情取出成功")   
       # urubusiness = 'I go '
        urcity = request.POST.getlist('cit')
        print("出差城市取出成功")   
    except:
        print('有错误出现了')
        #print(urdirector)
        #print(urcity)
        print('*****************************')
        print(urbusiness)
        urdirector = None 
        urcity = None 
        urbusiness = None
   
    
    #print(urdirector)
    #print(urcity)
    print('*************')
    #print(urbusiness)


    if urbusiness != None :
        director = models.Director.objects.get(name = urdirector[0])
        print(director)
        print(type(director))
        city = models.City.objects.get(city = urcity[0])
        trip = models.Trip.objects.create(director = director,city = city, business = urbusiness)
        trip.save() 
        print('very good')
    '''
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    '''
    html = template.render(locals())

    #return render(request, "hr.html", ctx)
    return HttpResponse(html)

'''
def index(request):
    template = get_template ('hr.html')
    trip = models.Trip.objects.all()
    director = models.Director.objects.all()
    city = models.City.objects.all()
    territory = models.Territory.objects.all()
    html = template.render(locals())

    return HttpResponse(html)
'''
# Create your views here.
