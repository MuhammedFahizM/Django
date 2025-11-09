from django.db import models

# Create your models here.

class Products(models.Model):
    productname = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=100)
    date = models.DateField()
    image = models.CharField(max_length=500)


class Customer(models.Model):
    cus_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by{self.author} on {self.post}"





