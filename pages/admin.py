from django.contrib import admin
from django.contrib.admin.sites import site
from .models import page

# Register your models here.
admin.site.register(page)

#configuracion del panel
title = "Proyecto con django"
subtitle ="Panel de gestion"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
