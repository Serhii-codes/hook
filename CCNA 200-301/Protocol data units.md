- At each stage in the encapsulation/decapsulation process, there is a name given to the message:
	- The combination of data and a L4 header is called a **segment** (TCP) or **datagram** (UDP).
		- TCP creates segments, UDP creates datagrams.
	- The combination of a **segment/datagram** and a L3 header is called a packet.
	- The combination of a packet and a L2 header/trailer is called a frame.
	- This is what is actually sent over the wire.

- We can use alternative names to describe the message at each stage: **protocol data unit (PDU)**
	- A segment or datagram is a **Layer 4 PDU (L4PDU)**.
	- A packet is a **Layer 3 PDU (L3PDU)**.
	- A frame is a **Layer 2 PDU (L2PDU)**.

- The contents of each PDU (everything encapsulated by that layer's header/trailer) are called the **payload**.
	- A **segment** or **datagram's** payload is the **application data**.
	- A **packet's** payload is a **segment** or **datagram**.
	- A **frame's** payload is a **packet**.


#sh7