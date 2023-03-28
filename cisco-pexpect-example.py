import sys
import pexpect

verbose = True
cisco_switch_ip = "10.0.0.1"
cisco_switch_user = "user"
cisco_switch_password = "__cisco_switch_password__"
cisco_switch_enable_password = "__cisco_switch_enable_password__"
cisco_switch_interface = "Gi2/0/2"
cisco_switch_vlan = 300


try:
    try:
        child = pexpect.spawn('ssh %s@%s' % (cisco_switch_user, cisco_switch_ip))
        if verbose:
            child.logfile = sys.stdout
        child.timeout = 4
        child.expect('Password:')
        
    except pexpect.TIMEOUT:
        raise Exception("Couldn't log on to the switch")

    child.sendline(cisco_switch_password)

    child.expect('>')
    child.sendline('terminal length 0')

    child.expect('>')
    child.sendline('enable')

    child.expect('Password:')
    child.sendline(cisco_switch_enable_password)

    child.expect('#')
    child.sendline('conf t')

    child.expect('\(config\)#')
    child.sendline('interface %s' % cisco_switch_interface)

    o = child.expect(['\(config-if\)#', '% Invalid'])
    if o != 0:
        raise Exception("Unknown switch port/interface '%s'" % cisco_switch_interface)

    child.sendline('switchport access vlan %s' % cisco_switch_vlan)

    child.expect('\(config-if\)#')
    child.sendline('no shutdown')

    child.expect('#')
    child.sendline('end')

    child.expect('#')
    child.sendline('wr mem')

    child.expect('[OK]')
    child.expect('#')
    child.sendline('quit')

except (pexpect.EOF, pexpect.TIMEOUT) as e:
    # Not sure what error() is. Came from example code. Changed it to a raise Exception()
    # error("Error while trying to move the vlan on the switch.")
    # raise
    # raise Exception("Error while trying to move the vlan on the switch.", e)  # Pass e as second arg?
    raise Exception("Error while trying to move the vlan on the switch.")

