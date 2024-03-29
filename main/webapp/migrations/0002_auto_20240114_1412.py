# Generated by Django 3.2.21 on 2024-01-14 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='job_photo1',
        ),
        migrations.RemoveField(
            model_name='jobmodel',
            name='job_photo2',
        ),
        migrations.RemoveField(
            model_name='jobmodel',
            name='job_photo3',
        ),
        migrations.CreateModel(
            name='Product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('time_created', models.DateTimeField(blank=True, null=True)),
                ('job_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_images', to='webapp.jobmodel')),
            ],
            options={
                'ordering': ['time_created'],
            },
        ),
    ]
