from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    
    def validate(self, postdata):
        errors = {}

        if len(postdata['name']) < 3:
            errors['name'] = 'Course name has to be greater then 3'

        if len(postdata['desc']) < 3:
            errors['desc'] = 'Description name has to be greater then 3'
        return errors
        
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __repr__(self):
        return "Course object: {} {}".format(self.name, self.desc)
