# -*- coding: utf-8 -*-

from django.contrib import admin
from data.models import Section, Data, Solutions

class SectionAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'in_menu', 'in_footer', 'weight_menu', 'weight_footer', 'lang')
	search_fields = ['title', 'slug']
	list_filter = ['in_menu', 'in_footer', 'weight_menu', 'weight_footer', 'lang']
	prepopulated_fields = {'slug' : ('title',),}

class DataAdmin(admin.ModelAdmin):
	list_display = ( 'id', 'section', 'text')
	search_fields = ['id', 'section__title', 'text']
	list_filter = ['section']

class SolutionsAdmin(admin.ModelAdmin):
	list_display = ( 'id', 'title', 'subtitle', 'text', 'url', 'solution', 'lang')
	search_fields = ['id', 'title', 'subtitle', 'text', 'url' ,'solution', 'lang']
	list_filter = ['solution', 'lang']

admin.site.register(Section, SectionAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Solutions, SolutionsAdmin)
