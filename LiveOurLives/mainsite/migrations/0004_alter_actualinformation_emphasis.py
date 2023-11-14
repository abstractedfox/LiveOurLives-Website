# Generated by Django 4.2.4 on 2023-11-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_actualinformation_meta_info_multiexcerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualinformation',
            name='emphasis',
            field=models.CharField(choices=[('HEADLINE', 'HEADLINE'), ('EXCERPT', 'EXCERPT')], default='HEADLINE', max_length=100),
        ),
    ]
