from django.db import models

class Case(models.Model):
	title = models.CharField('Title', max_length=200)
	intro = models.TextField('Intro', max_length=200)
	link_text = models.CharField('Link Text', max_length=200)
	image = models.FileField('Image', upload_to='media/', blank=True, null=True)
	slug = models.SlugField()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

# class Article(models.Model):
# 	title = models.CharField(max_length=200)
# 	introduction = models.CharField(max_length=200)
# 	link_text = models.CharField('Link Text', max_length=200)
# 	body 
# 	slug = models.SlugField(editable=False) # hide from admin
	
# 	def __unicode__(self):
# 		return self.title

class Chapter(models.Model):
	case = models.ForeignKey(Case)
	title = models.CharField('Title', max_length=200)
	body = models.TextField('Body', blank=True)
	slug = models.SlugField()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title