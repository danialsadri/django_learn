from django.db import models


class Post(models.Model):
    """
        this is class to define posts for blog app
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='posts', blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upldated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title[0:20]


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name[0:20]
