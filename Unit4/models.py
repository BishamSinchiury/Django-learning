from django.db import models

class Student(models.Model):
    # Student's full name
    name = models.CharField(max_length=100)
    # Age of the student (integer)
    age = models.IntegerField()
    # Student's email address with validation
    email = models.EmailField(unique=True)
    # Whether the student is currently active
    is_active = models.BooleanField(default=True)
    # The date the student enrolled, auto-filled when created
    enrolled_date = models.DateField(auto_now_add=True)
    # A short bio or description
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        # This will show the student name instead of "Student object (1)"
        return f"{self.name} ({self.email})"

class Task(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()