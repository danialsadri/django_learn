from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="posts", blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title[0:20]

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post_model_view_set-detail", kwargs={"pk": self.id})


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name[0:20]
