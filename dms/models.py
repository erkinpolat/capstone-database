from django.db import models
from django.utils.text import slugify
from django.urls import reverse

'''
Professors
Students
Alumni (a way to get the students to move to alumni every year)
'''

class StudentJunior(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	collegeMajor = models.CharField(max_length=50)
	primaryConc = models.CharField(max_length=100)
	secondMajor = models.CharField(max_length=50, blank=True)
	secondConc = models.CharField(max_length=50, blank=True)
	customConc = models.CharField(max_length=100, blank=True)
	minor = models.CharField(max_length=50, blank=True)
	minorConc = models.CharField(max_length=50, blank=True)
	knowledge2Offer = models.TextField()
	knowledge2Request = models.TextField()
	section = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	topProjectIdea = models.TextField()
	degreeCommitment = models.CharField(max_length=100)
	projectFeatures = models.TextField()
	otherProjectIdeas = models.TextField(blank=True)
	externalDependencies = models.TextField(blank=True)
	hsrReview = models.TextField(blank=True)
	relevantSkills = models.TextField(blank=True)
	slug = models.SlugField(max_length=200, blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	def save(self, *args, **kwargs):
		'''
		Upon saving a slug is created
		'''
		if not self.slug:
			self.slug = slugify(self.first_name + self.last_name)
		super().save(*args, **kwargs)






