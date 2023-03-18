from django.db import models

# Create your models here.
class About(models.Model):
    data_set = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images')
    about = models.TextField()
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resume')
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    github_link = models.URLField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.data_set

    class Meta:
        verbose_name_plural = "01. Personal Data"


class Experience(models.Model):
    date = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "02. Experience"


class Education(models.Model):
    date = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.institution_name
    
    class Meta:
        verbose_name_plural = "03. Education"


class Skills(models.Model):
    name=models.CharField(max_length=255)
    percentage=models.IntegerField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "04. Skills"

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_link = models.URLField()
    image = models.ImageField(upload_to='images')
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.project_name
    
    class Meta:
        verbose_name_plural = "05. Projects"
    

class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonial_images', blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "06. Testimonials"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "07. Contact"