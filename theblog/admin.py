from django.contrib import admin
from .models import PostMainPage,PhotoModel,VideoModel,ONasModel
# Register your models here.
admin.site.register(PostMainPage)
admin.site.register(PhotoModel)
admin.site.register(VideoModel)
admin.site.register(ONasModel)