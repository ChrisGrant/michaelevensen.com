from django import forms
from django.contrib import admin
from portfolio.models import Case, Chapter, Article
# from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CaseAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'slug' )
	prepopulated_fields = {"slug": ("title",)}

class ChapterForm(forms.ModelForm):
    body = forms.CharField( widget=SummernoteInplaceWidget() )

    class Meta:
    	model = Chapter
        fields = ['title', 'introduction', 'body', 'slug', 'case']

class ChapterAdmin(admin.ModelAdmin):
    form = ChapterForm
    list_display = ( 'title', 'case', 'id' )
    prepopulated_fields = {"slug": ("title",)}

class ArticleAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'slug', 'id' )
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Case, CaseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Article, ArticleAdmin)