**TCP/IP**

## **Protocol and standards**  
- A **protocol** is a set of rules defining how data should be communicated between devices over a network.
	- The "languages" that computers use to communicate.

- Since the early days of computer networking, there have been several attempts to define the functions needed for computers to communicate with each other.
	- Often developed by a specific vendor (e.g., IBM) to be used with their own products.
	- With a proprietary approach, enabling communications between different vendors' products was difficult.

Apple iMac can't sand Request to IBM server

- A **standard** is an agreed-upon specification that describes how a protocol or technology should work.
	- With vendor-neutral standards, devices of all types can communicate with each other.
		- An Apple MacBook can access a website hosted on a web server running Linux.
		- A PC running Windows can send an email that can be read on a smartphone running Android.

## **A bit of history**

- Early work on the computer networks that would evolve into today's Internet began in the 1960s.
	- The US Department of Defense's **ARPA** (Advanced Research Projects Agency) funded **ARPANET**, which came online in 1969 to connect mainframes at universities and labs.
	- Originally used a protocol called NCP (Network Control Program).

- Vint Cerf and Bob Kahn (working at DARPA) began developing TCP (Transmission Control Program) in 1974.
	- Later divided into two protocols still used today:
		- **Transmission Control Protocol (TCP)**
		- **Internet Protocol (IP)**

- These two protocols form the foundation of the protocol suite known as TCP/IP today.
	- ARPANET fully switched to TCP/IP on January 1, 1983.


- TCP/IP became dominant over vendor-proprietary solutions at the time because it was published as a set of open standards that any vendor could implement, and it could run over many different types of networks.

## **Who defines the standards?** 

- Most networking standards are developed by independent standards organizations, not by a single vendor, with participation from engineers at many companies.

- **IEEE (Institute of Electrical and Electronics Engineers)**
	- Develops many of the technologies used on local area networks:
		- **Ethernet (802.3)**
		- **Wi-Fi (802.11)**

- **IETF (Internet Engineering Task Force)**
	- Open community that defines protocols used on the Internet:
		- TCP, IP, UDP, HTTP, DNS, etc.
	- Publishes standards in documents called **RFCs** (Requests for Comments).
	  

## **Layered models**

- Networks do a lot of different jobs to move data from one computer to another.
	- Physical transmission of signals, local delivery on a LAN, routing traffic between networks, end-to-end conversations, applications, etc.

- A model lets us group related jobs into layers.
	- Each layer has a specific role.
	- Each layer uses the services of the layer below and provides services to the layer above.

- Protocols live (mostly) at one layer.
	- Examples later: IP, TCP, HTTP, etc.
	- Together they form a stack of protocols that work as a team (the network stack).

- The model is description, not low.
	- Different textbooks/courses use slightly different models (4-layer, 5-layer, etc.).



#sh7