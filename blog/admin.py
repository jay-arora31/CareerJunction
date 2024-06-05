from django.contrib import admin
from .models import *
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

class ContentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body_content', )


admin.site.register(Category)
admin.site.register(AnswerQuestion)
admin.site.register(PostDislike)
admin.site.register(PostLike)
admin.site.register(TotalData)
admin.site.register(Post,ContentAdmin)
