from django.db import models
import uuid

class User(models.Model):

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    college = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.first_name