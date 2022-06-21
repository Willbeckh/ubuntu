# Generated by Django 4.0.4 on 2022-06-20 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch_app', '0010_neighborhood_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='business',
            field=models.ManyToManyField(blank=True, related_name='neighborhood', to='watch_app.business'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='neighborrhood', to='watch_app.post'),
        ),
    ]