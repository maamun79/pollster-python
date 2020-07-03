from django.contrib import admin

from .models import Question, Choice


# admin.site.register(Question)
# admin.site.register(Choice)

# change default header, title
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster admin area"
admin.site.index_title = "Welcome to Pollster admin area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
