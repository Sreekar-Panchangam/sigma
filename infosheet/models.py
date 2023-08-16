from django.db import models
from workorder.models import HoistWorkOrder

# Create your models here.
class HoistInformationSheet(models.Model):
    # Foreign Key
    work_order = models.ForeignKey(HoistWorkOrder, on_delete=models.CASCADE)

    # General Information
    serial_number = models.CharField(max_length=100, unique=True)
    dispatch_date = models.DateField()

    # Gear Box & Drum
    gearbox_stages = models.CharField(max_length=100)
    heat_treatment = models.CharField(max_length=20, choices=[('Soft Gears', 'Soft Gears'), ('Hardened', 'Hardened')])
    rope_drum_dia = models.CharField(max_length=100)
    drum_length = models.CharField(max_length=100)
    drum_pitch = models.CharField(max_length=100)
    rope_guide_id = models.CharField(max_length=100)
    guide_thread_depth = models.CharField(max_length=100)
    guide_thread_pitch = models.CharField(max_length=100)

    # Bottom Block & Idler
    sheave_dia = models.CharField(max_length=100, blank=True, null=True)
    no_of_sheaves = models.CharField(max_length=100, blank=True, null=True)
    sheave_covers = models.CharField(max_length=100, blank=True, null=True)
    idler_sheave_dia = models.CharField(max_length=100, blank=True, null=True)
    no_of_idler = models.CharField(max_length=100, blank=True, null=True)
    hook_type = models.CharField(max_length=100, blank=True, null=True)
    no_of_gear_box = models.CharField(max_length=100, blank=True, null=True)

    # Electricals
    motor_mh_serial_number = models.CharField(max_length=100)
    motor_mh_make = models.CharField(max_length=100)
    motor_ct_serial_number = models.CharField(max_length=100)
    motor_ct_make = models.CharField(max_length=100)
    brake_mh_serial_number = models.CharField(max_length=100)
    brake_mh_make = models.CharField(max_length=100)
    brake_ct_serial_number = models.CharField(max_length=100)
    brake_ct_make = models.CharField(max_length=100)

    # Limit Switch Information
    hoisting_limit_switch_type = models.CharField(max_length=100, blank=True, null=True)
    hoisting_limit_switch_serial_number = models.CharField(max_length=100, blank=True, null=True)
    hoisting_limit_switch_make = models.CharField(max_length=100, blank=True, null=True)
    ct_limit_switch_type = models.CharField(max_length=100, blank=True, null=True)
    ct_limit_switch_serial_number = models.CharField(max_length=100, blank=True, null=True)
    ct_limit_switch_make = models.CharField(max_length=100, blank=True, null=True)

    # Control Panel & Pendent
    control_panel_type = models.CharField(max_length=100, blank=True, null=True)
    control_panel_make = models.CharField(max_length=100, blank=True, null=True)
    pendent_type = models.CharField(max_length=100, blank=True, null=True)
    pendent_make = models.CharField(max_length=100, blank=True, null=True)

    # VFD Information
    hoist_vfd_model = models.CharField(max_length=100, blank=True, null=True)
    hoist_vfd_type = models.CharField(max_length=100, blank=True, null=True)
    hoist_vfd_make = models.CharField(max_length=100, blank=True, null=True)
    ct_vfd_model = models.CharField(max_length=100, blank=True, null=True)
    ct_vfd_type = models.CharField(max_length=100, blank=True, null=True)
    ct_vfd_make = models.CharField(max_length=100, blank=True, null=True)
    lt_vfd_model = models.CharField(max_length=100, blank=True, null=True)
    lt_vfd_type = models.CharField(max_length=100, blank=True, null=True)
    lt_vfd_make = models.CharField(max_length=100, blank=True, null=True)

    # Additional Information
    additional_information = models.TextField()
    fitter_name = models.CharField(max_length=100)
    engineer_in_charge = models.CharField(max_length=100)

    # Test Certificate
    proof_of_load_applied = models.CharField(max_length=100, blank=True, null=True)
    date_of_test = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.serial_number
