# Generated by Django 2.2.24 on 2023-03-12 00:42
import phonenumbers
from django.db import migrations


def reformat_phonenumber(phone_number):
    phone = phonenumbers.parse(phone_number, 'RU')
    if phonenumbers.is_valid_number(phone):
        return phone


def upgrade_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    old_format_numbers = Flat.objects.exclude(owners_phonenumber__isnull=True)
    for phone in old_format_numbers.iterator():
        phone.owner_pure_phone = reformat_phonenumber(phone.owners_phonenumber)
    Flat.objects.bulk_update(old_format_numbers, ['owner_pure_phone'])


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_auto_20230312_0242'),
    ]

    operations = [
        migrations.RunPython(upgrade_phonenumbers)
    ]
