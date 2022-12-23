from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


def get_file_path(instance, filename):
    """
    Function to get filepath for a file to be uploaded
    Args:
        instance: instance of the file object
        filename: uploaded filename

    Returns:
        path: Path of file
    """
    type = instance.__class__.__name__.lower()
    path = '%s/%s/%s:%s' % (
        type, instance.id,
        get_random_string(10), filename)
    return path


class ProjectUser(AbstractUser):
    """
    Model to store project user details.

    Attribs:-
       phone(char): phone number of the user
       email(email): email of the user
       address(txt): address of the user
       image(img): profile image of the user

    """
    phone = models.CharField(default='', max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)
    image = models.ImageField(
        upload_to=get_file_path, null=True, default=None, blank=True)

    def __str__(self):
        """Object Name in Django Model."""
        return f'{self.id}: {self.first_name}'




