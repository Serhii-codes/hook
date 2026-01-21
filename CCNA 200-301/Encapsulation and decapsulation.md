5 **Application**
4 **Transport**
3 **Internet**
2 **Local network**
1 **Physical**
## Encapsulation
- The **Application layer** prepares the data to be sent over the network.
- As the message moves down the stack, each layer **encapsulates** the data with a **header** including the information needed for that layer.
	- Source and destination addresses (port numbers, IP addresses, MAC addresses), etc.
	- Layer 2 also adds a **trailer** that the receiving device uses to check for transmission errors.

- The **Physical layer** transmits the bits as signals over the physical medium.
	- The **L2 header** is transmitted first, and the **L2 trailer** is transmitted last

## Decapsulation
5 **Application**
4 **Transport**
3 **Internet**
2 **Local network**
1 **Physical**

- The receiving device receives the message as a stream of bits at Layer 1.
- The device examines the information in the Layer 2 header and trailer, and then removes them (**decapsulation**).
	- The decapsulation process continues up the stack: Layer 3 removes the L3 header, then Layer 4 removes the L4 header, and then the data is delivered to the Application layer.
- The application processes the data and, if needed, generates a response that goes back down the stack.


#sh01