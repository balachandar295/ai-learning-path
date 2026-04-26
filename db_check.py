import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import Question, AptitudeQuestion

print(f"Aptitude: {AptitudeQuestion.objects.count()}")
print(f"DSA: {Question.objects.filter(language='DSA').count()}")
print(f"C#: {Question.objects.filter(language='C#').count()}")
print(f"JavaScript: {Question.objects.filter(language='JavaScript').count()}")
print(f"SQL: {Question.objects.filter(language='Sql').count()}")
