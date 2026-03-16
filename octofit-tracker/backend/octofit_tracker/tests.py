from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='testuser@test.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=50)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'run')
        self.assertEqual(self.activity.duration, 10)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 50)
