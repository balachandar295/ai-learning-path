import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import AptitudeQuestion

def load_questions():
    csv_file = os.path.join(os.path.dirname(__file__), 'aptitude_questions.csv')
    if not os.path.exists(csv_file):
        print(f"{csv_file} not found!")
        return

    # Delete existing data
    AptitudeQuestion.objects.all().delete()
    print("Deleted old records.")

    questions = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            q = AptitudeQuestion(
                topic=row['topic'],
                question=row['question'],
                option_a=row['option_a'],
                option_b=row['option_b'],
                option_c=row['option_c'],
                option_d=row['option_d'],
                correct=row['correct'],
                explanation=row.get('explanation', ''),
                difficulty=row.get('difficulty', 'Medium')
            )
            questions.append(q)
            
            # Batch create for speed
            if len(questions) >= 500:
                AptitudeQuestion.objects.bulk_create(questions)
                questions = []
                
    if questions:
        AptitudeQuestion.objects.bulk_create(questions)

    print(f"Successfully loaded {AptitudeQuestion.objects.count()} questions into the database.")

if __name__ == '__main__':
    load_questions()