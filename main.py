from dotenv import dotenv_values
from google.cloud import iot_v1
from google.cloud.iot_v1.services.device_manager.client import (
    DeviceManagerClient,)

import env

client: DeviceManagerClient = iot_v1.DeviceManagerClient(
    credentials=env.credential())
registry_path = client.registry_path(env.project_id(), env.proejct_region(),
                                     env.registry())


def get_registry():
    """ Retrieves a device registry.
    
    refs: https://github.com/googleapis/python-iot/blob/main/samples/api-client/manager/manager.py
    """
    return client.get_device_registry(request={"name": registry_path},
                                      timeout=3.0)


def main():
    get_registry()


if __name__ == '__main__':
    main()
