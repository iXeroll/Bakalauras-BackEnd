from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


def upload_to(instance, filename):
    return "posts/{filename}".format(filename=filename)


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="active").order_by("-id")

    statusOptions = (("active", "Active"), ("inactive", "Inactive"))

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, default="posts/default.jpg")
    creationDate = models.DateField(default=timezone.now)
    updateDate = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=statusOptions, default="active")
    price = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title


class Order(models.Model):

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="buyer"
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seller"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=250)
    price = models.PositiveIntegerField(default=0)
    creationDate = models.DateField(default=timezone.now)
    completionDate = models.DateField(null=True)

    objects = models.Manager()
