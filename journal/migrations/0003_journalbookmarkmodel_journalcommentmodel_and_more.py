# Generated by Django 4.2.7 on 2024-02-06 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0002_delete_articlemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalBookmarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='comment')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('created_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalDownloadsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalRatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='rating')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='comment')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('created_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalViewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryModel',
        ),
        migrations.AlterField(
            model_name='journalmodel',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='journal/files', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='journalmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='journal/photos', verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='CommentModel',
        ),
        migrations.AddField(
            model_name='journalviewsmodel',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journalmodel'),
        ),
        migrations.AddField(
            model_name='journalratingmodel',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journalmodel'),
        ),
        migrations.AddField(
            model_name='journaldownloadsmodel',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journalmodel'),
        ),
        migrations.AddField(
            model_name='journalcommentmodel',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journalmodel'),
        ),
        migrations.AddField(
            model_name='journalbookmarkmodel',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journalmodel'),
        ),
    ]