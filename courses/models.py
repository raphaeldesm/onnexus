from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='instructors/')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_thumbnail = models.ImageField(upload_to='thumbnails/')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title