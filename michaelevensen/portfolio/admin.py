from django import forms
from django.contrib import admin
from portfolio.models import Case, Chapter, Article
from django_summernote.admin import SummernoteModelAdmin

class CaseAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'slug' )
	prepopulated_fields = {"slug": ("title",)}

class ChapterAdmin(SummernoteModelAdmin):
    list_display = ( 'title', 'case', 'id' )
    prepopulated_fields = {"slug": ("title",)}

class ArticleAdmin(SummernoteModelAdmin):
	list_display = ( 'title', 'slug', 'id' )
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Case, CaseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Article, ArticleAdmin)