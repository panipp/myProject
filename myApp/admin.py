from django.contrib import admin

from myApp.models import Survey, Question, Answer, Response

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	inlines = [QuestionInline]

class AnswerBaseInline(admin.StackedInline):
    fields = ('question', 'body')
    readonly_fields = ('question',)
    extra = 0
    model = Answer

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('survey', 'created', 'user')
    list_filter = ('survey', 'created')
    date_hierarchy = 'created'
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = (
        'survey', 'created', 'updated','user'
    )


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)

# Register your models here.
# from myApp.models import Person
# class PersonAdmin(admin.ModelAdmin):
# 	list_display=[f.name for f in Person._meta.fields]
# admin.site.register(Person,PersonAdmin)