from django.db import models


class Team(models.Model):
    team_id = models.IntegerField()
    rating = models.FloatField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    last_match_time = models.IntegerField()
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=50)
    logo_url = models.URLField(max_length=500)

    def __str__(self):
        return self.name
