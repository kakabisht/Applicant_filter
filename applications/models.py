import json
import sys
import time
import requests

# pip install misaka
import misaka

from django.db import models
from django.conf import settings
from django.urls import reverse

from companys.models import Company
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
User = get_user_model()


class Application(models.Model):
    '''
        Application model containing details of the application, along with data base restrictions and constraints
    '''

    user = models.ForeignKey(
        User, related_name="applications", on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, related_name="applications", null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    github = models.URLField(max_length=254, blank=True)
    linkedin = models.URLField(max_length=254, blank=True)
    portfolio_site = models.URLField(max_length=254, blank=True)
    resume = models.FileField(upload_to='resume/')
    tell_us_something_about_yourself = models.TextField(
        max_length=150)
    tell_us_about_your_weaknesses = models.TextField(
        max_length=150)
    apart_from_core_technical_skills = models.TextField(
        max_length=150)
    how_do_you_handle_stress_and_Pressure = models.TextField(
        max_length=150)
    do_you_like_to_work_in_a_team_or_work_alone = models.CharField(
        max_length=50)
    What_do_you_prefer_on_weekends_staying_home_or_going_out = models.CharField(
        max_length=50)
    would_you_correct_your_colleagues_or_wont_bother = models.CharField(
        max_length=50)
    in_a_group_which_person_has_your_attention = models.CharField(
        max_length=50)
    do_you_believe_you_can_achieve_everything = models.CharField(
        max_length=50)
    What_attracts_you_science_or_music = models.CharField(
        max_length=50)
    do_you_like_to_plan_before_or_after_things = models.CharField(
        max_length=50)
    would_you_change_your_preferences = models.CharField(
        max_length=50)

    class Meta:
        # How to order application in admin side
        ordering = ['email']

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        '''
        Saving application form into the data base, perfoming compute on text messages.
        '''
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # To check information about a particular application
        return reverse(
            "applications:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )
