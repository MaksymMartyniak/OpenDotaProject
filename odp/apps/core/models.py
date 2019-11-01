from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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


class Player(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    full_name = models.CharField(max_length=200)
    open_dota_account_id = models.IntegerField()
    solo_competitive_rank = models.IntegerField(null=True)
    competitive_rank = models.IntegerField(null=True)
    rank_tier = models.IntegerField(null=True)
    leaderboard_rank = models.IntegerField(null=True)
    steamid = models.CharField(max_length=100, null=True)
    avatar = models.URLField(max_length=500, null=True)
    loccountrycode = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.full_name
