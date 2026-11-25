from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(name="Pantalon", fields=[
        ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
        ("marca", models.CharField(max_length=50)), ("talla", models.CharField(max_length=10)),
        ("fecha_creacion", models.DateField()), ("material", models.CharField(max_length=50)),
    ], options={"ordering":["id"],"verbose_name":"Pantalón","verbose_name_plural":"Pantalones"})]
