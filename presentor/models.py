from django.db import models
from django.contrib.auth.models import User


class Presentation(models.Model):
    title = models.CharField(max_length=50)
    slides = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        permissions = (
            ("control_presentation", "Can control the presentation"),
        )


class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.choice_text


class Answer(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.choice.choice_text
