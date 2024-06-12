from django.contrib import admin
from .models import Post, Comment, LongRunningOperation

admin.site.register(Post)
admin.site.register(Comment)


@admin.register(LongRunningOperation)
class LongRunningOperationAdmin(admin.ModelAdmin):
    list_display = ('operation_name', 'data', 'result', 'datetime')
