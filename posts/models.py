from django.db import models

import uuid
# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4 )

class Topic(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(BaseModel):
    category = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title