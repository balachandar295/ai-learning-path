from django.db import models
from django.contrib.auth.models import User

# 1. User Profile and Preferences
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=50, default='Python')
    level = models.CharField(max_length=50, default='Beginner')
    learning_goal = models.CharField(max_length=100, null=True, blank=True)
    study_time = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    
    # Assessment and Progress tracking
    last_score = models.IntegerField(default=0)
    weak_topics = models.TextField(default='None') 
    streak = models.IntegerField(default=1)
    last_login_date = models.DateField(null=True, blank=True)
    
    # Activity tracking for Heatmap
    activity_count = models.JSONField(default=dict) # e.g., {"2026-03-01": 5}

    def __str__(self):
        return f"{self.user.username} - {self.language} ({self.level})"

# 2. Activity history
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    task_name = models.CharField(max_length=255, null=True, blank=True)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} completed {self.task_name or 'task'} on {self.date}"

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

# 3. Assessment Questions
class Question(models.Model):
    language = models.CharField(max_length=20) # e.g., Python, C, Java
    level = models.CharField(max_length=20, default='Beginner') # Beginner, Intermediate, Advanced
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.language} ({self.level}) - {self.question_text[:30]}"

class AptitudeQuestion(models.Model):
    topic = models.CharField(max_length=255)
    question = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct = models.CharField(max_length=10)
    explanation = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=50, default='Medium')

    def __str__(self):
        return f"{self.topic} - {self.question[:50]}"

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} applied for {self.job_title} at {self.company}"