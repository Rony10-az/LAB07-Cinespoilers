from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # CAMBIO
    list_display = (
        'id',
        'movie',
        'reviewer_name',
        'rating',
        'is_active',
        'created_at'
    )

    list_filter = ('rating', 'is_active')

    # CAMBIO
    search_fields = ('reviewer_name', 'reviewer_email', 'movie__title')

    ordering = ('-created_at',)