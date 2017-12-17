# -*- coding: utf-8 -*-
# Generated by Django 1.11.8.dev20171216134037 on 2017-12-16 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='SitePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.TextBlock(icon='title', template='wagtailcontentstream/blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], icon='pilcrow')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock(icon='table')), ('code', wagtail.core.blocks.StructBlock((('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('http', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', label='Language')), ('code', wagtail.core.blocks.TextBlock(label='Code'))), icon='code'))), blank=True)),
                ('excerpt', wagtail.core.fields.RichTextField(blank=True, help_text='An short excerpt or abstract about the content.', null=True)),
            ],
            options={
                'verbose_name': 'Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SitePost',
            fields=[
                ('sitepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='peregrine.SitePage')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time of the post.')),
            ],
            options={
                'verbose_name': 'Post',
            },
            bases=('peregrine.sitepage',),
        ),
        migrations.AddField(
            model_name='sitepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='The categories for the page or post.', to='peregrine.Category'),
        ),
        migrations.AddField(
            model_name='sitepage',
            name='header_image',
            field=models.ForeignKey(blank=True, help_text='A featured image that will appear in the site theme header.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='sitepost',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='The authors of the post.', to=settings.AUTH_USER_MODEL),
        ),
    ]
