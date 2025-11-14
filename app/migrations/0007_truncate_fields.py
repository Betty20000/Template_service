# app/migrations/000X_truncate_fields.py
from django.db import migrations

def truncate_fields(apps, schema_editor):
    Template = apps.get_model('app', 'Template')
    for t in Template.objects.all():
        if t.version:
            t.version = t.version[:10]
        if t.type:
            t.type = t.type[:10]
        if t.language:
            t.language = t.language[:2]
        if t.name:
            t.name = t.name[:255]
        t.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_template_language_alter_template_name_and_more'),
    ]

    operations = [
        migrations.RunPython(truncate_fields),
    ]
