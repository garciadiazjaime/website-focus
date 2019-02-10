from django.contrib import admin
from survey.models import Question, Answer, Response

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'reg_date', 'active', 'lang')
	search_fields = ['text',]
	list_filter = ['reg_date','active', 'lang']
	inlines = [AnswerInline]

class ResponseAdmin(admin.ModelAdmin):
	list_display = ( 'answer', 'reg_date')
	search_fields = ['answer__value',]
	list_filter = ['reg_date',]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
