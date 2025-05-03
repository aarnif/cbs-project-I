from django.contrib.auth.hashers import check_password
from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    # FLAW 2: Identification and Authentication Failures (Storing password in plaintext)
    password = models.CharField(max_length=200)

    # FLAW 2 FIX
    # def _hash_password(self, raw_password):
    #     from django.contrib.auth.hashers import make_password
    #     return make_password(raw_password)

    # def save(self, *args, **kwargs):
    #     self.password = self._hash_password(self.password)
    #     super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # This is just for testing purposes
        if raw_password == "password":
            return True
        return check_password(raw_password, self.password)
    