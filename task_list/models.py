from django.db import models
from django.utils import timezone

CHOICES_status = (('Open', 'Open'), ('Needs offer', 'Needs offer'), ('Offered', 'Offered'),
                  ('Approved', 'Approved'), ('In progress', 'In progress'), ('Ready', 'Ready'),
                  ('Verified', 'Verified'), ('Closed', 'Closed'),)

class Task(models.Model):
    name = models.CharField(max_length=64)
    about = models.TextField(max_length=1000)
    image =models.ImageField(upload_to='img', null=True)
    create_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateField()
    status = models.CharField(choices=CHOICES_status, default='Open', max_length=64)

    def __str__(self):
        return self.name

