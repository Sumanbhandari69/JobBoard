from django.shortcuts import render, redirect
from django.http import HttpResponse
from jobs.models import JobInformation
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.models import UserProfile
from jobs.forms import UserProfileForm
from django.views import View


# Create your views here.

# def home(request):
#     return HttpResponse("Hello, World!")

class JobsListView(ListView):
    template_name = "app/home.html"
    model = JobInformation
    context_object_name = "Jobs"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Exclude jobs posted by the current user
            return JobInformation.objects.exclude(posted_by=user)
        else:
            # For anonymous users, show all jobs
            return JobInformation.objects.all()

class JobCreateView(LoginRequiredMixin,CreateView):
    template_name = "app/job_create.html"
    model = JobInformation
    fields = ["job_title", "company_name", "location", "job_description"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user  # Set current user here
        return super().form_valid(form)

class JobUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "app/job_update.html"
    model = JobInformation
    fields = ["job_title", "company_name", "location", "job_description"]
    success_url = reverse_lazy("home")
    context_object_name = "Job"

    # def get_object(self, queryset=None):  Only use for custom 404 page
    #     # Use get_object_or_404 to fetch the object
    #     return get_object_or_404(JobInformation, pk=self.kwargs.get('pk'))


class JobDeleteView(LoginRequiredMixin,DeleteView):
    template_name ="app/job_delete.html"
    model = JobInformation
    success_url = reverse_lazy('home')
    context_object_name = "Job"


class UserJobsListView(LoginRequiredMixin, ListView):
    template_name = "app/user_job_list.html"
    model = JobInformation
    context_object_name = "Jobs"

    def get_queryset(self):
        return JobInformation.objects.filter(posted_by=self.request.user)
    
class ProfileView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        user = request.user
        response = render(request, "app/profile_public.html")
        # Check if profile exists
        profile = UserProfile.objects.filter(user=user).first()

        if not profile:
            # If no profile, show form to create one
            form = UserProfileForm()
            return render(request, 'app/profile_form.html', {
                'form': form,
                'edit_mode': True
            })

        # If profile exists and user clicked 'Edit'
        if request.GET.get('edit') == '1':
            form = UserProfileForm(instance=profile)
            return render(request, 'app/profile_form.html', {
                'form': form,
                'edit_mode': True
            })
        
        data= {
            'profile': profile,
            'edit_mode': False
        }
        print(data)
        # Else show public profile
        return render(request, 'app/profile_public.html',data)

    def post(self, request):
        user = request.user
        profile = UserProfile.objects.filter(user=user).first()

        if profile:
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')

        return render(request, 'app/profile_form.html', {
            'form': form,
            'edit_mode': True
        })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    

