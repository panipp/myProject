from django.shortcuts import render
from myApp.forms import SurveyForm,QuestionInlineFormSet,ResponseForm

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Survey,Question
from django.views.generic import TemplateView,View

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render



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

def main(request):
	return render(request,'main.html')

def feedback(request):
	return render(request,'feedback.html')

def success(request):
	return render(request,'success.html')

class SurveyView(TemplateView):
	template_name = "main.html"

	def get_context_data(self, **kwargs):
		context = super(SurveyView, self).get_context_data(**kwargs)
		surveys = Survey.objects.all()
		context['surveys'] = surveys
		return context

class SurveyDetail(View):

    def get(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey,id=kwargs['id'])
        template_name = 'answer.html'
        questions = Question.objects.filter(survey=survey)
        form = ResponseForm(survey=survey, user=request.user,
                            step=kwargs.get('step', 0))
        context = {
            'response_form': form,
            'survey': survey,
            'questions': questions,
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, id=kwargs['id'])
        questions = Question.objects.filter(survey=survey)
        form = ResponseForm(request.POST, survey=survey, user=request.user,
                            step=kwargs.get('step', 0))
        context = {'response_form': form, 'survey': survey,
                   'questions': questions}
        if form.is_valid():
            session_key = 'survey_%s' % (kwargs['id'],)
            if session_key not in request.session:
                request.session[session_key] = {}
            for key, value in form.cleaned_data.items():
                request.session[session_key][key] = value
                request.session.modified = True

            next_url = form.next_step_url()
            response = None
        
            if not form.has_next_step():
                save_form = ResponseForm(request.session[session_key],
                                            survey=survey, user=request.user)
                response = save_form.save()
           
            response = form.save()

            if next_url is not None:
                return redirect(next_url)
            else:
                del request.session[session_key]
                if response is None:
                    return redirect('/')
                else:
                    next_ = request.session.get('next', None)
                    if next_ is not None:
                        if 'next' in request.session:
                            del request.session['next']
                            print("yes")
                        return redirect(next_)
                    else:
                        return redirect('survey-confirmation')

            template_name = 'answer.html'
        return render(request, template_name, context)

class ConfirmView(TemplateView):

    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        return context
