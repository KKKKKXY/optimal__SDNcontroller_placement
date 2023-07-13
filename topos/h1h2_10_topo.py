#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

TOPOS = {'mytopo' : (lambda : multiControllerNet())}

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=RemoteController, switch=OVSKernelSwitch, waitConnected=True )

    info( "*** Creating (reference) controllers\n" )
    c1 = net.addController('c1', controller=RemoteController, ip="172.20.0.4", port=6653)
    c2 = net.addController('c2', controller=RemoteController, ip="172.20.0.5", port=6653)
    c3 = net.addController('c3', controller=RemoteController, ip="172.20.0.6", port=6653)
    c4 = net.addController('c4', controller=RemoteController, ip="172.20.0.7", port=6653)
    c5 = net.addController('c5', controller=RemoteController, ip="172.20.0.8", port=6653)
    c6 = net.addController('c6', controller=RemoteController, ip="172.20.0.9", port=6653)
    c7 = net.addController('c7', controller=RemoteController, ip="172.20.0.10", port=6653)
    c8 = net.addController('c8', controller=RemoteController, ip="172.20.0.11", port=6653)
    c9 = net.addController('c9', controller=RemoteController, ip="172.20.0.12", port=6653)
    c10 = net.addController('c10', controller=RemoteController, ip="172.20.0.13", port=6653)

    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1', protocols="OpenFlow13"  )
    s2 = net.addSwitch( 's2', protocols="OpenFlow13"  )
    s3 = net.addSwitch( 's3', protocols="OpenFlow13"  )
    s4 = net.addSwitch( 's4', protocols="OpenFlow13"  )
    s5 = net.addSwitch( 's5', protocols="OpenFlow13"  )
    s6 = net.addSwitch( 's6', protocols="OpenFlow13"  )
    s7 = net.addSwitch( 's7', protocols="OpenFlow13"  )
    s8 = net.addSwitch( 's8', protocols="OpenFlow13"  )
    s9 = net.addSwitch( 's9', protocols="OpenFlow13"  )
    s10 = net.addSwitch( 's10', protocols="OpenFlow13"  )

    info( "*** Creating hosts\n" )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )

    info( "*** Creating links\n" )
    s1.linkTo( h1 )
    s2.linkTo( h2 )
    s1.linkTo( s3 )
    s3.linkTo( s4 )
    s4.linkTo( s5 )
    s5.linkTo( s6 )
    s6.linkTo( s7 )
    s7.linkTo( s8 )
    s8.linkTo( s9 )
    s9.linkTo( s10 )
    s10.linkTo( s2 )

    info( "*** Starting network\n" )
    net.build()
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c5.start()
    c6.start()
    c7.start()
    c8.start()
    c9.start()
    c10.start()
    s1.start( [ c1 ] )
    s2.start( [ c2 ] )
    s3.start( [ c3 ] )
    s4.start( [ c4 ] )
    s5.start( [ c5 ] )
    s6.start( [ c6 ] )
    s7.start( [ c7 ] )
    s8.start( [ c8 ] )
    s9.start( [ c9 ] )
    s10.start( [ c10 ] )

    net.start()

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()