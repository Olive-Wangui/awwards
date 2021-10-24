from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=200)
    contact = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    image = models.ImageField(upload_to='projects/', null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1500, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(tag, blank=True)
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    caption = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    date_posted = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    
    def __str__(self):
        return self.comment
    
class Ratings(models.Model):
    RATING_CHOICES   = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    design_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    usability = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    
    def __str__(self):
        return self.author
    