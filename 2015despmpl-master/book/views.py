from django.shortcuts import render
from book.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
       # create an object and save to database
       Item.objects.create(name=request.POST['name_text'], number=request.POST['number_text'])

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def add_item(name, number):
    pass

def search_item(name, number):
    if Item.objects.create(name=request.POST['name_text'])
    	items = Item.objects.get(item.name=['name_text'])

   	return render(request, 'home.html', {'items': items})

   	if Item.objects.create(number=request.POST['number_text'])
    	items = Item.objects.get(item.number=['number_text'])

   	return render(request, 'home.html', {'items': items})
