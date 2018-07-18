from django.shortcuts import render
from myApp.forms import SurveyForm,QuestionInlineFormSet

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
# from myApp.forms import PersonForm
# from myApp.models import Person
from django.contrib.auth.decorators import login_required
from .models import Survey,Question

@login_required
def home(request):
	form = SurveyForm()
	survey = Survey()
	formset = QuestionInlineFormSet(instance=survey) 
	if request.method == 'POST':
		form = SurveyForm(request.POST)
		if form.is_valid() :
			sv = form.save(commit=False)
			formset = QuestionInlineFormSet(request.POST,instance=sv)
			if formset.is_valid():
				sv.save()
				formset.save()

	return render(request, 'home.html', {
		'form': form,
		'formset' : formset
	})
	# return render(request,'home.html')

# def submit_cre_survey(request):
	# if request.method == 'POST':
	# 	form = SurveyForm(request.POST)
	# if form.is_valid():
	# 	survey = form.save(commit=False)
	# 	survey.save()
	# else:
	# 	form = SurveyForm()
	# return render(request, 'home.html', {'form': form})
	# name = request.POST["topic"]
	# des = request.POST["description"]
	# sh = request.POST["questionS"]
	# lo = request.POST["questionL"]
	# survey_info = Survey(name=name,description=des,text=sh)
	# survey_info.save()
	# return render(request,'home.html')

def answer(request):
	return render(request,'answer.html')

# class CreatePersonView(CreateView):
# 	# queryset = Person()
# 	template_name='person.html'
# 	form_class = PersonForm
# 	success_url = '/home'

def main(request):
	return render(request,'main.html')

def feedback(request):
	return render(request,'feedback.html')

def success(request):
	return render(request,'success.html')
