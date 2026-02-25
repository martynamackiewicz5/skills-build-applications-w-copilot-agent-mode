from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='TestHero', email='hero@test.com')
        self.assertEqual(user.email, 'hero@test.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='TestTeam', members=['hero@test.com'])
        self.assertEqual(team.name, 'TestTeam')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='hero@test.com', activity_type='Running', duration=20)
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=50)
        self.assertEqual(leaderboard.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='TestWorkout', description='Test workout description')
        self.assertEqual(workout.name, 'TestWorkout')
