from django.core.cache import cache
from django.db import models

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import hooks

from .models import Category
from .settings import get_clear_cache


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = 'Manage Categories'
    menu_icon = 'fa-folder-open'
    add_to_settings_menu = False
    list_display = ('name',)
    search_fields = ('name',)


class PeregrineAdminGroup(ModelAdminGroup):
    menu_label = 'Peregrine'
    menu_icon = 'fa-th'
    menu_order = 400
    items = (CategoryAdmin,)


modeladmin_register(PeregrineAdminGroup)


@hooks.register('after_edit_page')
def clear_page_cache(request, page):
    """
    This will clear Django's entire cache after a page edit. It is ugly,
    but Django's cache mechanism doesn't currently support a way to easily
    depending on the value of is_staff() and (if present) is_faculty.
    """

    if get_clear_cache():
        cache.clear()


@register_setting
class PeregrineSettings(BaseSetting):
    """
    Settings for the user to customize their Peregrine blog.
    """
    landing_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='The page to display at the root. If blank, displays the latest posts.'
    )
    post_title = models.CharField(
        max_length=30,
        default="Posts",
        help_text='The menu text label for latest posts.',
    )
    post_number = models.IntegerField(
        default=10,
        help_text='The number of posts to display.',
    )
    post_number_nav = models.IntegerField(
        default=10,
        help_text='The number of posts to display in navigation.',
    )
    post_number_rss = models.IntegerField(
        default=100,
        help_text='The number of posts to include in the RSS feed.',
    )
