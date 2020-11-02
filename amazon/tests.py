from django.test import TestCase
from .models import Projects, Profile, Review
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='felixgargado', password='mbocochilo')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_delete_user(self):
        self.user.delete()

    def test_save_user(self):
        self.user.save()

class ProjectsTest(TestCase):
    def setUp(self):
        self.user = User(username='virsail')
        self.project = Projects(project_title='test post',  project_image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', project_description='desc',Owner=self.user, link='http://github.com')

    def test_instance(self):
       #self.assertTrue(isinstance(self.projects, Project))

#   def test_save_project(self):
        self.project.save_project()
#       project = Projects.objects.get_projects
#       self.assertTrue(len(Projects) > 0)

    def test_get_projects(self):
        self.project.save()
       #projects = Projects.search_projects(search_term)
       #self.assertTrue() 

    def test_search_projects(self):
        self.project.save()
#       Projects = Projects.search_projects('test')
#       self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = Projects.search_projects('test')
        self.assertTrue(len(project) < 1)


class ReviewTest(TestCase):
    def setUp(self):
        self.user = User(username='cockroach', id=1)
        self.project = Projects(project_title='Clubing', project_image='https://unsplash.com/photos/bcitHQkoEig',project_description='partyafterparty', Owner =self.user, link='http://github.com/')
        self.review = Review(id=1, design=1, usability=3, content=4, user=self.user, projects=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.review, Review))

    def test_save_review(self):
    #   self.review.save_review()
        review = Review.objects.all()
        self.assertFalse(len(review) > 0)

   
