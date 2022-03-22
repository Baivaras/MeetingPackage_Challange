from django.db import migrations

some_venues = [
    {
        'name': 'Test Venue 1',
        'city': 'Helsinki',
        'country': 'Finland',
        'latitude': 60.1814921,
        'longitude': 24.8840972,
    }, {
        'name': 'Test Venue 2',
        'city': 'Helsinki',
        'country': 'Finland',
        'latitude': 60.1724392,
        'longitude': 24.9394797,
    }, {
        'name': 'Test Venue 3',
        'city': 'Helsinki',
        'country': 'Finland',
        'latitude': 60.1776359,
        'longitude': 24.7862195,
    }, {
        'name': 'Test Venue 4',
        'city': 'Helsinki',
        'country': 'Finland',
        'latitude': 60.4507301,
        'longitude': 22.2660405,
    }, {
        'name': 'Test Venue 5',
        'city': 'Helsinki',
        'country': 'Finland',
        'latitude': 60.3249478,
        'longitude': 24.7295941,
    }, {
        'name': 'Test Venue 6',
        'city': 'Helsinki',
        'country': 'Finland',
        'latitude': 60.1670746,
        'longitude': 24.9598909,
    },
]


def create_dummy_user(apps, schema_editor):
    user = apps.get_model('auth', 'User')
    user.objects.create_superuser(username="mpackage",
                                  first_name="Meeting",
                                  last_name="Package",
                                  email="test@meetingpackage.com",
                                  password="demo123")


def create_dummy_venues(apps, schema_editor):
    venue = apps.get_model('venues', 'Venue')
    for v in some_venues:
        dummy_venue = {
            'name': v['name'],
            'city': v['city'],
            'country': v['country'],
            'latitude': v['latitude'],
            'longitude': v['longitude'],
        }

        venue.objects.create(**dummy_venue)


class Migration(migrations.Migration):
    dependencies = [
        ('venues', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_dummy_venues, migrations.RunPython.noop),
        migrations.RunPython(create_dummy_user, migrations.RunPython.noop)
    ]
