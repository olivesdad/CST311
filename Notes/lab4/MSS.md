### Maximum Segment Size
-  The MSS is typically set by first
determining the length of the largest link-layer frame that can be sent by the local sending host (the so-
called maximum transmission unit, MTU), and then setting the MSS to ensure that a TCP segment
(when encapsulated in an IP datagram) plus the TCP/IP header length (typically 40 bytes) will fit into a
single link-layer frame