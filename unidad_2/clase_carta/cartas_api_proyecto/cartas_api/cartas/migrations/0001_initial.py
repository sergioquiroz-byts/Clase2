from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carta",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fecha", models.DateField()),
                ("texto", models.TextField()),
                ("remitente", models.CharField(max_length=100)),
                ("destinatario", models.CharField(max_length=100)),
                ("direccion", models.CharField(max_length=200)),
            ],
            options={"ordering": ["-fecha"]},
        ),
    ]
