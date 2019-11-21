from django.conf import settings
from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.contrib import admin
from .models import Visit
from .models import Visitor
from .models import Host
import uuid

admin.site.register(Visitor)
admin.site.register(Host)
admin.site.register(Visit)