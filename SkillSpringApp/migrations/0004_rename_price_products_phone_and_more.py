# Generated by Django 4.2.7 on 2023-11-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillSpringApp', '0003_remove_products_course_remove_products_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='color',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.AddField(
            model_name='products',
            name='course',
            field=models.CharField(default='Data Science', max_length=50),
        ),
        migrations.AddField(
            model_name='products',
            name='email',
            field=models.TextField(default='Email Address'),
        ),
    ]