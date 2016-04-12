# required import! Contains handler map
import cloudshell.networking.cisco.ios.extended.resource_drivers
from cloudshell.networking.resource_driver.networking_generic_resource_driver import networking_generic_resource_driver
from cloudshell.shell.core.driver_builder_wrapper import DriverFunction


class cisco_generic_ios_resource_driver_extended(networking_generic_resource_driver):
    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def Init(self, matrixJSON):
        self.handler_name = 'ios_ext'
        networking_generic_resource_driver.Init(self, matrixJSON)


    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def ConfigureInterfaceSpeed(self, matrixJSON, port_list):
        self._check_for_attributes_changes(matrixJSON)
        result = self._resource_handler.configure_interface_speed(port_list)
        return self._resource_handler.normalize_output(result)


    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def ConfigureInterfaceMtu(self, matrixJSON, port_list):
        self._check_for_attributes_changes(matrixJSON)
        result = self._resource_handler.configure_interface_mtu(port_list)
        return self._resource_handler.normalize_output(result)


    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def CreatePortchannel(self, matrixJSON, port_list):
        self._check_for_attributes_changes(matrixJSON)
        result = self._resource_handler.create_portchannel(port_list)
        return self._resource_handler.normalize_output(result)


    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def DeletePortchannel(self, matrixJSON, port_list):
        self._check_for_attributes_changes(matrixJSON)
        result = self._resource_handler.delete_portchannel(port_list)
        return self._resource_handler.normalize_output(result)


    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def RestorePortConfig(self, matrixJSON, source_file, port_list):
        self._check_for_attributes_changes(matrixJSON)
        result = self._resource_handler.restore_port_config(source_file, port_list)
        return self._resource_handler.normalize_output(result)




if __name__ == '__main__':

    data_json = str("""{
            "resource" : {

                    "ResourceAddress": "10.89.143.225",
                    "User": "quali",
                    "Password": "Password2",
                    "CLI Connection Type": "SSH",
                    "Console User": "",
                    "Console Password": "",
                    "Console Server IP Address": "",
                    "ResourceName" : "sw9003-if-10-3.cisco.com",
                    "ResourceFullName" : "sw9003-if-10-3.cisco.com",
                    "Enable Password": "",
                    "Console Port": "",
                    "SNMP Read Community": "stargate",
                    "SNMP Version": "2",
                    "SNMP V3 Password": "",
                    "SNMP V3 User": "",
                    "SNMP V3 Private Key": ""
                },
            "reservation" : {
                    "ReservationId" : "d1229816-5856-4e8d-a094-51aacfbec50b",
                    "Username" : "admin",
                    "Password" : "admin",
                    "Domain" : "Global",
                    "AdminUsername" : "admin",
                    "AdminPassword" : "admin"}
            }""")

    resource_driver = cisco_generic_ios_resource_driver_extended('77', data_json)
    # print resource_driver.GetInventory(data_json)
    # print resource_driver.Add_VLAN(data_json, '10.89.143.225/0/1/5|10.89.143.225/0/1/6', '45', 'trunk', '')
    # print resource_driver.Add_VLAN(data_json, '10.89.143.225/PC22', '45', 'trunk', '')
    # import sys; sys.exit()
    # print resource_driver.ConfigureInterfaceSpeed(data_json, 'gigabitEthernet 1/1|gig 1/2', '1000')

    print resource_driver.CreatePortchannel(data_json, 'Shell/sw9003-if-10-3.cisco.com/Chassis 0/Module 1/GigabitEthernet1-5;Shell/sw9003-if-10-3.cisco.com/Chassis 0/Module 1/GigabitEthernet1-6' )
    # print resource_driver.DeletePortchannel(data_json, 'Shell/sw9003-if-10-3.cisco.com/Chassis 0/Module 1/GigabitEthernet1-5;Shell/sw9003-if-10-3.cisco.com/Chassis 0/Module 1/GigabitEthernet1-6' )
