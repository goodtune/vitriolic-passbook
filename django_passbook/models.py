from django.db import models


class Pass(models.Model):
    """
    Pass instance
    """
    pass_type_identifier = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    authentication_token = models.CharField(max_length=255)
    data = models.FileField(upload_to='passes')
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.serial_number

    class Meta:
        unique_together = (('pass_type_identifier', 'serial_number'),)
        verbose_name = 'passes'


class Registration(models.Model):
    """
    Registration of a Pass on a device
    """
    device_library_identifier = models.CharField(max_length=64)
    push_token = models.TextField()
    pazz = models.ForeignKey(Pass, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.device_library_identifier


class Log(models.Model):
    """
    Log message sent by a device
    """
    message = models.TextField()

    def __unicode__(self):
        return self.message
