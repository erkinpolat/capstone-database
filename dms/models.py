from django.db import models
from django.utils.text import slugify
from django.urls import reverse

'''
Professors
Students
Alumni (a way to get the students to move to alumni every year)
'''

class StudentJunior(models.Model):
	timestamp = models.CharField(max_length=200)
	email = models.EmailField()
	name = models.CharField(max_length=200)
	collegeMajor = models.CharField(max_length=50, blank=True)
	primaryConc = models.CharField(max_length=100, blank=True)
	secondMajor = models.CharField(max_length=50, blank=True)
	secondConc = models.CharField(max_length=50, blank=True)
	customConc = models.CharField(max_length=100, blank=True)
	minor = models.CharField(max_length=50, blank=True)
	minorConc = models.CharField(max_length=50, blank=True)
	knowledge2Offer = models.TextField(blank=True)
	knowledge2Request = models.TextField(blank=True)
	section = models.CharField(max_length=50, blank=True)
	location = models.CharField(max_length=100, blank=True)
	topProjectIdea = models.TextField(blank=True)
	degreeCommitment = models.CharField(max_length=100, blank=True)
	projectFeatures = models.TextField(blank=True)
	otherProjectIdeas = models.TextField(blank=True)
	externalDependencies = models.TextField(blank=True)
	hsrReview = models.TextField(blank=True)
	relevantSkills = models.TextField(blank=True)
	slug = models.SlugField(max_length=200, blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		'''
		Upon saving a slug is created
		'''
		if not self.slug:
			self.slug = slugify(self.email)
		super().save(*args, **kwargs)

class Faculty(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=200)
	colleges = models.CharField(max_length=200)
	coursesMinerva = models.TextField(blank=True)
	coursesElsewhere = models.TextField(blank=True)
	overviewExpertise = models.TextField(blank=True)
	expertiseKeywords = models.TextField(blank=True)
	additionalInterest = models.TextField(blank=True)
	links = models.TextField(blank=True)
	coursesDomainExpertise = models.TextField(blank=True)
	slug = models.SlugField(max_length=200, blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		'''
		Upon saving a slug is created
		'''
		if not self.slug:
			self.slug = slugify(self.email)
		super().save(*args, **kwargs)





