# Generated by Django 4.2.4 on 2023-10-24 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActualInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ARTICLE STUDY', 'Article on a study'), ('ARTICLE OPINION', 'Opinion piece'), ('ARTICLE STATISTICS', 'Article on statistics'), ('ANECDOTE', 'Personal anecdote'), ('STUDY', 'Study'), ('STATISTICS', 'Statistics & Models'), ('EXAMPLE', 'Example'), ('OTHER/MIXED', 'Other / Mixed'), ('PAPER', 'Paper')], default='OTHER/MIXED', max_length=150)),
                ('source', models.CharField(choices=[('INDIVIDUAL ACCOUNT', 'Individual account'), ('MEDICAL PROFESSIONAL', 'Medical professional'), ('GROUP OF PROFESSIONALS', 'Group of professionals'), ('ENGINEER', 'Engineer'), ('GOVERNING BODY', 'Governing body'), ('JOURNALIST', 'Journalist'), ('OTHER/MIXED', 'Other / Mixed'), ('OTHER PROFESSIONAL', 'Other / Professional'), ('ECONOMIST', 'Economist')], default='OTHER/MIXED', max_length=150)),
                ('archiveLink', models.CharField(blank=True, default='', max_length=2000)),
                ('liveLink', models.CharField(blank=True, default='', max_length=2000)),
                ('headline', models.CharField(max_length=500)),
                ('publication', models.CharField(blank=True, default='', max_length=150)),
                ('exerpt', models.CharField(blank=True, default='', max_length=600)),
                ('author', models.CharField(blank=True, default='', max_length=1000)),
                ('authors_title', models.CharField(blank=True, default='', max_length=150)),
                ('participants', models.IntegerField(blank=True, default=0)),
                ('meta_info', models.CharField(blank=True, default='', max_length=1000)),
                ('datePublished', models.DateField(blank=True, null=True)),
                ('dateArchived', models.DateField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
                ('emphasis', models.CharField(choices=[('HEADLINE', 'HEADLINE'), ('EXCERPT', 'EXCERPT')], default=('HEADLINE', 'HEADLINE'), max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localPath', models.CharField(blank=True, default='#', max_length=200)),
                ('altText', models.CharField(blank=True, default='', max_length=200)),
                ('author', models.CharField(blank=True, default='', max_length=200)),
                ('sourcedFrom', models.CharField(blank=True, default='', max_length=500)),
                ('sourceLink', models.CharField(blank=True, default='', max_length=500)),
                ('dateGathered', models.DateField(blank=True, null=True)),
                ('licenseInfo', models.CharField(blank=True, default='', max_length=2000)),
                ('changesMade', models.CharField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='InfoCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(choices=[('LONG COVID EFFECTS ON BODY', 'Long covid & effects on the body'), ('LONG COVID ANECDOTES', 'Long covid anecdotes'), ('LONG COVID', 'Long covid'), ('MITIGATION AND EFFICACY', 'Mitigation and efficacy'), ('IMMUNE SYSTEM', 'Immune system'), ('ARTICLE', 'Article'), ('STUDY', 'Study'), ('ECONOMY', 'Economy'), ('TRANSMISSIBILITY', 'Transmission'), ('VACCINES', 'Vaccines'), ('Misc.', 'Misc')], default='Misc.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MinimizerRetorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=100)),
                ('longName', models.CharField(blank=True, max_length=400)),
                ('display', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MultiExcerpt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excerpt', models.CharField(max_length=500)),
                ('parentEntry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.actualinformation')),
            ],
        ),
        migrations.AddField(
            model_name='actualinformation',
            name='categories',
            field=models.ManyToManyField(to='mainsite.infocategories'),
        ),
        migrations.AddField(
            model_name='actualinformation',
            name='retorts',
            field=models.ManyToManyField(to='mainsite.minimizerretorts'),
        ),
    ]
