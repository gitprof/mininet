"""Custom topology example


                   s5
                 /    \
        h1 ---- s3     s4 --- host
                 \    /
                   s6

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class TestTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1', ip='0.0.0.0' )
        rightHost = self.addHost( 'h2', ip='0.0.0.0' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )
        northSwitch = self.addSwitch( 's5' )
        southSwitch = self.addSwitch( 's6' )

        # Add links
        self.addLink( leftHost,    leftSwitch )
        self.addLink( rightSwitch, rightHost )
        self.addLink( leftSwitch,  northSwitch )
        self.addLink( rightSwitch, northSwitch )
        self.addLink( rightSwitch, southSwitch )
        self.addLink( leftSwitch,  southSwitch )


topos = { 'testtopo': ( lambda: TestTopo() ) }
