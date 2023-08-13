# Generated by Django 4.2.4 on 2023-08-02 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("Mr.", "Mr."),
                            ("Mrs.", "Mrs."),
                            ("Miss.", "Miss."),
                            ("Dr.", "Dr."),
                        ],
                        max_length=10,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            (
                                "Andaman and Nicobar Islands",
                                "Andaman and Nicobar Islands",
                            ),
                            ("Andhra Pradesh", "Andhra Pradesh"),
                            ("Arunachal Pradesh", "Arunachal Pradesh"),
                            ("Assam", "Assam"),
                            ("Bihar", "Bihar"),
                            ("Chandigarh", "Chandigarh"),
                            ("Chhattisgarh", "Chhattisgarh"),
                            (
                                "Dadra and Nagar Haveli and Daman and Diu",
                                "Dadra and Nagar Haveli and Daman and Diu",
                            ),
                            ("Delhi", "Delhi"),
                            ("Goa", "Goa"),
                            ("Gujarat", "Gujarat"),
                            ("Haryana", "Haryana"),
                            ("Himachal Pradesh", "Himachal Pradesh"),
                            ("Jammu and Kashmir", "Jammu and Kashmir"),
                            ("Jharkhand", "Jharkhand"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("Lakshadweep", "Lakshadweep"),
                            ("Madhya Pradesh", "Madhya Pradesh"),
                            ("Maharashtra", "Maharashtra"),
                            ("Manipur", "Manipur"),
                            ("Meghalaya", "Meghalaya"),
                            ("Mizoram", "Mizoram"),
                            ("Nagaland", "Nagaland"),
                            ("Odisha", "Odisha"),
                            ("Puducherry", "Puducherry"),
                            ("Punjab", "Punjab"),
                            ("Rajasthan", "Rajasthan"),
                            ("Sikkim", "Sikkim"),
                            ("Tamil Nadu", "Tamil Nadu"),
                            ("Telangana", "Telangana"),
                            ("Tripura", "Tripura"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Uttarakhand", "Uttarakhand"),
                            ("West Bengal", "West Bengal"),
                        ],
                        default="Karnataka",
                        max_length=100,
                    ),
                ),
                (
                    "contact_person",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("gstin", models.CharField(max_length=15)),
                ("website", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="HoistWorkOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wonumber", models.IntegerField(unique=True)),
                ("date", models.DateField()),
                ("ponumber", models.CharField(max_length=100)),
                ("po_date", models.DateField()),
                ("delivery_date", models.DateField()),
                (
                    "hoist_size",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("250", "250"),
                            ("280", "280"),
                            ("350", "350"),
                            ("380", "380"),
                            ("430", "430"),
                            ("530", "530"),
                            ("680", "680"),
                            ("730", "730"),
                            ("830", "830"),
                            ("I-Lift", "I-Lift"),
                        ],
                        max_length=10,
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "capacity",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("250", "250"),
                            ("500", "500"),
                            ("1000", "1000"),
                            ("2000", "2000"),
                            ("3000", "3000"),
                            ("5000", "5000"),
                            ("7500", "7500"),
                            ("10000", "10000"),
                            ("15000", "15000"),
                            ("20000", "20000"),
                            ("25000", "25000"),
                            ("30000", "30000"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "height",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("8", "8"),
                            ("9", "9"),
                            ("12", "12"),
                            ("15", "15"),
                            ("18", "18"),
                            ("20", "20"),
                            ("24", "24"),
                            ("25", "25"),
                            ("30", "30"),
                            ("40", "40"),
                            ("50", "50"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "fall",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1/1", "1/1"),
                            ("2/1", "2/1"),
                            ("4/1", "4/1"),
                            ("4/2", "4/2"),
                            ("6/2", "6/2"),
                            ("8/2", "8/2"),
                            ("10/2", "10/2"),
                            ("12/2", "12/2"),
                            ("16/2", "16/2"),
                        ],
                        max_length=10,
                    ),
                ),
                ("hoist_code", models.CharField(max_length=100)),
                (
                    "trolley_type",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Foot Mounted", "Foot Mounted"),
                            ("Hand Geared", "Hand Geared"),
                            ("Lug Mounted", "Lug Mounted"),
                            ("Motorized", "Motorized"),
                            ("Push Pull", "Push Pull"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "additional_feature",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Extended Trolley", "Extended Trolley"),
                            ("Flame Proof", "Flame Proof"),
                            ("Flexible Trolley", "Flexible Trolley"),
                            ("Standard", "Standard"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "hoist_speed",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1", "1"),
                            ("1.3", "1.3"),
                            ("1.5", "1.5"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("6", "6"),
                            ("8", "8"),
                            ("9", "9"),
                            ("12", "12"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "hoist_motor",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("0.25", "0.25"),
                            ("0.50", "0.50"),
                            ("0.75", "0.75"),
                            ("1.00", "1.00"),
                            ("1.50", "1.50"),
                            ("2.00", "2.00"),
                            ("3.00", "3.00"),
                            ("5.00", "5.00"),
                            ("7.50", "7.50"),
                            ("10.00", "10.00"),
                            ("15.00", "15.00"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "hoist_motor_rpm",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("720", "720"),
                            ("960", "960"),
                            ("1440", "1440"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "hoist_brake",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("DAT 130", "DAT 130"),
                            ("DAT 150", "DAT 150"),
                            ("DAT 150X", "DAT 150X"),
                            ("DAT 190", "DAT 190"),
                            ("DAT 190X", "DAT 190X"),
                            ("DAT 235", "DAT 235"),
                            ("DAT 235X", "DAT 235X"),
                            ("DAT 290", "DAT 290"),
                            ("DAT 290X", "DAT 290X"),
                            ("DAT 290XX", "DAT 290XX"),
                            ('Dia 4"', 'Dia 4"'),
                            ('Dia 5.5"', 'Dia 5.5"'),
                            ('Dia 7"', 'Dia 7"'),
                            ("K1", "K1"),
                            ("K2", "K2"),
                            ("K3", "K3"),
                            ("K4", "K4"),
                            ("K5", "K5"),
                            ("K6", "K6"),
                            ("K7", "K7"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "hoist_brake_type",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("AC Disc", "AC Disc"),
                            ("AC Shoe", "AC Shoe"),
                            ("DC Disc", "DC Disc"),
                            ("DC Shoe", "DC Shoe"),
                            ("ETH", "ETH"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "rope_drum_code",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("M4 X 4/1", "M4 X 4/1"),
                            ("M6 X 4/1", "M6 X 4/1"),
                            ("M9 X 4/1", "M9 X 4/1"),
                            ("M12 X 4/1", "M12 X 4/1"),
                            ("M15 X 4/1", "M15 X 4/1"),
                            ("M20 X 4/1", "M20 X 4/1"),
                            ("M25 X 4/1", "M25 X 4/1"),
                            ("M4 X 4/2", "M4 X 4/2"),
                            ("M6 X 4/2", "M6 X 4/2"),
                            ("M9 X 4/2", "M9 X 4/2"),
                            ("M12 X 4/2", "M12 X 4/2"),
                            ("M15 X 4/2", "M15 X 4/2"),
                            ("M20 X 4/2", "M20 X 4/2"),
                            ("M25 X 4/2", "M25 X 4/2"),
                            ("M4 X 2/1", "M4 X 2/1"),
                            ("M6 X 2/1", "M6 X 2/1"),
                            ("M9 X 2/1", "M9 X 2/1"),
                            ("M12 X 2/1", "M12 X 2/1"),
                            ("M15 X 2/1", "M15 X 2/1"),
                            ("M20 X 2/1", "M20 X 2/1"),
                            ("M25 X 2/1", "M25 X 2/1"),
                            ("M9 X 6/2", "M9 X 6/2"),
                            ("M12 X 6/2", "M12 X 6/2"),
                            ("M15 X 6/2", "M15 X 6/2"),
                            ("M20 X 6/2", "M20 X 6/2"),
                            ("M25 X 6/2", "M25 X 6/2"),
                            ("M12 X 8/2", "M12 X 8/2"),
                            ("M15 X 8/2", "M15 X 8/2"),
                            ("M20 X 8/2", "M20 X 8/2"),
                            ("M25 X 8/2", "M25 X 8/2"),
                            ("M12 X 10/2", "M12 X 10/2"),
                            ("M15 X 10/2", "M15 X 10/2"),
                            ("M20 X 10/2", "M20 X 10/2"),
                            ("M25 X 10/2", "M25 X 10/2"),
                            ("M15 X 12/2", "M15 X 12/2"),
                            ("M20 X 12/2", "M20 X 12/2"),
                            ("M25 X 12/2", "M25 X 12/2"),
                            ("Special", "Special"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "rope_reeving",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("RH", "RH"),
                            ("LH", "LH"),
                            ("RH&LH", "RH&LH"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "wire_rope",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Dia 6", "Dia 6"),
                            ("Dia 8", "Dia 8"),
                            ("Dia 10", "Dia 10"),
                            ("Dia 12", "Dia 12"),
                            ("Dia 13", "Dia 13"),
                            ("Dia 16", "Dia 16"),
                            ("Dia 18", "Dia 18"),
                            ("Dia 20", "Dia 20"),
                            ("Dia 22", "Dia 22"),
                            ("Dia 26", "Dia 26"),
                        ],
                        max_length=10,
                    ),
                ),
                ("wire_length", models.IntegerField()),
                (
                    "ct_wheel",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Dia 50", "Dia 50"),
                            ("Dia 100", "Dia 100"),
                            ("Dia 130", "Dia 130"),
                            ("Dia 150", "Dia 150"),
                            ("Dia 180", "Dia 180"),
                            ("Dia 200", "Dia 200"),
                            ("Dia 250", "Dia 250"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "tread",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Flat", "Flat"),
                            ("Taper", "Taper"),
                            ("Special", "Special"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "ct_wheel_type",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("2 + 2 Wheel", "2 + 2 Wheel"),
                            ("4 Wheel", "4 Wheel"),
                            ("6 Wheel", "6 Wheel"),
                            ("8 Wheel", "8 Wheel"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "ct_wheel_type2",
                    models.CharField(
                        choices=[("0", "0"), ("DT", "DT"), ("ST", "ST")], max_length=10
                    ),
                ),
                (
                    "ct_speed",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("8", "8"),
                            ("10", "10"),
                            ("12", "12"),
                            ("14", "14"),
                            ("18", "18"),
                            ("20", "20"),
                            ("14", "14"),
                            ("Manual", "Manual"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "ct_gear_box",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("CT 1", "CT 1"),
                            ("CT 2", "CT 2"),
                            ("CT 3", "CT 3"),
                            ("CT 4", "CT 4"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "ct_motor",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("0.25", "0.25"),
                            ("0.50", "0.50"),
                            ("0.75", "0.75"),
                            ("1.00", "1.00"),
                            ("1.50", "1.50"),
                            ("2.00", "2.00"),
                            ("3.00", "3.00"),
                            ("5.00", "5.00"),
                            ("7.50", "7.50"),
                            ("10.00", "10.00"),
                            ("15.00", "15.00"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "ct_motor_rpm",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("720", "720"),
                            ("960", "960"),
                            ("1440", "1440"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "ct_brake",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("DAT 130", "DAT 130"),
                            ("DAT 150", "DAT 150"),
                            ("DAT 150X", "DAT 150X"),
                            ("DAT 190", "DAT 190"),
                            ("DAT 190X", "DAT 190X"),
                            ("DAT 235", "DAT 235"),
                            ("DAT 235X", "DAT 235X"),
                            ("DAT 290", "DAT 290"),
                            ("DAT 290X", "DAT 290X"),
                            ("DAT 290XX", "DAT 290XX"),
                            ('Dia 4"', 'Dia 4"'),
                            ('Dia 5.5"', 'Dia 5.5"'),
                            ('Dia 7"', 'Dia 7"'),
                            ("K1", "K1"),
                            ("K2", "K2"),
                            ("K3", "K3"),
                            ("K4", "K4"),
                            ("K5", "K5"),
                            ("K6", "K6"),
                            ("K7", "K7"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "ct_brake_type",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("AC Disc", "AC Disc"),
                            ("AC Shoe", "AC Shoe"),
                            ("DC Disc", "DC Disc"),
                            ("DC Shoe", "DC Shoe"),
                            ("ETH", "ETH"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "gravity_type",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Required", "Required"),
                            ("Not Required", "Not Required"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "ct_limit_switch",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Required", "Required"),
                            ("Not Required", "Not Required"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "lt_limit_switch",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Required", "Required"),
                            ("Not Required", "Not Required"),
                        ],
                        max_length=15,
                    ),
                ),
                ("hoist_creep", models.CharField(max_length=100)),
                ("ct_creep", models.CharField(max_length=100)),
                ("lt_creep", models.CharField(max_length=100)),
                ("flange_width", models.IntegerField()),
                (
                    "outdoor_cover",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Required", "Required"),
                            ("Not Required", "Not Required"),
                        ],
                        max_length=15,
                    ),
                ),
                ("notes1", models.TextField(blank=True, null=True)),
                ("notes2", models.TextField(blank=True, null=True)),
                ("notes3", models.TextField(blank=True, null=True)),
                ("notes4", models.TextField(blank=True, null=True)),
                ("notes5", models.TextField(blank=True, null=True)),
                ("notes6", models.TextField(blank=True, null=True)),
                ("notes7", models.TextField(blank=True, null=True)),
                ("notes8", models.TextField(blank=True, null=True)),
                ("notes9", models.TextField(blank=True, null=True)),
                ("notes10", models.TextField(blank=True, null=True)),
                (
                    "packing",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("Required", "Required"),
                            ("Not Required", "Not Required"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "sales_rep",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("AMRK", "AMRK"),
                            ("Direct", "Direct"),
                            ("DNR", "DNR"),
                            ("KMN", "KMN"),
                            ("MSM", "MSM"),
                            ("ARP", "ARP"),
                            ("SKS", "SKS"),
                        ],
                        max_length=10,
                    ),
                ),
                ("transportation", models.CharField(max_length=100)),
                ("issued_to", models.CharField(max_length=100)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workorder.customer",
                    ),
                ),
            ],
        ),
    ]
