from django import forms
from .models import user, experience, education, skill, course


class user_form(forms.ModelForm):
    class Meta:
        model = user
        fields = [
            'user_id',
            'user_about',
            'user_age',
            'user_city',
            'user_country',
            'user_email',
            'user_first_name',
            'user_jop_title',
            'user_last_name',
            'user_password',
            'user_phone'
        ]


class userUpdateForm(forms.ModelForm):
    class Meta:
        model = user
        fields = [
            'user_age',
            'user_city',
            'user_country',
            'user_email',
            'user_first_name',
            'user_jop_title',
            'user_last_name',
            'user_password',
            'user_phone'
        ]


class loginForm(forms.ModelForm):
    class Meta:
        model = user
        fields = [
            'user_email',
            'user_password'

        ]


class educationUpdateForm(forms.ModelForm):
    class Meta:
        model = education
        fields = [
            'education_degree',
            'education_place',
            'end_date',
            'start_date',
            'user_id'
        ]


class experienceForm(forms.ModelForm):
    class Meta:
        model = experience
        fields = [
            'end_date',
            'experience_place',
            'experience_position',
            'start_date',
            'user_id'
        ]


class courseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = [

            'course_name',
            'course_provider',
            'user_id'
        ]


class aboutForm(forms.ModelForm):
    class Meta:
        model = user
        fields = [
            'user_about'
        ]


class skillForm(forms.ModelForm):
    class Meta:
        model = skill
        fields = [

            'skill_name',
            'user_id'
        ]
