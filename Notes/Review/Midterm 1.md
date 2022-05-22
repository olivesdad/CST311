# Review Questions:
1. **Bandwidth flooding vs Connection flooding?**
	- Bandwidth flooding is an attack on the network access links for the targeted host; while connection flooding is an attack on a server by overwhelming it with so many bogus TCP connections, the server stops accepting real connections.
2. **BitTorent would likely not exist if not for the trading "tit for tat" design**
	- True
3. **TCP Tahoe with *MSS = 12* and *sshthresh = 8* experiences 3 consecutive duplicate ACKS what is the new window?**
	- cwnd = 1 ssthresh = 6
4.  **TCP invented by Vinton Cerf and Robert Kahn?**
	- True
5.  **Match protocol stack:**
	1. Application layer -> message
	2. Transport layer -> Segment
	3. Network layer -> Datagram
	4. Link Layer -> Frame 
6. **Network layer guarantees delivery of a segment but does not guarantee orderly delivery**
	- false
7. ![[Pasted image 20220519210956.png]]
	- when it gets into the route *2*
8.  **x ->5Mbs-> Y  sending 250KB. What is the tranmission time?**
	- check [[Bits and Shits]]
	- $(1024*250*8)/(5*1,000,000)=0.4096$
9. **Traffic intensity**  
	- $La/R$:  L=packet size, a=packets/sec, R=transmission rate of router
10. **When traffic Intensity is greater than 1**
	- queuing delay can be significiant
15. **Generally what port numbers can we use as programmers?**
	- Anything over 1023 and that has not been registered by IANA
16. **WIreshark how many answers in DNS packet?**
	- I just saw 2 blocks so i picked 2
17. **Where do queuing delays occur?**
	- At the router before before the out link (before transmission)
>[!Note on Delay]
>processing -> queuing ->transmission ->propagation 
18. **Wireshark what is the local DNS ip?**
	- I picked the destination **Dst:** field 
19. **Transmission delay**
	- On the outbound router section (when its putting packet onto the link)
20. **Propagation Delay**
	- Path between routers 
21. **End to End delay**
	- I just summed everything up $Processing + queuing + transmission + propagation = 21$
23. **Throughput**
	- The bottleneck but be careful the question asks *"each client"* so it's the bottlneck divided by the clients using it
26.  **A -TCP-> B  fileSize=200k Bytes [[MSS]] = 500Bytes. If the first segment is numnbered 0 what is put in the sequence number field in the header of the 3rd segment?**
		- see [[sequence number field]] ->1000
27.  ***950KB (A) --10Mbs-> C* what is the transfer time?**
		- [[Bits and Shits]]
		- $(950*1024*8)/10,000,000=0.778$
29. **DNS question gives rtt for the DNS query and then RTT to the server and asks for total** 
>[!TCP tricky]
>For TCP transfers we need to account for 1 $RTT_{handshake}$ per transfer
-   $RTT_{dns}(4) + RTT_{http}(54) + RTT_{handshake}(54) = 112$ <- Needs handshake
	- Suppose we need to pull 5 objects from the server and are allowed 5 parallel TCP connections
		- We have the origignal 58ms of question 1 then we can pull the 5 additional objects referenced in parallel *Plus Handshakes*  so we have $RTT_{dns}(4)+RTT_{http}(54)+RTT_{5obj}(54)+2*RTT_{handshake}(54) = 220ms$
	- now the supposition is that we have 5 objects that must be pulled without parallel connetions so the equation is now: $RTT_{dns}(4)+RTT_{http}(54)+5*RTT_{5obj}(54) + 6 * RTT_{handshake}(54)=652$
	- Now same thing parallel connections with peristent HTTP the equation becomes: $RTT_{dns}(4)+RTT_{http}(54)+RTT_{5obj}(54)+2*RTT_{handshake}(54)=166$ <- This seems to imply we can open 5 parallel connections at the begnning or that the first one doesnt need a handshake??
34. **Distribute file F = 9Gbits to each of 6 peers (p2p)**
	- $DP2P≥max\{F/u_s,F/d_{min},NF/(u_s + ∑u_i)\}$
		- This was File size / the slowest download rate = 818.18. And the next question asked which of the 3 values were the basis 
36. **Distribute file Client server**
	- $D_{c-s}≥max\{NF/u_s,F/d_{min}\}$
	- 