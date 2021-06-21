<<<<<<< Updated upstream
# Generated by Django 3.2 on 2021-06-21 06:33
=======
# Generated by Django 3.2 on 2021-05-14 07:06
>>>>>>> Stashed changes

import core.utilities
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=40, verbose_name='Образ')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(upload_to=core.utilities.get_timestamp_path, verbose_name='Изображение')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_outfits', to=settings.AUTH_USER_MODEL, verbose_name='Автор образа')),
<<<<<<< Updated upstream
                ('likes', models.ManyToManyField(blank=True, related_name='outfits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
=======
            ],
        ),
        migrations.CreateModel(
            name='UserOutfitRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Ok'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')])),
                ('outfit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.outfit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='outfit',
            name='fans',
            field=models.ManyToManyField(related_name='outfits', through='api.UserOutfitRelation', to=settings.AUTH_USER_MODEL),
        ),
>>>>>>> Stashed changes
    ]
