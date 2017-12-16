from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager


class Image(models.Model):
    """Image model."""

    cover = models.URLField(max_length=512, blank=True, null=True)
    thumbnail = models.URLField(max_length=512, blank=True, null=True)
    static = models.ImageField(upload_to='photo', blank=True, verbose_name="photo")

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = 'image'

    def get_cover(self):
        if self.static:
            return "".join([settings.STATIC_URL, "media/", str(self.static)])
        else:
            return self.cover

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail
        elif self.cover:
            return self.cover
        else:
            return "".join([settings.STATIC_URL, "media/", str(self.static)])

    def __str__(self):
        return self.get_thumbnail()


class Blog(models.Model):
    """blog model"""
    title = models.CharField(max_length=200)
    web_url = models.URLField(max_length=512, blank=True, null=True, verbose_name="facebook link")
    source = models.CharField(blank=True, max_length=50, null=True)
    referrer = models.URLField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    on_home_page = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')
        db_table = 'blogs'

    def __str__(self):
        return self.title

    tags = TaggableManager(blank=True)
