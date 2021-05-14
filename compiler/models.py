from django.db import models
import uuid
# Create your models here.
class problem(models.Model):
    difficulty_levels =(
        ("Easy","Easy"),
        ("Medium","Medium"),
        ("Hard","Hard"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    statement = models.TextField(max_length=5000)
    title = models.CharField(max_length =200)
    difficulty = models.CharField(max_length=15,choices = difficulty_levels)
    constraints =models.TextField(max_length=200)
    points = models.IntegerField()
    def __str__(self):
        return self.title



class test_case(models.Model):
    problem = models.ForeignKey(problem,on_delete =models.CASCADE)
    input = models.CharField(max_length=100)
    output =models.CharField(max_length=500)
    description = models.TextField(max_length =500,default="")
    isPublic =models.BooleanField(default=True)
    def _str__(self):
        return self.id

#test,test@2021