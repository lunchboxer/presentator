from django.contrib import admin
from presentor.models import Presentation, Poll, Choice, Answer


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'poll')


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('choice', 'poll', 'user', 'created')

admin.site.register(Presentation)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
