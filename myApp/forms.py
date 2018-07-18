from django.forms import ModelForm,modelformset_factory,inlineformset_factory
from myApp.models import Survey,Question
from django.utils.translation import ugettext_lazy as _

class SurveyForm(ModelForm):
    class Meta(object):
        model = Survey
        fields = '__all__'
        # labels = {
        #     'name': _("ชื่อแบบฟอร์ม"),
        #     'description': _("คำอธิบาย")
        # }

class QuestionForm(ModelForm):
    class Meta(object):
        model = Question
        fields="__all__"

# QuestionFormSet = modelformset_factory(
#     model = Question,
#     form = QuestionForm,
#     extra=2,
# )

QuestionInlineFormSet = inlineformset_factory(
    parent_model = Survey,
    model = Question,
    extra = 0,
    fields = "__all__",
    # formset=QuestionFormSet,
    min_num=1,
)