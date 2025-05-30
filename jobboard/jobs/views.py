from django.shortcuts import render
from django.http import HttpResponse
from jobs.models import JobInformation
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, World!")

class JobsListView(ListView):
    template_name = "app/home.html"
    model = JobInformation
    context_object_name = "Jobs"

class JobCreateView(CreateView):
    template_name = "app/job_create.html"
    model = JobInformation
    fields = ["job_title", "company_name", "location", "job_description"]
    success_url = reverse_lazy("home")

class JobUpdateView(UpdateView):
    template_name = "app/job_update.html"
    model = JobInformation
    fields = ["job_title", "company_name", "location", "job_description"]
    success_url = reverse_lazy("home")
    context_object_name = "Job"

    # def get_object(self, queryset=None):  Only use for custom 404 page
    #     # Use get_object_or_404 to fetch the object
    #     return get_object_or_404(JobInformation, pk=self.kwargs.get('pk'))


class JobDeleteView(DeleteView):
    template_name ="app/job_delete.html"
    model = JobInformation
    success_url = reverse_lazy('home')
    context_object_name = "Job"
    

