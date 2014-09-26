from django.shortcuts import render
from django.template.response import TemplateResponse
from portfolio.models import Case, Chapter, Article
from django.http import HttpResponse, HttpResponseRedirect

def index(request):

	# cases
	cases = Case.objects.all()

	# articles
	articles = Article.objects.all()

	for case in cases:

		# get first chapter for each case
		chapter = Chapter.objects.filter(case=case).order_by('id')

		# first chapter
		case.first = chapter[0].slug

	return TemplateResponse(request, "portfolio/index.html", { 'cases': cases, 'articles': articles })


def case(request, case=None, chapter=None):

	try:
		current_chapter = Chapter.objects.get(slug=chapter)

	except:
		return HttpResponseRedirect("/")

	# all chapters
	chapters = Chapter.objects.all().order_by('id')

	# chapter numbers
	for index, chapter in enumerate(chapters):
		chapter.number = index + int(1)

		if chapter == current_chapter:
			current_chapter.number = index + int(1)
			
			# if next chapter exists
			try:
				current_chapter.next = Chapter.objects.get(id=chapter.id+int(1))
			except:
				# or don't set it
				current_chapter.next = False

			# set current state for chapter
			chapter.current = True

	return TemplateResponse(request, "portfolio/chapter.html", { 'current_chapter': current_chapter, 'chapters': chapters })


def article(request):
	return HttpResponse("Article")
