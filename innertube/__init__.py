from . import devices
from . import services
from . import utils
from . import clients
from . import infos
from . import info

# def get_client(*, service: info.ServiceInfo, device: info.DeviceInfo):
    # client_info = utils.get_client_info \
    # (
    #     service = service.type,
    #     device  = device.type,
    # )
    #
    # for identifier in dir(infos):
    #     if getattr(infos, identifier) == client_info:
    #         break
    # else:
    #     return
    #
    # client = getattr(clients, identifier, None)
    #
    # if client: return client()
