from rest_framework import serializers
from .models import Projects, Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_title', 'project_description', 'project_image', 'Owner','link')

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'picture', 'name')
        