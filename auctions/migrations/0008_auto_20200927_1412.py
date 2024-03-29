from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='last_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auctions.Bid'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
