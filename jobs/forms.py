from django import forms
from jobs.models import UserProfile  # Or your model name

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'gender',
            'bio',
            'phone',
            'location',
            'education',
            'experience',
            'skills',
            'contact_email',
            'linkedin_url',
            'github_url',
        ]

