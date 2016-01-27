from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'updated', 'timestamp']
	list_display_links = ['updated']
	list_filter = ['updated', 'timestamp']
	search_fields = ['content', 'title']
	list_editable = ['title']
	class Meta:
		model = Post