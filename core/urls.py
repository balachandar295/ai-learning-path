from django.urls import path
from . import views 

urlpatterns = [
    # 1. Main Entry Point (Root URL)
    # User empty URL-ku vandha, namba ezhudhuna redirect logic-ku poga vaimom
    path('', views.root_redirect, name='root'), 

    # 2. Authentication Pages
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password-logic/', views.reset_password_logic, name='reset_password_logic'),

    # 3. User Flow Pages
    path('home/', views.home_view, name='home_view'), # Indhu dhaan unga main landing
    path('profile/', views.profile_view, name='profile_view'), #
    path('assessment/', views.assessment_view, name='assessment_view'), #
    path('dashboard/', views.dashboard_view, name='dashboard_view'),

    # 4. Backend Logic (Action URLs)
    path('update-profile/', views.update_profile, name='update_profile'),
    path('submit-test/', views.submit_test, name='submit_test'),
    path('logout/', views.logout_view, name='logout_view'),
    path('ai-chat/', views.ai_mentor_chat, name='ai_mentor_chat'),
    path('api/ai-video-tutor/', views.ai_video_tutor_api, name='ai_video_tutor_api'),
    path('run-python/', views.run_python_code, name='run_python_code'),
    path('aptitude/', views.aptitude_categories, name='aptitude_categories'),
    path('aptitude/arithmetic/', views.arithmetic_topics, name='arithmetic_topics'),
    path('aptitude/logical-reasoning/', views.logical_reasoning_topics, name='logical_reasoning_topics'),
    path('aptitude/data-interpretation/', views.data_interpretation_topics, name='data_interpretation_topics'),
    path('aptitude/verbal-reasoning/', views.verbal_reasoning_topics, name='verbal_reasoning_topics'),
    path('aptitude/non-verbal-reasoning/', views.non_verbal_reasoning_topics, name='non_verbal_reasoning_topics'),
    path('aptitude/puzzles/', views.puzzle_topics, name='puzzle_topics'),
    path('arithmetic/progress/', views.progress_view, name='progress_view'),
    path('topic-detail/', views.topic_detail_view, name='topic_detail'),
    path('aptitude-test/', views.aptitude_test_view, name='aptitude_test_view'),
    path('roadmap/<str:track_name>/', views.roadmap_view, name='roadmap_view'),
    path('coding-problems/', views.coding_problems_view, name='coding_problems_view'),
    path('problem-solve/', views.problem_solve_view, name='problem_solve'),
    path('jobs/', views.jobs_view, name='jobs_view'),
    path('job-apply/', views.job_apply_view, name='job_apply'),
    path('api/jobs/', views.fetch_jobs_api, name='fetch_jobs_api'),
    path('api/update-streak/', views.update_streak_api, name='update_streak_api'),
    path('career-paths/', views.developer_roles_view, name='developer_roles'),
    path('career-paths/<slug:role_slug>/', views.detailed_roadmap_view, name='detailed_roadmap'),

    # 5. Comprehensive Assessment Hub
    path('skill-tests/', views.skill_tests_hub_view, name='skill_tests_hub'),
    path('skill-tests-instructions/<str:category>/', views.skill_test_instructions_view, name='skill_test_instructions'),
    path('skill-tests/<str:category>/', views.comprehensive_test_view, name='comprehensive_test'),
    path('skill-tests-submit/', views.submit_comprehensive_test, name='submit_comprehensive_test'),
    path('certificate/', views.certificate_view, name='certificate_view'),
    path('mock-interview/', views.mock_interview_view, name='mock_interview'),
    path('api/interview-chat/', views.interview_chat, name='interview_chat'),
    path('load-my-data/', views.load_data_view, name='load_data'),
]