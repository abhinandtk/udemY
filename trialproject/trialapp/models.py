from django.db import models
import uuid

# Create your models here.
class projects(models.Model):
    Title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    feature_image=models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    tags=models.ManyToManyField('tag',blank=True)
    vote_total=models.IntegerField(default=0,blank=True,null=True)
    vote_ratio=models.IntegerField(default=0,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.Title
    
class review(models.Model):
    VOTE_TYPE=(
        ('up','Upvote'),
               ('down','Downvote')
               )
    project=models.ForeignKey(projects,on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
       return self.value

class tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
       return self.name



