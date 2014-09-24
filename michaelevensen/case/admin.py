from django.contrib import admin
from case.models import Case, Chapter

class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}

class ChapterAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'case', 'slug' )
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Case, CaseAdmin)
admin.site.register(Chapter, ChapterAdmin)