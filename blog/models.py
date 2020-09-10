from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    post = models.TextField()
    
    def __unicode__(self):
        return self.title
class Comment(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    def __unicode__(self):
        return (self.post, self.text)