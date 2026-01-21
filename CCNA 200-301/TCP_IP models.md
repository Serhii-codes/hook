## **TCP/IP** models

**Application layer** 
- Protocols for communication between application processes; create and interpret the data.

**Transport layer** 
- Provides end-to-end communication between application processes using port numbers.

**Internet layer**
- Provides end-to-end communication between hosts across networks using IP addresses and routers.

**Local network layer** 
- Provides hop-to-hop delivery within a local network using MAC addresses and switches.

**Physical layer**
- Sends bits as electrical, optical, or radio signals over the physical medium.

##  **layer 1: Physical layer**
- The **Physical Layer** (Layer 1) sends and receives bits as electrical, optical, or radio signals over the medium.
- Defines things like cables, connectors, signal levels, and link speeds.
- Examples: copper UTP cables, fiber-optic cables, Wi-Fi radios and antennas, network interface cards (NICs).
- The physical layer aspect of transmitting data are very complex
	- Network engineers typically don't n have to know the low-level details.  

##   **layer 2: Local network layer** 
- The **Local Network layer (Layer 2)** provides **hop-to-hop** delivery of messages on a local network.
	- A **hop** is one step along the path between two devices:
		- from one router or host, to the next router or host in the path.
	- Switches don't count: a switch just extends the local network, allowing multiple devices to connect.

- Uses **MAC (Media Access Control)** addresses to identify interfaces.
	- **PC1** sends the message to the MAC address of **R1's G1 interface (NIC)**.
	- **R1** sends the message to the MAC address of **R2's G1 interface (NIC)**.
	- **R2** sends the message to the MAC address of **SRV1's interface (NIC)**.

- Protocols at this layer include:
	- Ethernet (IEEE 802.3)
	- Wi-Fi (IEEE 802.11)

## **layer 3: Internet layer**
- The **Internet layer** (Layer 3) provides end-to-end delivery between hosts across multiple networks.
	- Internet = internetwork (between networks)

- Uses **IP addresses** to identify hosts in the network.
	- When PC1 sends a message to SRV1, it addresses the message to SRV1's IP address.

- **Routers** operate mainly at this layer, using the message's destination IP address to forward the message toward its final destination host.

- Protocols at this layer include:
	- IP (IPv4, IPv6)
	- ICMP (Internet Control Message Protocol)

## **layer 4: Transport layer** 
 - The **Transport layer** (Layer 4) provides end-to-end communication between application processes.
	- Also called "process-to-process" or "service-to-service".

- Uses **port numbers** to identify the processes on each host.
	- When the web client on PC1 wants to send a request to the web server running on SRV1, it addresses the message to port 80.

- Runs mainly on the communicating hosts (PC1 and SRV1); routers normally operate based on IP (Layer 3), not on Transport-layer information.

- Protocols at this layer include:
	- UDP (User Datagram Protocol): simple and efficient
	- TCP (Transmission Control Protocol): more robust features beyond basic message addressing
	  
## **layer 5(7): Application layer** 
- The **Application layer** (Layer 5) is where network communications meet applications.
	- Usually called **Layer 7** (more info on that later...)

- Defines how application processes format, send, and interpret data.

- Protocols at this layer define message formats and rules for specific tasks, such as:
	- Browsing web pages (HTTP/HTTPS)
	- Transferring files (FTP, TFTP)
	- Sending/receiving email (SMTP, POP3, IMAP)

- Network infrastructure devices (routers, switches) don't care about Application-layer details.
	- They just move messages across the network.
	- Only the communicating hosts interpret the data.





#sh14