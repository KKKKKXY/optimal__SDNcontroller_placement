from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import time
from datetime import datetime

TOPOS = {'mytopo' : (lambda : multiControllerNet())}

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=RemoteController, switch=OVSKernelSwitch, waitConnected=True, link=TCLink )

    info( "*** Creating (reference) controllers\n" )
    # 3 Atomix nodes(2,3,4)
    c1 = net.addController('c1', controller=RemoteController, ip="172.20.0.5", port=6653)
    c2 = net.addController('c2', controller=RemoteController, ip="172.20.0.6", port=6653)
    c3 = net.addController('c3', controller=RemoteController, ip="172.20.0.7", port=6653)
    c4 = net.addController('c4', controller=RemoteController, ip="172.20.0.8", port=6653)

    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1', protocols="OpenFlow13" )
    s2 = net.addSwitch( 's2', protocols="OpenFlow13" )
    s3 = net.addSwitch( 's3', protocols="OpenFlow13" )
    s4 = net.addSwitch( 's4', protocols="OpenFlow13" )
    s5 = net.addSwitch( 's5', protocols="OpenFlow13" )
    s6 = net.addSwitch( 's6', protocols="OpenFlow13" )
    s7 = net.addSwitch( 's7', protocols="OpenFlow13" )
    s8 = net.addSwitch( 's8', protocols="OpenFlow13" )

    s9 = net.addSwitch( 's9', protocols="OpenFlow13" )
    s10 = net.addSwitch( 's10', protocols="OpenFlow13" )
    s11 = net.addSwitch( 's11', protocols="OpenFlow13" )
    s12 = net.addSwitch( 's12', protocols="OpenFlow13" )
    s13 = net.addSwitch( 's13', protocols="OpenFlow13" )
    s14 = net.addSwitch( 's14', protocols="OpenFlow13" )
    s15 = net.addSwitch( 's15', protocols="OpenFlow13" )
    s16 = net.addSwitch( 's16', protocols="OpenFlow13" )

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
    s10.linkTo( s11 )
    s11.linkTo( s12 )
    s12.linkTo( s13 )
    s13.linkTo( s14 )
    s14.linkTo( s15 )
    s15.linkTo( s16 )
    s16.linkTo( s2 )

    info( "*** Starting network\n" )
    net.build()
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    s1.start( [ c1 ] )
    s3.start( [ c1 ] )
    s4.start( [ c2 ] )
    s5.start( [ c2 ] )
    s6.start( [ c3 ] )
    s7.start( [ c3 ] )
    s8.start( [ c4 ] )
    s9.start( [ c4 ] )
    s10.start( [ c1 ] )
    s11.start( [ c1 ] )
    s12.start( [ c2 ] )
    s13.start( [ c2 ] )
    s14.start( [ c3 ] )
    s15.start( [ c3 ] )
    s16.start( [ c4 ] )
    s2.start( [ c4] )
    

    net.start()

    info( "*** Running CLI\n" )
    CLI(net)

    info( "*** Stopping network\n" )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()