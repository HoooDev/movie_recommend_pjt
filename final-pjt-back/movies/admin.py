from django.contrib import admin
from .models import Movie, Review
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, MovieAdmin)