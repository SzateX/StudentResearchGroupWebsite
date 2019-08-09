from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm


def assign_permissions_to_instance(permissions: list, user, instance):
    for permission in permissions:
        assign_perm(permission, user, instance)


def assign_all_perms_to_creator_and_staff(instance):
    permissions = ["%s_%s" % (perm, type(instance).__name__.lower()) for perm in ["add", "change", "delete", "view"]]
    assign_permissions_to_instance(permissions, instance.creator, instance)
    for user in User.objects.filter(is_staff=True):
        assign_permissions_to_instance(permissions, user, instance)


def assign_all_perms_to_staff(instance):
    permissions = ["%s_%s" % (perm, type(instance).__name__.lower()) for perm in ["add", "change", "delete", "view"]]
    for user in User.objects.filter(is_staff=True):
        assign_permissions_to_instance(permissions, user, instance)


# Create your models here.
class Profile(models.Model):
    # Admin Owner
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        x = Profile.objects.create(user=instance)
        if not instance.username == "AnonymousUser":
            permissions = [
                "%s_%s" % (perm, type(x).__name__.lower()) for perm in
                ["add", "change", "delete", "view"]]
            assign_permissions_to_instance(permissions, instance, x)
            for user in User.objects.filter(is_staff=True):
                assign_permissions_to_instance(permissions, user, x)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class RepoLink(models.Model):
    # Admin Owner
    link = models.CharField(max_length=100)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,
                             related_name='repo_links')


@receiver(post_save, sender=RepoLink)
def assign_permisions_repo_link(sender, instance: RepoLink, created: bool,
                                **kwargs):
    if created:
        permissions = [
            "%s_%s" % (perm, type(instance).__name__.lower()) for perm in
             ["add", "change", "delete", "view"]]
        assign_permissions_to_instance(permissions, instance.user,
                                       instance)
        for user in User.objects.filter(is_staff=True):
            assign_permissions_to_instance(permissions, user, instance)


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


@receiver(post_save, sender=Article)
def assign_permisions_article(sender, instance: Article, created: bool, **kwargs):
    if created:
        assign_all_perms_to_creator_and_staff(instance)


class Tag(models.Model):
    # Admin
    name = models.CharField(max_length=50)


@receiver(post_save, sender=Tag)
def assign_permisions_tag(sender, instance: Tag, created: bool, **kwargs):
    if created:
        assign_all_perms_to_staff(instance)


class HardwareRental(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,
                             related_name='rentals')
    hardware = models.ForeignKey('Hardware', on_delete=models.CASCADE,
                                 related_name='rentals')
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)


@receiver(post_save, sender=HardwareRental)
def assign_permisions_hardware_rental(sender, instance: HardwareRental, created: bool,
                                  **kwargs):
    if created:
        permissions = [
            "%s_%s" % (perm, type(instance).__name__.lower()) for perm in
             ["add", "change", "delete", "view"]]
        assign_permissions_to_instance(permissions, instance.user, instance)
        for user in User.objects.filter(is_staff=True):
            assign_permissions_to_instance(permissions, user, instance)


class Hardware(models.Model):
    name = models.TextField()
    description = models.TextField()
    serial_number = models.TextField()


@receiver(post_save, sender=Hardware)
def assign_permisions_hardware(sender, instance: Hardware, created: bool, **kwargs):
    if created:
        assign_all_perms_to_staff(instance)
        for user in User.objects.all():
            if user.username is not 'AnonymousUser':
                assign_permissions_to_instance(['view'], user, instance)


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


@receiver(post_save, sender=Project)
def assign_permisions_project(sender, instance: Project, created: bool, **kwargs):
    if created:
        assign_all_perms_to_creator_and_staff(instance)


class Section(models.Model):
    name = models.TextField()
    description = models.TextField()
    isVisible = models.BooleanField()
    icon = models.TextField(null=True, blank=True)


@receiver(post_save, sender=Section)
def assign_permisions_section(sender, instance: Section, created: bool, **kwargs):
    if created:
        assign_all_perms_to_staff(instance)


class Gallery(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE,
                                related_name='gallery')
    image = models.ImageField(upload_to='gallery/')
    creator = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                related_name='created_gallery_entity')


@receiver(post_save, sender=Gallery)
def assign_permisions_gallery(sender, instance: Gallery, created: bool, **kwargs):
    if created:
        assign_all_perms_to_creator_and_staff(instance)
