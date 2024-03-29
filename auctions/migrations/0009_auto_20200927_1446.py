from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200927_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='last_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Bid'),
        ),
    ]
