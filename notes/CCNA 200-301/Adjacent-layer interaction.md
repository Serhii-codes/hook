## Adjacent-layer interaction
- Each layer provides a service to the layer above it, and is serviced by the layer below it (**adjacent-layer interaction**).
	- **Layer 4** provides a service to **Layer 5** by delivering data to the correct application using port numbers.
	- **Layer 3** provides a service to **Layer 4** by delivering segments/datagrams to the correct destination host using IP addresses.
	- **Layer 2** provides a service to **Layer 3** by delivering packets to the next hop using MAC addresses.
	- **Layer 1** provides a service to **Layer 2** by sending and receiving frames as electrical, optical, or radio signals.

## Same-layer interaction 
- Each layer communicates with the same layer on other devices (**same-layer interaction**).
	- The Application layer on one host sends data to the Application layer on the other host.
	- A segment/datagram is addressed to the **Layer 4 port number** of the correct application on the destination host.
	- A packet is addressed to the **Layer 3 IP address** of the destination host.
	- A frame is addressed to the **Layer 2 MAC address** of the next hop.
	- Signals sent out of a physical port are received by a **physical port** on the connected device

## Separation of layers
- Each layer has its own job and provides a specific service to the layers above.
	- The layers are modular.
- As long as each layer keeps its "contract" with the other layers, we can improve or replace protocols at different layers without redesigning everything.
- That flexibility is one of the main benefits of a layered model.


#sh03