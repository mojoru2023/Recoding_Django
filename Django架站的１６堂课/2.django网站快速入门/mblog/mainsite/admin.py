from django.contrib import admin

# Register your models here.


from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')  #显示具体时间



admin.site.register(Post,PostAdmin)


