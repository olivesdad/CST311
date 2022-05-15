
# Chapter 3 Reading

## 3.5; TCP
- [[MSS]]  maximum segment
- [[MTU]] maximum transmission unit
- [[sequence number field]]
- [[ACK]]
- [[SYN]]
- [[NAK]]
- [[FIN]]
- [[Go-Back-N (GBN)]]
-  [[Selective Repeat (SR)]]

## RTT Estimation and TImeout

- **Sample RTT** Sample RTT is the measurement of time between when a segment is sent and when the [[ACK]] is recieved
- **EstimatedRTT** is updated after each sample. given by the formula:
   *EstimatedRTT=(1−α)⋅EstimatedRTT+α⋅SampleRTT*  
   Each sample is added to the esimtated with a weighted value so that this number reflects changes in the network. Older value will decay
   recommended value of some alpha is 0.125 which is the weighted value which causes the decay
- **DevRTT** is the variablility of RTT estimatedby the formula:
  *DevRTT=(1−β)⋅DevRTT+β⋅|SampleRTT−EstimatedRTT|*  This measurement is the amount that the sample RTT is deviating from the estimated it is [[EWMW]]
  - Timeout is usually set to EstimatedRTT + some margin *TimeoutInterval=EstimatedRTT+4⋅DevRTT*
## Errororor
If an ack for a lower segment gets lost but we get a higher ack we can not re-transmit this is because, say we sen packets ending in 100 and 200, and the ack for 100 is lost but we get an ACK for 200. WE know tht 100 was recieved because the reciever will not stop transmitting the ack for the lowest recieved packet
$$ example $$
- Server sends packet 100, , 200, 300
- Client gets packet 100, and 300
- Client will ack 100 when it gets 100 but then when it recieves 300 it will send ack for 100 again
