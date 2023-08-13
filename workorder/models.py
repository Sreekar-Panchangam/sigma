from django.db import models

class Customer(models.Model):
    TITLE_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss.', 'Miss.'),
        ('Dr.', 'Dr.'),
    ]

    STATE_CHOICES = [
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default='Karnataka')
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    gstin = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.name}"



class HoistWorkOrder(models.Model):
    HOIST_SIZE_CHOICES = [
        ('0', '0'),
        ('250', '250'),
        ('280', '280'),
        ('350', '350'),
        ('380', '380'),
        ('430', '430'),
        ('530', '530'),
        ('680', '680'),
        ('730', '730'),
        ('830', '830'),
        ('I-Lift', 'I-Lift'),
    ]

    CAPACITY_CHOICES = [
        ('0', '0'),
        ('250', '250'),
        ('500', '500'),
        ('1000', '1000'),
        ('2000', '2000'),
        ('3000', '3000'),
        ('5000', '5000'),
        ('7500', '7500'),
        ('10000', '10000'),
        ('15000', '15000'),
        ('20000', '20000'),
        ('25000', '25000'),
        ('30000', '30000'),
    ]

    HEIGHT_CHOICES = [
        ('0', '0'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('8', '8'),
        ('9', '9'),
        ('12', '12'),
        ('15', '15'),
        ('18', '18'),
        ('20', '20'),
        ('24', '24'),
        ('25', '25'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
    ]

    FALL_CHOICES = [
        ('0', '0'),
        ('1/1', '1/1'),
        ('2/1', '2/1'),
        ('4/1', '4/1'),
        ('4/2', '4/2'),
        ('6/2', '6/2'),
        ('8/2', '8/2'),
        ('10/2', '10/2'),
        ('12/2', '12/2'),
        ('16/2', '16/2'),
    ]

    TROLLEY_TYPE_CHOICES = [
        ('0', '0'),
        ('Foot Mounted', 'Foot Mounted'),
        ('Hand Geared', 'Hand Geared'),
        ('Lug Mounted', 'Lug Mounted'),
        ('Motorized', 'Motorized'),
        ('Push Pull', 'Push Pull'),
    ]

    ADDITIONAL_FEATURE_CHOICES = [
        ('0', '0'),
        ('Extended Trolley', 'Extended Trolley'),
        ('Flame Proof', 'Flame Proof'),
        ('Flexible Trolley', 'Flexible Trolley'),
        ('Standard', 'Standard'),
    ]

    HOIST_SPEED_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('1.3', '1.3'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('9', '9'),
        ('12', '12'),
    ]

    HOIST_MOTOR_CHOICES = [
        ('0', '0'),
        ('0.25', '0.25'),
        ('0.50', '0.50'),
        ('0.75', '0.75'),
        ('1.00', '1.00'),
        ('1.50', '1.50'),
        ('2.00', '2.00'),
        ('3.00', '3.00'),
        ('5.00', '5.00'),
        ('7.50', '7.50'),
        ('10.00', '10.00'),
        ('15.00', '15.00'),
    ]

    HOIST_MOTOR_RPM_CHOICES = [
        ('0', '0'),
        ('720', '720'),
        ('960', '960'),
        ('1440', '1440'),
    ]

    HOIST_BRAKE_CHOICES = [
        ('0', '0'),
        ('DAT 130', 'DAT 130'),
        ('DAT 150', 'DAT 150'),
        ('DAT 150X', 'DAT 150X'),
        ('DAT 190', 'DAT 190'),
        ('DAT 190X', 'DAT 190X'),
        ('DAT 235', 'DAT 235'),
        ('DAT 235X', 'DAT 235X'),
        ('DAT 290', 'DAT 290'),
        ('DAT 290X', 'DAT 290X'),
        ('DAT 290XX', 'DAT 290XX'),
        ('Dia 4"', 'Dia 4"'),
        ('Dia 5.5"', 'Dia 5.5"'),
        ('Dia 7"', 'Dia 7"'),
        ('K1', 'K1'),
        ('K2', 'K2'),
        ('K3', 'K3'),
        ('K4', 'K4'),
        ('K5', 'K5'),
        ('K6', 'K6'),
        ('K7', 'K7'),
    ]

    HOIST_BRAKE_TYPE_CHOICES = [
        ('0', '0'),
        ('AC Disc', 'AC Disc'),
        ('AC Shoe', 'AC Shoe'),
        ('DC Disc', 'DC Disc'),
        ('DC Shoe', 'DC Shoe'),
        ('ETH', 'ETH'),
    ]

    ROPE_DRUM_CODE_CHOICES = [
        ('0', '0'),
        ('M4 X 4/1', 'M4 X 4/1'),
        ('M6 X 4/1', 'M6 X 4/1'),
        ('M9 X 4/1', 'M9 X 4/1'),
        ('M12 X 4/1', 'M12 X 4/1'),
        ('M15 X 4/1', 'M15 X 4/1'),
        ('M20 X 4/1', 'M20 X 4/1'),
        ('M25 X 4/1', 'M25 X 4/1'),
        ('M4 X 4/2', 'M4 X 4/2'),
        ('M6 X 4/2', 'M6 X 4/2'),
        ('M9 X 4/2', 'M9 X 4/2'),
        ('M12 X 4/2', 'M12 X 4/2'),
        ('M15 X 4/2', 'M15 X 4/2'),
        ('M20 X 4/2', 'M20 X 4/2'),
        ('M25 X 4/2', 'M25 X 4/2'),
        ('M4 X 2/1', 'M4 X 2/1'),
        ('M6 X 2/1', 'M6 X 2/1'),
        ('M9 X 2/1', 'M9 X 2/1'),
        ('M12 X 2/1', 'M12 X 2/1'),
        ('M15 X 2/1', 'M15 X 2/1'),
        ('M20 X 2/1', 'M20 X 2/1'),
        ('M25 X 2/1', 'M25 X 2/1'),
        ('M9 X 6/2', 'M9 X 6/2'),
        ('M12 X 6/2', 'M12 X 6/2'),
        ('M15 X 6/2', 'M15 X 6/2'),
        ('M20 X 6/2', 'M20 X 6/2'),
        ('M25 X 6/2', 'M25 X 6/2'),
        ('M12 X 8/2', 'M12 X 8/2'),
        ('M15 X 8/2', 'M15 X 8/2'),
        ('M20 X 8/2', 'M20 X 8/2'),
        ('M25 X 8/2', 'M25 X 8/2'),
        ('M12 X 10/2', 'M12 X 10/2'),
        ('M15 X 10/2', 'M15 X 10/2'),
        ('M20 X 10/2', 'M20 X 10/2'),
        ('M25 X 10/2', 'M25 X 10/2'),
        ('M15 X 12/2', 'M15 X 12/2'),
        ('M20 X 12/2', 'M20 X 12/2'),
        ('M25 X 12/2', 'M25 X 12/2'),
        ('Special', 'Special'),
    ]

    ROPE_REEVING_CHOICES = [
        ('0', '0'),
        ('RH', 'RH'),
        ('LH', 'LH'),
        ('RH&LH', 'RH&LH'),
    ]

    WIRE_ROPE_CHOICES = [
        ('0', '0'),
        ('Dia 6', 'Dia 6'),
        ('Dia 8', 'Dia 8'),
        ('Dia 10', 'Dia 10'),
        ('Dia 12', 'Dia 12'),
        ('Dia 13', 'Dia 13'),
        ('Dia 16', 'Dia 16'),
        ('Dia 18', 'Dia 18'),
        ('Dia 20', 'Dia 20'),
        ('Dia 22', 'Dia 22'),
        ('Dia 26', 'Dia 26'),
    ]

    CT_WHEEL_CHOICES = [
        ('0', '0'),
        ('Dia 50', 'Dia 50'),
        ('Dia 100', 'Dia 100'),
        ('Dia 130', 'Dia 130'),
        ('Dia 150', 'Dia 150'),
        ('Dia 180', 'Dia 180'),
        ('Dia 200', 'Dia 200'),
        ('Dia 250', 'Dia 250'),
    ]

    TREAD_CHOICES = [
        ('0', '0'),
        ('Flat', 'Flat'),
        ('Taper', 'Taper'),
        ('Special', 'Special'),
    ]

    CT_WHEEL_TYPE_CHOICES = [
        ('0', '0'),
        ('2 + 2 Wheel', '2 + 2 Wheel'),
        ('4 Wheel', '4 Wheel'),
        ('6 Wheel', '6 Wheel'),
        ('8 Wheel', '8 Wheel'),
    ]

    CT_WHEEL_TYPE2_CHOICES = [
        ('0', '0'),
        ('DT', 'DT'),
        ('ST', 'ST'),
    ]

    CT_SPEED_CHOICES = [
        ('0', '0'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('18', '18'),
        ('20', '20'),
        ('14', '14'),
        ('Manual', 'Manual'),
    ]

    CT_GEAR_BOX_CHOICES = [
        ('0', '0'),
        ('CT 1', 'CT 1'),
        ('CT 2', 'CT 2'),
        ('CT 3', 'CT 3'),
        ('CT 4', 'CT 4'),
    ]

    CT_MOTOR_CHOICES = [
        ('0', '0'),
        ('0.25', '0.25'),
        ('0.50', '0.50'),
        ('0.75', '0.75'),
        ('1.00', '1.00'),
        ('1.50', '1.50'),
        ('2.00', '2.00'),
        ('3.00', '3.00'),
        ('5.00', '5.00'),
        ('7.50', '7.50'),
        ('10.00', '10.00'),
        ('15.00', '15.00'),
    ]

    CT_MOTOR_RPM_CHOICES = [
        ('0', '0'),
        ('720', '720'),
        ('960', '960'),
        ('1440', '1440'),
    ]

    CT_BRAKE_CHOICES = [
        ('0', '0'),
        ('DAT 130', 'DAT 130'),
        ('DAT 150', 'DAT 150'),
        ('DAT 150X', 'DAT 150X'),
        ('DAT 190', 'DAT 190'),
        ('DAT 190X', 'DAT 190X'),
        ('DAT 235', 'DAT 235'),
        ('DAT 235X', 'DAT 235X'),
        ('DAT 290', 'DAT 290'),
        ('DAT 290X', 'DAT 290X'),
        ('DAT 290XX', 'DAT 290XX'),
        ('Dia 4"', 'Dia 4"'),
        ('Dia 5.5"', 'Dia 5.5"'),
        ('Dia 7"', 'Dia 7"'),
        ('K1', 'K1'),
        ('K2', 'K2'),
        ('K3', 'K3'),
        ('K4', 'K4'),
        ('K5', 'K5'),
        ('K6', 'K6'),
        ('K7', 'K7'),
    ]

    CT_BRAKE_TYPE_CHOICES = [
        ('0', '0'),
        ('AC Disc', 'AC Disc'),
        ('AC Shoe', 'AC Shoe'),
        ('DC Disc', 'DC Disc'),
        ('DC Shoe', 'DC Shoe'),
        ('ETH', 'ETH'),
    ]

    GRAVITY_TYPE_CHOICES = [
        ('0', '0'),
        ('Required', 'Required'),
        ('Not Required', 'Not Required'),
    ]

    CT_LIMIT_SWITCH_CHOICES = [
        ('0', '0'),
        ('Required', 'Required'),
        ('Not Required', 'Not Required'),
    ]

    LT_LIMIT_SWITCH_CHOICES = [
        ('0', '0'),
        ('Required', 'Required'),
        ('Not Required', 'Not Required'),
    ]

    SALES_REP_CHOICES = [
        ('0','0'),
        ('AMRK','AMRK'),
        ('Direct','Direct'),
        ('DNR','DNR'),
        ('KMN','KMN'),
        ('MSM','MSM'),
        ('ARP','ARP'),
        ('SKS','SKS'),
    ]

    Work_Order_Number = models.IntegerField(unique=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    P_O_Number = models.CharField(max_length=100)
    P_O_Date = models.DateField()
    delivery_date = models.DateField()
    hoist_size = models.CharField(max_length=10, choices=HOIST_SIZE_CHOICES)
    quantity = models.IntegerField()
    capacity = models.CharField(max_length=10, choices=CAPACITY_CHOICES)
    height = models.CharField(max_length=10, choices=HEIGHT_CHOICES)
    fall = models.CharField(max_length=10, choices=FALL_CHOICES)
    hoist_code = models.CharField(max_length=100)
    trolley_type = models.CharField(max_length=100, choices=TROLLEY_TYPE_CHOICES)
    additional_feature = models.CharField(max_length=100, choices=ADDITIONAL_FEATURE_CHOICES)
    hoist_speed = models.CharField(max_length=10, choices=HOIST_SPEED_CHOICES)
    hoist_motor = models.CharField(max_length=10, choices=HOIST_MOTOR_CHOICES)
    hoist_motor_rpm = models.CharField(max_length=10, choices=HOIST_MOTOR_RPM_CHOICES)
    hoist_brake = models.CharField(max_length=100, choices=HOIST_BRAKE_CHOICES)
    hoist_brake_type = models.CharField(max_length=100, choices=HOIST_BRAKE_TYPE_CHOICES)
    rope_drum_code = models.CharField(max_length=100, choices=ROPE_DRUM_CODE_CHOICES)
    rope_reeving = models.CharField(max_length=10, choices=ROPE_REEVING_CHOICES)
    wire_rope = models.CharField(max_length=10, choices=WIRE_ROPE_CHOICES)
    wire_length = models.IntegerField()
    C_T_wheel = models.CharField(max_length=10, choices=CT_WHEEL_CHOICES)
    tread = models.CharField(max_length=10, choices=TREAD_CHOICES)
    C_T_wheel_type = models.CharField(max_length=15, choices=CT_WHEEL_TYPE_CHOICES)
    C_T_wheel_type_2 = models.CharField(max_length=10, choices=CT_WHEEL_TYPE2_CHOICES)
    C_T_speed = models.CharField(max_length=10, choices=CT_SPEED_CHOICES)
    C_T_gear_box = models.CharField(max_length=10, choices=CT_GEAR_BOX_CHOICES)
    C_T_motor = models.CharField(max_length=10, choices=CT_MOTOR_CHOICES)
    C_T_motor_rpm = models.CharField(max_length=10, choices=CT_MOTOR_RPM_CHOICES)
    C_T_brake = models.CharField(max_length=100, choices=CT_BRAKE_CHOICES)
    C_T_brake_type = models.CharField(max_length=100, choices=CT_BRAKE_TYPE_CHOICES)
    gravity_type = models.CharField(max_length=15, choices=GRAVITY_TYPE_CHOICES, blank=True, null=True)
    C_T_limit_switch = models.CharField(max_length=15, choices=CT_LIMIT_SWITCH_CHOICES, blank=True, null=True)
    L_T_limit_switch = models.CharField(max_length=15, choices=LT_LIMIT_SWITCH_CHOICES, blank=True, null=True)
    hoist_creep = models.CharField(max_length=100, blank=True, null=True)
    C_T_creep = models.CharField(max_length=100, blank=True, null=True)
    L_T_creep = models.CharField(max_length=100, blank=True, null=True)
    flange_width = models.IntegerField()
    outdoor_cover = models.CharField(max_length=15, choices=GRAVITY_TYPE_CHOICES)
    notes_1 = models.TextField(blank=True, null=True)
    notes_2 = models.TextField(blank=True, null=True)
    notes_3 = models.TextField(blank=True, null=True)
    notes_4 = models.TextField(blank=True, null=True)
    notes_5 = models.TextField(blank=True, null=True)
    notes_6 = models.TextField(blank=True, null=True)
    notes_7 = models.TextField(blank=True, null=True)
    notes_8 = models.TextField(blank=True, null=True)
    packing = models.CharField(max_length=15, choices=GRAVITY_TYPE_CHOICES)
    sales_rep = models.CharField(max_length=10, choices=SALES_REP_CHOICES)
    transportation = models.CharField(max_length=100)
    issued_to = models.CharField(max_length=100)

    def __str__(self):
        return f"Work Order {self.Work_Order_Number}"
