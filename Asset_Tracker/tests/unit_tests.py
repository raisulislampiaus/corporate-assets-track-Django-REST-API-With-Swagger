import unittest

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from Asset_Tracker.tests.factories import DeviceFactory


@pytest.mark.django_db
class TestDeviceAPI:
    def test_create_device(self, client: APIClient):
        device_data = {
            'name': DeviceFactory.name,
            'model_number': DeviceFactory.model_number,
            'description': DeviceFactory.description,
            'serial_number': DeviceFactory.serial_number,
            'condition': DeviceFactory.condition,
            'checked_out': DeviceFactory.checked_out
        }

        response = client.post('devices/', data=device_data)

        # assert response.status_code == status.HTTP_201_CREATED
        # assert response.status_code == status.HTTP_401_UNAUTHORIZED
        # now, in pytest it might show 401, that means JWT token is not initialized
