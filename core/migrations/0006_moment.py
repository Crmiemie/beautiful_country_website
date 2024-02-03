# Generated by Django 4.2.5 on 2023-12-14 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_city_feature_category_city_feature_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('note', models.CharField(default='', max_length=4096)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
