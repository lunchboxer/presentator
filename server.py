###############################################################################
##
##  Copyright (C) 2011-2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import sys

from twisted.python import log
from twisted.internet import reactor

from autobahn.twisted.websocket import listenWS

from autobahn.wamp1.protocol import WampServerFactory, WampServerProtocol


class MyPubSubServerProtocol(WampServerProtocol):
    """
    Protocol class for our simple demo WAMP server.
    """
    def onSessionOpen(self):

        ## When the WAMP session to a client has been established,
        ## register a single fixed URI as PubSub topic that our
        ## message broker will handle
        self.registerForPubSub("http://192.168.1.106/messages")


if __name__ == '__main__':

    log.startLogging(sys.stdout)

    ## our WAMP/WebSocket server
    wampFactory = WampServerFactory("ws://192.168.1.106:9000", debugWamp=True)
    wampFactory.protocol = MyPubSubServerProtocol
    listenWS(wampFactory)

    ## run the Twisted network reactor
    reactor.run()
