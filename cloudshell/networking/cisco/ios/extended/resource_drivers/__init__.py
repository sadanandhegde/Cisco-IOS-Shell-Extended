from cloudshell.networking.cisco.ios.extended.cisco_ios_handler_extended import CiscoIOSHandlerExtended
from cloudshell.shell.core.handler_factory import HandlerFactory
from cloudshell.networking.cisco.resource_drivers_map import CISCO_RESOURCE_DRIVERS_MAP
from cloudshell.networking.platform_detector.hardware_platform_detector import HardwarePlatformDetector

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

HandlerFactory.handler_classes['CATALYST_2950'] = CiscoIOSHandlerExtended
HandlerFactory.handler_classes['CATALYST_3560'] = CiscoIOSHandlerExtended
HandlerFactory.handler_classes['CATALYST_3850'] = CiscoIOSHandlerExtended
HandlerFactory.handler_classes['IOS_EXT'] = CiscoIOSHandlerExtended
HardwarePlatformDetector.RESOURCE_DRIVERS_MAP = CISCO_RESOURCE_DRIVERS_MAP
