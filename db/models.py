from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    # Admin Owner
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class RepoLink(models.Model):
    # Admin Owner
    link = models.CharField(max_length=100)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,
                             related_name='repo_links')


class Article(models.Model):
    # Admin Owner
    title = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    text = models.TextField()
    creation_date = models.DateTimeField()
    publication_date = models.DateTimeField(null=True)
    creator = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                related_name='created_articles')
    tags = models.ManyToManyField('Tag', related_name='articles')
    authors = models.ManyToManyField('Profile', related_name='articles')


class Tag(models.Model):
    # Admin Owner
    name = models.CharField(max_length=50)


class File(models.Model):
    # Admin
    creation_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,
                             related_name='files')
    article = models.ForeignKey('Article', on_delete=models.CASCADE,
                                related_name='files')


class HardwareRental(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,
                             related_name='rentals')
    hardware = models.ForeignKey('Hardware', on_delete=models.CASCADE,
                                 related_name='rentals')
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)


class Hardware(models.Model):
    name = models.TextField()
    description = models.TextField()
    serial_number = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creation_date = models.DateTimeField()
    publication_date = models.DateTimeField(null=True)
    repository_link = models.CharField(null=True, blank=True, max_length=100)
    creator = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                related_name='created_projects')
    section = models.ForeignKey('Section', on_delete=models.CASCADE,
                                related_name='projects', null=True)

    authors = models.ManyToManyField('Profile', related_name='projects')


class Section(models.Model):
    name = models.TextField()
    description = models.TextField()
    isVisible = models.BooleanField()
    icon = models.TextField(null=True, blank=True)


class Gallery(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE,
                                related_name='gallery')
    image = models.ImageField(upload_to='gallery/')
