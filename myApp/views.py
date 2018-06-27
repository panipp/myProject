from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from myApp.forms import PersonForm
from myApp.models import Person
def home(request):
    return render(request,'home.html')

def answer(request):
	return render(request,'answer.html')

class CreatePersonView(CreateView):
	# queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/home'

	