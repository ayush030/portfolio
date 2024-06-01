from django.db import models

from django.utils import timezone

# Introduction : model to display content for home page
# Footer : model for Home page footer


class Introduction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # display name
    name = models.CharField(max_length=20, default='Ayush Tripathi')

    # field to add 2-3 lines about oneself
    brief_intro = models.TextField()

    # path to profile picture displayed on home page
    profile_picture_path = models.FilePathField(path="/home/ayush/projects/python/portfolio/static", allow_folders=True)

    # banner picture path displayed on home page
    banner_picture_path = models.FilePathField(path="/home/ayush/projects/python/portfolio/static", allow_folders=True)

    # field to display description about oneself on home page
    paragraph_description = models.TextField()

    def __str__(self):
        return "Portfolio home page of " + self.name.__str__()


class Footer(models.Model):
    def __str__(self):
        return "Home page footer"

    message = models.CharField(max_length=50)
