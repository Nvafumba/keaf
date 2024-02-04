from django.db import models
import random
import string

class County(models.Model):
    county_id = models.AutoField(primary_key=True)
    county_name = models.CharField(max_length=255)

    def __str__(self):
        return self.county_name

class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name
   

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    def generate_person_id():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(5))

    person_id = models.CharField(max_length=5, default=generate_person_id, unique=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Other')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=1)
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LeadershipPosition(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Leadership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.ForeignKey(LeadershipPosition, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} - {self.position}"