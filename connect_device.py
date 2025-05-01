from netmiko import ConnectHandler

# Define the device connection parameters
device = {
    'device_type': 'cisco_ios',  # Cisco IOS device type
    'host': 'devnetsandboxiosxe.cisco.com',  # Public URL of the sandbox
    'username': 'admin',  # Username for authentication
    'password': 'C1sco12345',  # Password for authentication
    'port': 22,  # SSH port
    'secret': '',  # Enable password (if any), leave blank if not required
}

# Establish the connection to the device
net_connect = ConnectHandler(**device)

# Enter privileged EXEC mode (enable mode) if needed
net_connect.enable()

# Send a simple command to retrieve the device information
output = net_connect.send_command('show version')  # This command will return device version info
output = net_connect.send_command('show ip interface brief')
print(output)


# Print the output of the command
print(output)

# Disconnect after the session
net_connect.disconnect()
