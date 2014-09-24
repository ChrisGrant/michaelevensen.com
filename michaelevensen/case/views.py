from django.shortcuts import render
from django.template.response import TemplateResponse
from case.models import Case, Chapter

def index(request):

	# cases
	cases = Case.objects.all()

	# associated first chapter
	first_chapters = []

	for case in cases:

		# get first chapter for each case
		chapter = Chapter.objects.filter(case=case).order_by('id')

		first_chapters.append(chapter[0])

	return TemplateResponse(request, "case/index.html", { 'cases': cases })