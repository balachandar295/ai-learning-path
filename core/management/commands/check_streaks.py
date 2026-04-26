from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from core.models import UserPreference, UserActivity

class Command(BaseCommand):
    help = 'Checks daily user activity to identify broken streaks and send reminder emails.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Starting daily streak check..."))
        
        today = timezone.localdate()
        yesterday = today - timedelta(days=1)
        
        users_emailed = 0
        
        # Iterate over all registered users
        for user in User.objects.all():
            try:
                pref = UserPreference.objects.get(user=user)
                if pref.streak > 0:
                    # Check if the user had activity yesterday OR today
                    had_activity_yesterday_or_today = UserActivity.objects.filter(
                        user=user, 
                        task_completed=True,
                        date__gte=yesterday
                    ).exists()
                    
                    if not had_activity_yesterday_or_today:
                        # Streak is broken or about to be broken!
                        # Update database strictly to 0
                        old_streak = pref.streak
                        pref.streak = 0
                        pref.save()
                        
                        # Send urgent email alert!
                        if user.email:
                            try:
                                send_mail(
                                    subject='🚨 Urgent: Your Coding Streak is Breaking!',
                                    message=f'Hello {user.first_name or user.username},\n\nWe noticed you haven\'t solved an AI Learning Path coding problem today.\n\nYou are about to lose your hard-earned {old_streak}-day streak!\n\nLog in right now and solve a quick problem to protect your progress.\n\nKeep coding!\n- The AI Learning Path Team',
                                    from_email='bchandar295@gmail.com',  # Or use settings.DEFAULT_FROM_EMAIL
                                    recipient_list=[user.email],
                                    fail_silently=False,
                                )
                                users_emailed += 1
                                self.stdout.write(self.style.SUCCESS(f"Email sent to {user.email} (Streak {old_streak} broken)."))
                            except Exception as e:
                                self.stdout.write(self.style.ERROR(f"Failed to send email to {user.email}: {e}"))
                                
            except UserPreference.DoesNotExist:
                continue

        self.stdout.write(self.style.SUCCESS(f"Streak check complete. Emailed {users_emailed} users."))
