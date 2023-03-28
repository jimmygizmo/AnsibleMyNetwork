import pexpect

switch_ip = "10.0.0.1"
switch_un = "user"
switch_pw = "s3cr3t"
switch_enable_pw = "m0r3s3cr3t"
port = "Gi2/0/2"
vlan = 300


# https://www.electricmonk.nl/log/2014/07/26/scripting-a-cisco-switch-with-python-and-expect/


try:
    try:
        child = pexpect.spawn('ssh %s@%s' % (switch_un, switch_ip))
        if verbose:
            child.logfile = sys.stdout
        child.timeout = 4
        child.expect('Password:')
    except pexpect.TIMEOUT:
        raise OurException("Couldn't log on to the switch")

    child.sendline(switch_pw)
    child.expect('>')
    child.sendline('terminal length 0')
    child.expect('>')
    child.sendline('enable')
    child.expect('Password:')
    child.sendline(switch_enable_pw)
    child.expect('#')
    child.sendline('conf t')
    child.expect('\(config\)#')
    child.sendline('interface %s' % (port))
    o = child.expect(['\(config-if\)#', '% Invalid'])
    if o != 0:
        raise Exception("Unknown switch port '%s'" % (port))
    child.sendline('switchport access vlan %s' % (vlan))
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
    error("Error while trying to move the vlan on the switch.")
    raise
