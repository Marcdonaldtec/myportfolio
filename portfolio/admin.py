from django.contrib import admin
from .models import Skill,Education,Experience,Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
