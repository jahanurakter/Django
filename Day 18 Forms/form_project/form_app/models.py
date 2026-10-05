from django.db import models

class BlogModel(models.Model):
    title=models.CharField(max_length=150,null=True)
    author_name=models.CharField(max_length=150,null=True)
    content=models.TextField(null=True)
    blog_image=models.ImageField(upload_to='media/blog_image', null=True)
    publish_date=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.author_name}"