from django.template import loader
from django.http import HttpResponse
from .models import Member


# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))    


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'firstname': 'Linus',
        'greeting': 5,
    }
    return HttpResponse(template.render(context, request))


def testing2(request):  # For Querysets section
    mydata = Member.objects.all()
    
    ### The values() Method allows return each object as a python dictionary.
    # mydata = Member.objects.all().values()
    
    ### esta linea devuelve <QuerySet [('Emil',), ('Tobias',), ('Linus',), ('Lene',), ('Stalikken',)]>
    # mydata = Member.objects.values_list("firstname")  
    
    ### Return Specific Rows using filter
    # mydata = Member.objects.filter(firstname='Emil').values()

    template = loader.get_template('template2.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
