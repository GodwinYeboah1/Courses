from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    
    def validate(self, postdata):
        response = {}
        
        if len(postdata['name']) < 5 :
            response['name'] = 'Course name has to be greater then 3'

        if len(postdata['desc']) < 15:
            response['desc'] = 'Description name has to be greater then 15'

        return response

    def create_course(self,postdata):
        response = {
            "course": None
        }
        course_data = Course(name=postdata['name'],desc=postdata['desc'])
        course_data.save()
        response['course'] = course_data
        return response
        
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __repr__(self):
        return "Course object: {} {}".format(self.name, self.desc)
