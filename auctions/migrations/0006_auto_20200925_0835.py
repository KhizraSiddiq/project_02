from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200921_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='last_bid',
            field=models.FloatField(null=True),
        ),
    ]
