from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="teamuser", email="teamuser@example.com", password="password123")
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertIn(self.user, self.team.members.all())

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="activityuser", email="activityuser@example.com", password="password123")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration="01:00:00")

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(str(self.activity.duration), "1:00:00")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="leaderboarduser", email="leaderboarduser@example.com", password="password123")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name="Test Workout", description="A test workout description.")

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Test Workout")
        self.assertEqual(self.workout.description, "A test workout description.")