from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201109_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
