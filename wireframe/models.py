#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.db import models


class Area(models.Model):
    name   = models.CharField(max_length=100)
    parent = models.ForeignKey("self", null=True, blank=True)


class AgeGroup(models.Model):
    name = models.CharField(max_length=100)
    min  = models.IntegerField()
    max  = models.IntegerField()


class Sector(models.Model):
    name = models.CharField(max_length=100)


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()


class LifecycleStage(models.Model):
    """
    Lifecycle stages are (almost) always displayed in the right-hand
    side of the map, to highlight which stages of life the currently-
    viewed issue affects. They can also be clicked, to filter issues.
    """

    name  = models.CharField(max_length=100)
    order = models.IntegerField(help_text=
        "The order in which this stage occurs in life. " +
        "Lower is earlier.")

    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return self.name


class CrcPart(models.Model):
    name     = models.CharField(max_length=100)
    preamble = models.TextField(blank=True)


class CrcArticle(models.Model):
    part = models.ForeignKey(CrcPart)
    text = models.TextField()


class WfcGoal(models.Model):
    number = models.IntegerField()
    text   = models.TextField()


GENDER_CHOICES = (
    ('M', "Male"),
    ('F', "Female"))

class Demographic(models.Model):
    area       = models.ForeignKey(Area)
    age_group  = models.ForeignKey(AgeGroup)
    gender     = models.CharField(max_length=2, choices=GENDER_CHOICES)
    population = models.IntegerField()


class FactsChapter(models.Model):
    name = models.CharField(max_length=100)


class FactsMessage(models.Model):
    chapter = models.ForeignKey(FactsChapter)
    number  = models.IntegerField()
    summary = models.TextField(blank=True)
    text    = models.TextField(blank=True)


class Issue(models.Model):
    sector          = models.ForeignKey(Sector)
    crc_articles    = models.ManyToManyField(CrcArticle)
    lifecycle_stage = models.ForeignKey(LifecycleStage)
    facts_message   = models.ForeignKey(FactsMessage)
    wfc_goal        = models.ForeignKey(WfcGoal)


UNIT_CHOICES = (
    ('num',   "Absolute"),
    ('rate',  "Rate"),
    ('ratio', "Ratio"))

class Indicator(models.Model):
    name       = models.CharField(max_length=100)
    unit       = models.CharField(max_length=5, choices=UNIT_CHOICES)
    is_primary = models.BooleanField()
    issue      = models.ForeignKey(Issue)


class Message(models.Model):
    text = models.TextField()


class Range(models.Model):
    indicator = models.ForeignKey(Indicator)
    best      = models.IntegerField()
    worst     = models.IntegerField()


class Value(models.Model):
    indicator   = models.ForeignKey(Indicator)
    demographic = models.ForeignKey(Demographic)
    dataset     = models.ForeignKey(Dataset)
    value       = models.IntegerField()
