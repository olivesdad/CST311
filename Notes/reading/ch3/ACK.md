## ack
**Acknowledgement field** 


->*The acknowledgment number that Host A puts in its segment is
the sequence number of the next byte* That it is expecting

>  TCP only acknowledges bytes up to the first missing byte in the stream, TCP is
said to provide cumulative acknowledgments.

-> what that ^ means is that the protocol can only ack segments in order. IF something arrives out of order it is up to the application to decide what to do. Some will save the out of order segment and wait until the correct sequence is recieved or discard and then the sending side would be designed to resend.

