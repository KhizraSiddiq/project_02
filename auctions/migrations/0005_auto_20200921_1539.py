from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200921_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='photo',
            new_name='picture',
        ),
    ]
