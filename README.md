# AnsibleMyNetwork


### Ansible automation for setup, configuration, maintenance and operation of networking appliances like routers, switches, firewalls, load-balancers and other devices.

### Supports General-Purpose Automation: Command-Response over SSH

### Plus vendor-specific support: Cisco, Palo Alto Networks, Checkpoint

*This project is in an early stage and under active development so there will be frequent updates and rapid improvement.*


----


## Network Automation Development Environments

This project is being developed 'virtually' such that I do not currently have access to the target network devices in their physical form, nor do I have access to good emulators. What I do have access to are simulators, which offer a usually precise *manual* CLI interaction for many versions of IOS for Cisco devices and for many other devices by other vendors. I also draw from notes, code, articles and projects from other developers including published CLI interactions and logfiles. These sources allow me to accomplish a lot of development but not a lot of actual testing of complete playbooks against actual target devices.

Even in cases where one has access to a rich corporate network environment with many devices of all kinds to potentially automate, very few of those can be touched outside of very specific required actions becuase most devices are all in active production use. The theme here is that it is very rare to actually have a lab or real environment with lots of devices against which one can develop and test automation. This is an exceedingly rare thing to have access to.

Furthering the challenge, the available options for emulation of devices and network topologies are limited and without significant cost and effort, are essentially non-existent or effectively unusable. For example, of the only good and free option, GNS3, one currently cannot enable connections to emulated devices over WiFi on macOS, which is what almost half of interested developers would want/need to do.

Personally, I will end up using GNS3 because it looks really great for emulating and simulating network devices and complex network topologies, but I will do the following to be able to make a GNS emulated network with many devices work well: I will use a dedicated physical windows/PC host or perhaps a Linux host running VMWare Fusion or Workstation. I will run the PC or Linux version of GNS3 against the GNS3 VM on that host. I will use physical ethernet and not Wifi to connect to the local (WiFi) router. Without going over all the details of my testing and research, this looks like the most promising path, if not the only path, without spending thousands on paid options that may or may not be good for automation development.

Cloud options are almost a non-starter, because GNS3 is not designed to work well with nested virtualization and your host would be a VM running a hypervisor and that is not optimal nor even guaranteed to work, so unless you can afford a metal host in the cloud, VMs in the cloud are not a good option for GNS3 network emulation/simulation, plus cloud connectivity adds unwanted complexity for this use case as well as additional hops and latencies.

Bottom line .. it is very challenging to find a way to actually test/develop automation of network devices and topologies, unless you are on a real corporate network, with real devices which are not currently in production and are thus effectively safe to experiment on. For this reason, I will clearly mark playbooks with their status as to which tasks have or have not been tested on specific physical devices and/or device software versions.

I will test all individual tasks and steps within those tasks which do not require a physical or emulated target device. Stay tuned for more updates on emulation in a new document I will create on this topic. When I get GNS3 working well, I may be able to test everything in this project as I develop it. That is the theory and the goal anyhow.


----


TODO: Incorporate this intro text taken from the AnsibleMyEC2 README.md where this project lived for its first few days:


Goals for the new Network Device Automation playbooks: Manage firewall rules for rapid/frequent response to threat activity. Control Load Balancer configuration for blue/green software deployment. Enable general automation of Cisco IOS devices and those of the most popular vendors. The scope of the resulting project is still being planned.

