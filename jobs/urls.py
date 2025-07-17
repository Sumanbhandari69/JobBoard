from django.urls import path
from jobs.views import JobsListView, JobCreateView, JobUpdateView, JobDeleteView, signup,UserJobsListView
from django.contrib.auth import views as auth_views




urlpatterns = [
    path("", JobsListView.as_view(), name='home'),
    path("job/create/", JobCreateView.as_view(), name="create_job"),
    path("job/<int:pk>/update", JobUpdateView.as_view(), name="update_job"),
    path("job/<int:pk>/delete", JobDeleteView.as_view(), name="delete_job"),
    path('signup/',signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('job/your-jobs', UserJobsListView.as_view(), name="user_job")
    

]
