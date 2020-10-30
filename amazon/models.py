from django.db import models
from django.http import Http404
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import ObjectDoesNotExist



# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to = 'postmalone/')


    def save_profile(self):
        self.save()


     def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio


# Project class
class Projects(models.Model):
    project_title = models.CharField(max_length=300)
    project_image = models.ImageField(upload_to = 'givenofucks/')
    project_description = models.TextField()
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    owner_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
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
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'




