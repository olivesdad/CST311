# nmap

- port scanning tool
>  Network exploration tool and security / port scanner.
  Some features only activate when Nmap is run with privileges.
  More information: https://nmap.org.
- nmap sends TCP SYN segments to destination ports with 3 possible outcomes 
1.  Recieve [[SYN 1]]ACK segment -> port is open
2. recieve [[RST]] meaning there is no TCP listener on this port
3. no response -> probably blocked by firewall or something