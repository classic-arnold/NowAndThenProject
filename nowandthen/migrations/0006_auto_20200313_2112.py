# Generated by Django 2.1.5 on 2020-03-13 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nowandthen', '0005_pictures_when_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AlterModelOptions(
            name='pictures',
            options={'ordering': ['when_added']},
        ),
        migrations.AlterField(
            model_name='pictures',
            name='era',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='title',
            field=models.CharField(blank=True, max_length=190),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='when_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='nowandthen.Pictures'),
        ),
    ]