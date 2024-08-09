from django.db import models
 
class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def _str_(self):
        return self.name

class Admin(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    admin_name = models.CharField(max_length=255)
    admin_email = models.EmailField(unique=True)
    admin_password = models.CharField(max_length=255)

    def _str_(self):
        return self.admin_name

class PrepaidPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    validity = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class PostpaidPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    validity = models.CharField(max_length=50)

    def _str_(self):
        return self.name