from django.db import models
from django.utils import timezone
# Create your models here.

class RoastBoastModel(models.Model):
    boast_roast = [(True, 'Boast'), (False, 'Roast')]
    body = models.CharField(max_length=280)
    choices = models.BooleanField(choices=boast_roast, default=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    vote_score = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)


    # def votes(self):
    #     return self.upvote + self.downvote

    def __str__(self):
        return self.body