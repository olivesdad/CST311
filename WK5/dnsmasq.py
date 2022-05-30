#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/24')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    r4 = net.addHost('r4', cls=Node, ip='10.0.0.1/24', defaultRoute='via 192.168.200.1')
    r4.cmd('sysctl -w net.ipv4.ip_forward=1')
    r3 = net.addHost('r3', cls=Node, ip='10.0.2.1/24', defaultRoute='via 192.168.200.2')
    r3.cmd('sysctl -w net.ipv4.ip_forward=1')
    
    info( '*** Add hosts\n')
    h2 = net.addHost('h2', cls=Host, ip='0.0.0.0/24')
    h3 = net.addHost('h3', cls=Host, ip='10.0.2.11/24', defaultRoute='via 10.0.2.1')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.11/24', defaultRoute='via 10.0.0.1')
    h4 = net.addHost('h4', cls=Host, ip='0.0.0.0/24')

    info( '*** Add links\n')
    net.addLink(h1, s2)
    net.addLink(h2, s2)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.addLink(s2, r4, intfName2='r4-eth1', params2={ 'ip' : '10.0.0.1/24' } )     
    net.addLink(s1, r3, intfName2='r3-eth1', params2={ 'ip' : '10.0.2.1/24' } ) 
    net.addLink(r3, r4, intfName1='r3-eth2', params1={ 'ip' : '192.168.200.1/30' }, intfName2='r4-eth2', params2={ 'ip' : '192.168.200.2/30' } )
   
    
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

