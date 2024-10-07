# from django.db import models

# # Create your models here.
# from django.db import models
# from users.models import User  # Assuming you want to link to User

# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     content = models.TextField()
#     duration = models.IntegerField()  # Duration in minutes
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Set a default value
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
