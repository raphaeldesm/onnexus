from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='instructors/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    what_you_will_learn = models.TextField(blank=True, null=True)
    course_format = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)
    prerequisites = models.TextField(blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='thumbnails/')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    is_buyable = models.BooleanField(default=True)

    def __str__(self):
        return self.title