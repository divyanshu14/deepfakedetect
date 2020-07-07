# Generated by Django 3.0.8 on 2020-07-07 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_suggestions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakevideo',
            name='reasons',
        ),
        migrations.RemoveField(
            model_name='reason',
            name='votes',
        ),
        migrations.CreateModel(
            name='VideoHasReasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('fakeVideo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_suggestions.FakeVideo')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_suggestions.Reason')),
            ],
        ),
    ]