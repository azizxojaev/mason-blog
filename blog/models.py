from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return "Rasim"


class Timeline(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="timeline/")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    section1_image = models.ImageField(upload_to="about/", default=None)
    section1_header = models.CharField(max_length=50, default=None)
    section1_text = models.TextField(default=None)
    section2_image = models.ImageField(upload_to="about/", default=None)
    section2_header = models.CharField(max_length=50, default=None)
    section2_text = models.TextField(default=None)
    card1_image = models.ImageField(upload_to="about/", default=None)
    card1_header = models.CharField(max_length=50, default=None)
    card1_text = models.CharField(max_length=150, default=None)
    card2_image = models.ImageField(upload_to="about/", default=None)
    card2_header = models.CharField(max_length=50, default=None)
    card2_text = models.CharField(max_length=150, default=None)
    card3_image = models.ImageField(upload_to="about/", default=None)
    card3_header = models.CharField(max_length=50, default=None)
    card3_text = models.CharField(max_length=150, default=None)
    bottom_section_header = models.CharField(max_length=50)
    bottom_section_text = models.TextField()
    
    def __str__(self):
        return "About Information"

class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)

    def __str__(self):
        return "Contact Information"