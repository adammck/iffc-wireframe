#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.contrib import admin
from . import models


admin.site.register(models.AreaType)
admin.site.register(models.Area)
admin.site.register(models.AgeGroup)
admin.site.register(models.Sector)
admin.site.register(models.Dataset)
admin.site.register(models.LifecycleStage)
admin.site.register(models.CrcPart)
admin.site.register(models.CrcArticle)
admin.site.register(models.WfcGoal)
admin.site.register(models.Demographic)
admin.site.register(models.FactsChapter)
admin.site.register(models.FactsMessage)
admin.site.register(models.Issue)
admin.site.register(models.Indicator)
admin.site.register(models.Message)
admin.site.register(models.Range)
admin.site.register(models.Value)
