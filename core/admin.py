from django.contrib import admin
from .models import Question, UserPreference, UserActivity, UserProgress, JobApplication

# Ellam models-aiyum inga list pannunga
admin.site.register(Question)
admin.site.register(UserPreference)
admin.site.register(UserActivity)
admin.site.register(UserProgress)
admin.site.register(JobApplication)