from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Event(models.Model):
    event_name = models.CharField(max_length=50, verbose_name=_('name'))
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name=_('start date'))
    end_date = models.DateField(verbose_name=_('end date'))
    location = models.CharField(max_length=50, verbose_name=_('location'))
    description = models.TextField(verbose_name=_('description'))

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        return self.event_name


class Team(models.Model):
    team_name = models.CharField(max_length=50, verbose_name=_('name'))

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def __str__(self):
        return self.team_name


class Participant(models.Model):
    fullname = models.CharField(max_length=70, verbose_name=_('name'))
    birth_date = models.DateField(verbose_name=_('birth date'))
    gender = models.CharField(max_length=50, verbose_name=_('gender'))
    team_id = models.ForeignKey(Team, verbose_name=_('team'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('participants')
        verbose_name_plural = _('participants')

    def __str__(self):
        return self.fullname


class Result(models.Model):
    event_id = models.ForeignKey(Event, verbose_name=_('event id'), on_delete=models.CASCADE)
    participant_id = models.ForeignKey(Participant, verbose_name=_('participant id'), on_delete=models.CASCADE)
    result = models.CharField(max_length=50, verbose_name=_('result'))

    class Meta:
        verbose_name = _('result')
        verbose_name_plural = _('results')

    def __str__(self):
        return self.result


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name=_('name'))
    password = models.CharField(max_length=70, verbose_name=_('password'))
    email = models.EmailField(max_length=100, verbose_name=_('email'))
    role = models.CharField(max_length=50, verbose_name=_('role'))

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

