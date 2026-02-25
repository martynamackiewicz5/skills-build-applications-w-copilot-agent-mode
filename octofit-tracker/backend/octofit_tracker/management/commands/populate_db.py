from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        marvel_users = [
            User.objects.create_user(username='IronMan', email='ironman@marvel.com'),
            User.objects.create_user(username='CaptainAmerica', email='cap@marvel.com'),
            User.objects.create_user(username='Thor', email='thor@marvel.com'),
        ]
        dc_users = [
            User.objects.create_user(username='Batman', email='batman@dc.com'),
            User.objects.create_user(username='Superman', email='superman@dc.com'),
            User.objects.create_user(username='WonderWoman', email='wonderwoman@dc.com'),
        ]

        # Create teams
        Team.objects.create(name='Marvel', members=[u.email for u in marvel_users])
        Team.objects.create(name='DC', members=[u.email for u in dc_users])

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', activity_type='Running', duration=30)
        Activity.objects.create(user_email='batman@dc.com', activity_type='Cycling', duration=45)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Hero Strength', description='Full body workout for heroes')
        Workout.objects.create(name='Speed Training', description='Increase your speed like Flash')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
