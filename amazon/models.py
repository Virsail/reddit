from django.db import models
from django.http import Http404
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.db.models import ObjectDoesNotExist



# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(default='default.jpg', upload_to = 'postmalone/')
    contact = models.EmailField(max_length=100, blank=True)
    name = models.CharField(blank=True, max_length=100)


    def save_profile(self):
        self.save()

       

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio

    

# Project class
class Projects(models.Model):
    project_title = models.CharField(max_length=300)
    project_image = models.ImageField(default='default.jpg', upload_to = 'givenofucks/')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    link = models.URLField()
    

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
        
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    
    @classmethod
    def get_by_owner(cls, Owner):
        projects = cls.objects.filter(Owner=Owner)
        return projects
    
    
    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.project_title
    
    class Meta:
        ordering = ['-pub_date']

class Review(models.Model):
    review = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    design = models.IntegerField(choices=review, default=0, blank=True)
    usability = models.IntegerField(choices=review, blank=True)
    content = models.IntegerField(choices=review, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviewer')
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='reviews', null=True)

    def save_review(self):
        self.save()

    @classmethod
    def get_review(cls, id):
        reviews = Review.objects.filter(project_id=id).all()
        return reviews

    
    def __str__(self):
        return self.project(Review)
    
