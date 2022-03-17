from django.db import models
from django.contrib.auth.models import User


class PostList(models.Model):
    CATEGORY_CHOICES = [
        ('FrontEnd', 'FrontEnd'),
        ('BackEnd', 'BackEnd'),
        ('FullStack', 'FullStack'),
    ]
    title = models.CharField(max_length=20)
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, default="FS")
    content = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='post_images', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # @property
    # def get_likes_count(self):
    #     return self.likes.all().count()

    # @property
    # def get_comments_count(self):
    #     return self.comments.all().count()


class Comments(models.Model):
    post = models.ForeignKey(
        PostList, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)


class Likes(models.Model):
    post = models.ForeignKey(
        PostList, on_delete=models.CASCADE, related_name='like')
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
