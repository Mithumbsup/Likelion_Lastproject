# Generated by Django 2.1.7 on 2019-12-28 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=200, null=True)),
                ('product', models.CharField(max_length=200)),
                ('orderer', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=800)),
                ('phone1', models.CharField(max_length=100)),
                ('phone2', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('message', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('price', models.IntegerField(blank=True)),
                ('delivery_price', models.IntegerField(blank=True, null=True)),
                ('total_price', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('component', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('bad', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.Post'),
        ),
    ]
