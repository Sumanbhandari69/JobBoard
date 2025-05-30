from django.urls import path
from jobs.views import JobsListView, JobCreateView, JobUpdateView, JobDeleteView

urlpatterns = [
    path("", JobsListView.as_view(), name='home'),
    path("job/create/", JobCreateView.as_view(), name="create_job"),
    path("job/<int:pk>/update", JobUpdateView.as_view(), name="update_job"),
    path("job/<int:pk>/delete", JobDeleteView.as_view(), name="delete_job")
]
