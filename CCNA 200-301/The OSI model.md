- TCP/IP development started in the 1970s (ARPANET work, early TCP/IP specs).

- In the late 1970s and 1980s, the **International Organization for Standardization (ISO)** designed a 7-layer **Open Systems Interconnection (OSI) model** and a matching protocol suite.
	- The goal was to create international, vendor-neutral networking standards that could unify existing proprietary stacks and potentially replace TCP/IP.

- Governments, including the US, promoted OSI as the preferred/recommended stack for new deployments.

- OSI protocols ended up being late and complex, and never gained the same deployment as TCP/IP.
	- TCP/IP "won" in the real world, although some OSI technologies are still used.

- Today, almost all real networks use TCP/IP, but the 7-layer OSI model survives as a reference/teaching model and a common way to talk about "layers".

- Most networking resources use a 5-layer model like the one covered in this video, but with names from the OSI model.
	- That is why the TCP/IP Application layer is often called **Layer 7**

**Adapted 5-layer model**

| 7Application    |
| --------------- |
| 4 Transport     |
| 3 **Network**   |
| 2 **Data link** |
| 1 Physical      |
   |     |
| --- |
|     |
|     |
|     |
|     |
| 7Application    |
| --------------- |
| 4 Transport     |
| 3 **Network**   |
| 2 **Data link** |
| 1 Physical      |
**OSI nodel**

| 7Application    |
| --------------- |
| 6 Presentation  |
| 5 Session       |
| 4 Transport     |
| 3 Network       |
| 2 Data link<br> |
| 1 Physical      |

#sh7