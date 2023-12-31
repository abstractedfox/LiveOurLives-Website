# Generated by Django 4.2.4 on 2023-10-31 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_remove_actualinformation_meta_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualinformation',
            name='meta_info',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.CreateModel(
            name='MultiExcerpt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excerpt', models.CharField(max_length=500)),
                ('parentEntry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.actualinformation')),
            ],
        ),
    ]
