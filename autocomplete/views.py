from django.http import HttpResponse
from django.utils import simplejson as json
from tagging.models import Tag
from django.db.models import get_model

from target.models import Product,Company
from geography.models import Location

def main_search(request):
    try:
        query = request.GET['q']
    except KeyError:
        return HttpResponse("No query string", mimetype='text/plain')
    products = Product.objects.filter(name__istartswith=query)
    companies = Company.objects.filter(name__istartswith=query)
    locations = Location.objects.filter(name__istartswith=query)
    
    r = []
    r.append("<div class='ac_header'>Companies</div>")
    for c in companies:
        r.append("%s|%s" % (c.name,c.get_absolute_url()))
    r.append("<div class='ac_header'>Products</div>")
    for p in products:
        r.append("%s|%s" % (p.name,p.get_absolute_url()))
    r.append("<div class='ac_header'>Locations</div>")
    for l in locations:
        r.append("%s|%s" % (l.name,"")) #l.get_absolute_url()))
    return HttpResponse('\n'.join(r), mimetype='text/plain')
    
def list_objects(request,model):
    '''Query the objects saved for a particular model'''
    try:
        (app_label,model_name) = model.split(".")
    except ValueError:
        return HttpResponse('Need full model name with app prefix')
    model_class = get_model(app_label,model_name)
    #check for abstract
    #find subclasses
    
    if model_class == None:
        return HttpResponse('Model "%s.%s" does not exist' % (app_label,model_name))
    try:
        query = request.GET['q']
    except KeyError:
        return HttpResponse("No query string", mimetype='text/plain')
    objects = model_class.objects.filter(name__istartswith=query).values_list('name', flat=True)
    return HttpResponse('\n'.join(objects), mimetype='text/plain')
    
def list_fields(request,model_name):
    '''List the fields available for a particular model'''
    try:
        (app_label,model_name) = model.split(".")
    except ValueError:
        return HttpResponse('Need full model name with app prefix')
    model_class = get_model(app_label,model_name)
    model_fields = model_class._meta._fields() #uses internal api, but should continue to work
    model_fields.pop(0) #drop the pk
    response = []
    for f in model_fields:
        response.append(f.name)
    return HttpResponse('\n'.join(response))