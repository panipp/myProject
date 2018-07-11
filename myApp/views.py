from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from myApp.forms import PersonForm
from myApp.models import Person
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'home.html')

def answer(request):
	return render(request,'answer.html')

class CreatePersonView(CreateView):
	# queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/home'

def main(request):
	return render(request,'main.html')

def feedback(request):
	return render(request,'feedback.html')

def success(request):
	return render(request,'success.html')
	