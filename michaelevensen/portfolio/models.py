from django.db import models

# case
class Case(models.Model):
	title = models.CharField('Title', max_length=200)
	introduction = models.TextField('Introduction', blank=False, max_length=200)
	link_text = models.CharField('Link Text', max_length=200)
	slug = models.SlugField()
	image = models.FileField('Image', upload_to='media/', blank=True, null=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

# chapters
class Chapter(models.Model):
	title = models.CharField('Title', max_length=200)
	introduction = models.TextField('Introduction', blank=False, max_length=200)
	body = models.TextField('Body Text', blank=True)
	slug = models.SlugField()
	case = models.ForeignKey(Case, verbose_name="Associated Case")

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

# article
class Article(models.Model):
	title = models.CharField(max_length=200)
	introduction = models.TextField('Introduction', blank=False)
	body = models.TextField('Body Text', blank=True)
	link_text = models.CharField('Link Text', max_length=200)
	slug = models.SlugField()
	
	def __unicode__(self):
		return self.title

