import factory
from Asset_Tracker.models import Device


class DeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Device

    name = 'Test Device'
    model_number = 'TD-123'
    description = "Purchased from ABC company"
    serial_number = '1234'
    condition = 'Good'
    checked_out = False
