#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import time
from datetime import datetime
from mininet.link import TCLink

# net = Mininet(topo=topo, link=TCLink)

TOPOS = {'mytopo' : (lambda : multiControllerNet())}

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=RemoteController, switch=OVSKernelSwitch, waitConnected=True, link=TCLink )

    info( "*** Creating (reference) controllers\n" )
    c1 = net.addController('c1', controller=RemoteController, ip="172.20.0.5", port=6653)
    c2 = net.addController('c2', controller=RemoteController, ip="172.20.0.6", port=6653)

    # add nodes, switches first...
    NY54 = net.addSwitch( 's25', protocols='OpenFlow13' ) # 40.728270, -73.994483
    CMBR = net.addSwitch( 's1', protocols='OpenFlow13' )  # 42.373730, -71.109734
    # CHCG = net.addSwitch( 's2', protocols='OpenFlow13' )  # 41.877461, -87.642892
    # CLEV = net.addSwitch( 's3', protocols='OpenFlow13' )  # 41.498928, -81.695217
    # RLGH = net.addSwitch( 's4', protocols='OpenFlow13' )  # 35.780150, -78.644026
    # ATLN = net.addSwitch( 's5', protocols='OpenFlow13' )  # 33.749017, -84.394168
    # PHLA = net.addSwitch( 's6', protocols='OpenFlow13' )  # 39.952906, -75.172278
    # WASH = net.addSwitch( 's7', protocols='OpenFlow13' )  # 38.906696, -77.035509
    # NSVL = net.addSwitch( 's8', protocols='OpenFlow13' )  # 36.166410, -86.787305
    # STLS = net.addSwitch( 's9', protocols='OpenFlow13' )  # 38.626418, -90.198143
    # NWOR = net.addSwitch( 's10', protocols='OpenFlow13' ) # 29.951475, -90.078434
    # HSTN = net.addSwitch( 's11', protocols='OpenFlow13' ) # 29.763249, -95.368332
    # SNAN = net.addSwitch( 's12', protocols='OpenFlow13' ) # 29.424331, -98.491745
    # DLLS = net.addSwitch( 's13', protocols='OpenFlow13' ) # 32.777665, -96.802064
    # ORLD = net.addSwitch( 's14', protocols='OpenFlow13' ) # 28.538641, -81.381110
    # DNVR = net.addSwitch( 's15', protocols='OpenFlow13' ) # 39.736623, -104.984887
    # KSCY = net.addSwitch( 's16', protocols='OpenFlow13' ) # 39.100725, -94.581228
    # SNFN = net.addSwitch( 's17', protocols='OpenFlow13' ) # 37.779751, -122.409791
    # SCRM = net.addSwitch( 's18', protocols='OpenFlow13' ) # 38.581001, -121.497844
    # PTLD = net.addSwitch( 's19', protocols='OpenFlow13' ) # 45.523317, -122.677768
    # STTL = net.addSwitch( 's20', protocols='OpenFlow13' ) # 47.607326, -122.331786
    # SLKC = net.addSwitch( 's21', protocols='OpenFlow13' ) # 40.759577, -111.895079
    # LA03 = net.addSwitch( 's22', protocols='OpenFlow13' ) # 34.056346, -118.235951
    # SNDG = net.addSwitch( 's23', protocols='OpenFlow13' ) # 32.714564, -117.153528
    # PHNX = net.addSwitch( 's24', protocols='OpenFlow13' ) # 33.448289, -112.076299

    # ... and now hosts
    NY54_host = net.addHost( 'h25' )
    CMBR_host = net.addHost( 'h1' )
    # CHCG_host = net.addHost( 'h2' )
    # CLEV_host = net.addHost( 'h3' )
    # RLGH_host = net.addHost( 'h4' )
    # ATLN_host = net.addHost( 'h5' )
    # PHLA_host = net.addHost( 'h6' )
    # WASH_host = net.addHost( 'h7' )
    # NSVL_host = net.addHost( 'h8' )
    # STLS_host = net.addHost( 'h9' )
    # NWOR_host = net.addHost( 'h10' )
    # HSTN_host = net.addHost( 'h11' )
    # SNAN_host = net.addHost( 'h12' )
    # DLLS_host = net.addHost( 'h13' )
    # ORLD_host = net.addHost( 'h14' )
    # DNVR_host = net.addHost( 'h15' )
    # KSCY_host = net.addHost( 'h16' )
    # SNFN_host = net.addHost( 'h17' )
    # SCRM_host = net.addHost( 'h18' )
    # PTLD_host = net.addHost( 'h19' )
    # STTL_host = net.addHost( 'h20' )
    # SLKC_host = net.addHost( 'h21' )
    # LA03_host = net.addHost( 'h22' )
    # SNDG_host = net.addHost( 'h23' )
    # PHNX_host = net.addHost( 'h24' )

    # add edges between switch and corresponding host
    net.addLink( NY54 , NY54_host )
    net.addLink( CMBR , CMBR_host )
    # net.addLink( CHCG , CHCG_host )
    # net.addLink( CLEV , CLEV_host )
    # net.addLink( RLGH , RLGH_host )
    # net.addLink( ATLN , ATLN_host )
    # net.addLink( PHLA , PHLA_host )
    # net.addLink( WASH , WASH_host )
    # net.addLink( NSVL , NSVL_host )
    # net.addLink( STLS , STLS_host )
    # net.addLink( NWOR , NWOR_host )
    # net.addLink( HSTN , HSTN_host )
    # net.addLink( SNAN , SNAN_host )
    # net.addLink( DLLS , DLLS_host )
    # net.addLink( ORLD , ORLD_host )
    # net.addLink( DNVR , DNVR_host )
    # net.addLink( KSCY , KSCY_host )
    # net.addLink( SNFN , SNFN_host )
    # net.addLink( SCRM , SCRM_host )
    # net.addLink( PTLD , PTLD_host )
    # net.addLink( STTL , STTL_host )
    # net.addLink( SLKC , SLKC_host )
    # net.addLink( LA03 , LA03_host )
    # net.addLink( SNDG , SNDG_host )
    # net.addLink( PHNX , PHNX_host )

    # add edges between switches
    net.addLink( NY54 , CMBR, bw=10, delay='0.979030824185ms')
    net.addLink( NY54 , CMBR, bw=10, delay='0.979030824185ms')
    # net.addLink( NY54 , CMBR, bw=10, delay='0.979030824185ms')
    # net.addLink( NY54 , CHCG, bw=10, delay='0.806374975652ms')
    # net.addLink( NY54 , PHLA, bw=10, delay='0.686192970166ms')
    # net.addLink( NY54 , PHLA, bw=10, delay='0.686192970166ms')
    # net.addLink( NY54 , WASH, bw=10, delay='0.605826192092ms')
    # net.addLink( CMBR , PHLA, bw=10, delay='1.4018238197ms')
    # net.addLink( CHCG , CLEV, bw=10, delay='0.232315346482ms')
    # net.addLink( CHCG , PHLA, bw=10, delay='1.07297714274ms')
    # net.addLink( CHCG , STLS, bw=10, delay='1.12827896944ms')
    # net.addLink( CHCG , DNVR, bw=10, delay='1.35964770335ms')
    # net.addLink( CHCG , KSCY, bw=10, delay='1.5199778541ms')
    # net.addLink( CHCG , KSCY, bw=10, delay='1.5199778541ms')
    # net.addLink( CHCG , SNFN, bw=10, delay='0.620743405435ms')
    # net.addLink( CHCG , STTL, bw=10, delay='0.93027212534ms')
    # net.addLink( CHCG , SLKC, bw=10, delay='0.735621751348ms')
    # net.addLink( CLEV , NSVL, bw=10, delay='0.523419372248ms')
    # net.addLink( CLEV , STLS, bw=10, delay='1.00360290845ms')
    # net.addLink( CLEV , PHLA, bw=10, delay='0.882912133249ms')
    # net.addLink( RLGH , ATLN, bw=10, delay='1.1644489729ms')
    # net.addLink( RLGH , WASH, bw=10, delay='1.48176810502ms')
    # net.addLink( ATLN , WASH, bw=10, delay='0.557636936322ms')
    # net.addLink( ATLN , NSVL, bw=10, delay='1.32869749865ms')
    # net.addLink( ATLN , STLS, bw=10, delay='0.767705554748ms')
    # net.addLink( ATLN , DLLS, bw=10, delay='0.544782086448ms')
    # net.addLink( ATLN , DLLS, bw=10, delay='0.544782086448ms')
    # net.addLink( ATLN , DLLS, bw=10, delay='0.544782086448ms')
    # net.addLink( ATLN , ORLD, bw=10, delay='1.46119152532ms')
    # net.addLink( PHLA , WASH, bw=10, delay='0.372209320106ms')
    # net.addLink( NSVL , STLS, bw=10, delay='1.43250491305ms')
    # net.addLink( NSVL , DLLS, bw=10, delay='1.67698215288ms')
    # net.addLink( STLS , DLLS, bw=10, delay='0.256389964194ms')
    # net.addLink( STLS , KSCY, bw=10, delay='0.395511571791ms')
    # net.addLink( STLS , LA03, bw=10, delay='0.257085227363ms')
    # net.addLink( NWOR , HSTN, bw=10, delay='0.0952906633914ms')
    # net.addLink( NWOR , DLLS, bw=10, delay='1.60231329739ms')
    # net.addLink( NWOR , ORLD, bw=10, delay='0.692731063896ms')
    # net.addLink( HSTN , SNAN, bw=10, delay='0.284150653798ms')
    # net.addLink( HSTN , DLLS, bw=10, delay='1.65690128332ms')
    # net.addLink( HSTN , ORLD, bw=10, delay='0.731886304782ms')
    # net.addLink( SNAN , PHNX, bw=10, delay='1.34258627257ms')
    # net.addLink( SNAN , DLLS, bw=10, delay='1.50063532341ms')
    # net.addLink( DLLS , DNVR, bw=10, delay='0.251471593235ms')
    # net.addLink( DLLS , DNVR, bw=10, delay='0.251471593235ms')
    # net.addLink( DLLS , KSCY, bw=10, delay='0.18026026737ms')
    # net.addLink( DLLS , KSCY, bw=10, delay='0.18026026737ms')
    # net.addLink( DLLS , SNFN, bw=10, delay='0.74304274592ms')
    # net.addLink( DLLS , LA03, bw=10, delay='0.506439293357ms')
    # net.addLink( DLLS , LA03, bw=10, delay='0.506439293357ms')
    # net.addLink( DNVR , KSCY, bw=10, delay='0.223328790403ms')
    # net.addLink( DNVR , SNFN, bw=10, delay='0.889017541903ms')
    # net.addLink( DNVR , SNFN, bw=10, delay='0.889017541903ms')
    # net.addLink( DNVR , SLKC, bw=10, delay='0.631898982721ms')
    # net.addLink( KSCY , SNFN, bw=10, delay='0.922778522233ms')
    # net.addLink( SNFN , SCRM, bw=10, delay='0.630352278097ms')
    # net.addLink( SNFN , PTLD, bw=10, delay='0.828572513655ms')
    # net.addLink( SNFN , STTL, bw=10, delay='1.54076081649ms')
    # net.addLink( SNFN , SLKC, bw=10, delay='0.621507502625ms')
    # net.addLink( SNFN , LA03, bw=10, delay='0.602936230151ms')
    # net.addLink( SNFN , LA03, bw=10, delay='0.602936230151ms')
    # net.addLink( SNFN , LA03, bw=10, delay='0.602936230151ms')
    # net.addLink( SCRM , SLKC, bw=10, delay='0.461350343644ms')
    # net.addLink( PTLD , STTL, bw=10, delay='1.17591515181ms')
    # net.addLink( SLKC , LA03, bw=10, delay='0.243225267023ms')
    # net.addLink( LA03 , SNDG, bw=10, delay='0.681264950821ms')
    # net.addLink( LA03 , SNDG, bw=10, delay='0.681264950821ms')
    # net.addLink( LA03 , PHNX, bw=10, delay='0.343709457969ms')
    # net.addLink( LA03 , PHNX, bw=10, delay='0.343709457969ms')
    # net.addLink( SNDG , PHNX, bw=10, delay='0.345064487693ms')
    net.addLink( c1 , c2, bw=10, delay='0.345064487693ms')

    info( "*** Starting network\n" )
    net.build()
    c1.start()
    c2.start()

    net.start()

    info( "*** Running CLI\n" )
    CLI(net)

    info( "*** Stopping network\n" )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()