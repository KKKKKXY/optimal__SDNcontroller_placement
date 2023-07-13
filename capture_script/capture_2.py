#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import time

TOPOS = {'mytopo' : (lambda : multiControllerNet())}

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=RemoteController, switch=OVSKernelSwitch, waitConnected=True )

    info( "*** Creating (reference) controllers\n" )
    # for controller_num in range(16):
    #     x = x + 1
    #     # print(x)
    c1 = net.addController('c1', controller=RemoteController, ip="172.20.0.4", port=6653)
    c2 = net.addController('c2', controller=RemoteController, ip="172.20.0.5", port=6653)

    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1', protocols="OpenFlow13" )
    s2 = net.addSwitch( 's2', protocols="OpenFlow13" )

    info( "*** Creating hosts\n" )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )

    info( "*** Creating links\n" )
    s1.linkTo( h1 )
    s2.linkTo( h2 )
    s1.linkTo( s2 )

    info( "*** Starting network\n" )
    net.build()
    c1.start()
    c2.start()
    s1.start( [ c1 ] )
    s2.start( [ c2 ] )

    net.start()

    time.sleep(4)

    for x in range(1, 11):
        result = open("/home/mya/capture_script/capture_result_2.txt","a")
        info("====================================Starting " + str(x) + " FOR LOOP====================\n")
        result.write("\n")
        result.write("\n")
        info("*** h1 FLUSH\n")
        time.sleep(2)
        h1.cmd("ip -s -s neigh flush all >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)

        info( "*** h2 FLUSH\n" )
        time.sleep(2)
        h2.cmd("ip -s -s neigh flush all >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)

        info( "*** s1 FLUSH\n" )
        time.sleep(2)
        s1.cmd("ip -s -s neigh flush all >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)

        info( "*** s2 FLUSH\n" )
        time.sleep(2)
        s2.cmd("ip -s -s neigh flush all >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)

        info( "*** s1 DELETE FLOW\n" )
        time.sleep(2)
        s1.dpctl("del-flows -O OpenFlow13 >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)
        s1.dpctl("dump-flows -O OpenFlow13 >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)
        # s1.cmd("sh ovs-ofctl -O OpenFlow13 del-flows s1")
        # s1.cmd("sh ovs-ofctl -O OpenFlow13 dump-flows s1 >> /home/mya/capture_script/capture_result_2.txt")

        info( "*** s2 DELETE FLOW\n" )
        time.sleep(2)
        s2.dpctl("del-flows -O OpenFlow13 >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)
        s2.dpctl("dump-flows -O OpenFlow13 >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)

        info( "*** Starting PING\n" )
        time.sleep(2)
        h1.cmd("ping 10.0.0.2 -c 4 >> /home/mya/capture_script/capture_result_2.txt")
        time.sleep(2)

        info("====================================Finished " + str(x) + " FOR LOOP====================\n")
        info("\n")
        result.write("====================================Finished " + str(x) + " FOR LOOP====================\n")
        result.write("\n")
        result.write("\n")

        time.sleep(5)

    info( "*** Running CLI\n" )
    CLI(net)

    info( "*** Stopping network\n" )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()