# SYN 
	TCP SYN Segment

- This is a special segment in the initial connection
- contains no application layer data
- In this segment the the client randomly chooses an initial sequence number to start the transmission 
- Basically we send this when we want to establish connection with listener
- SYN is also one bit in the header that denotes this is happening. The server will also send a populated SYN bit back along with it's random first sequence number
- This single bit will be set to 0 for the remainder of the connection

>The connection-granted segment is referred to as a SYNACK segment.