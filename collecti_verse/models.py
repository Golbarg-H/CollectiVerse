from django.db import models


class Collections(models.Model):
    name = models.CharField(max_length=50)


class Books(models.Model):
    original_title = models.CharField(max_length=300)
    translated_title = models.CharField(max_length=300)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Publishers(models.Model):
    name = models.CharField(max_length=100)
