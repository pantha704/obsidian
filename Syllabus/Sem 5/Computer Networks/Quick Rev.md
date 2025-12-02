
# Computer Networks: The Ultimate Exam Cram Sheet

## **Part 1: Essential Definitions**

### **Basic Concepts**

  * **Computer Network:** An interconnection of devices to share information in real-time. [cite_start]Benefits include reduced cost, resource sharing, and flexibility [cite: 12-15].
  * **Protocol:** A set of rules that governs data communication. [cite_start]Key elements are **Syntax** (format), **Semantics** (meaning), and **Timing** (speed/synchronization) [cite: 21-23].
  * **Bandwidth:** The maximum rate of data transfer across a given path.
  * **Throughput:** The actual rate of data successfully delivered over the network.
  * [cite_start]**Piggybacking:** A technique where an Acknowledgment (ACK) is attached to an outgoing data frame to save bandwidth, rather than sending a separate ACK packet [cite: 1546-1548].
  * [cite_start]**Bit Stuffing:** In HDLC, inserting a `0` after five consecutive `1`s in the data to prevent it from looking like a Flag (`01111110`) [cite: 937-938].

### **Transmission Modes**

  * [cite_start]**Simplex:** Unidirectional communication (e.g., Keyboard to CPU, Monitor)[cite: 32].
  * [cite_start]**Half Duplex:** Bidirectional, but only one at a time (e.g., Walkie-talkie) [cite: 34-36].
  * [cite_start]**Full Duplex:** Bidirectional and simultaneous (e.g., Telephone) [cite: 37-39].

### **Switching Techniques**

  * **Circuit Switching:** A dedicated physical path is established before data transfer (e.g., Telephone network). [cite_start]Data arrives in order [cite: 367-372].
  * **Message Switching:** "Store and Forward." No dedicated path. [cite_start]The entire message is stored at each hop (Old telegraphy) [cite: 376-377].
  * **Packet Switching:** Data is broken into small fixed-size packets. Each packet may take a different route. [cite_start]Efficient for bursty traffic [cite: 342-344].

### **Error Control**

  * **Parity Check:** Adding an extra bit (0 or 1) to make the total number of 1s even (Even Parity) or odd (Odd Parity). [cite_start]Detects single-bit errors only [cite: 1035-1038].
  * **Checksum:** Data is divided into segments, summed up, and complemented. [cite_start]The receiver checks if the sum is zero [cite: 1051-1061].
  * **CRC (Cyclic Redundancy Check):** Uses binary division with a generator polynomial. [cite_start]The remainder is appended to the data [cite: 1101-1102].
  * **Hamming Distance:** The number of bit positions in which two binary strings differ. [cite_start]Used to determine error correction capability [cite: 1184-1187].

-----

## **Part 2: Key Differences (Comparisons)**

### **1. OSI Model vs. TCP/IP Model**

[cite_start][cite: 636-640]

| Feature | OSI Model (Open Systems Interconnection) | TCP/IP Model (Transmission Control Protocol) |
| :--- | :--- | :--- |
| **Layers** | **7 Layers** (Physical, Data Link, Network, Transport, Session, Presentation, Application). | **4 Layers** (Network Access, Internet, Transport, Application). |
| **Approach** | Theoretical; Model came before protocols. | Practical; Protocols came first, model followed. |
| **Coupling** | Strict boundaries between layers. | Looser boundaries; combines OSI top 3 layers into one. |
| **Service** | Supports both connection-oriented and connectionless. | Network layer is connectionless (IP); Transport is both (TCP/UDP). |
| **Use Case** | Educational / Reference. | The actual Internet. |

### **2. LAN vs. MAN vs. WAN**

[cite_start][cite: 298]

| Feature | LAN (Local Area Network) | MAN (Metropolitan Area Network) | WAN (Wide Area Network) |
| :--- | :--- | :--- | :--- |
| **Scope** | Room, Building, Campus (km). | City-wide (approx 50km). | Country, Continent, Globe. |
| **Speed** | High (100 Mbps - 1 Gbps+). | Moderate. | Low (Kbps to Mbps). |
| **Ownership** | Private (You own the switch). | Public or Private. | Public (ISPs). |
| **Error Rate** | Lowest. | Moderate. | Highest. |
| **Example** | Home Wi-Fi, Office Ethernet. | Cable TV Network. | The Internet. |

### **3. Connection-Oriented vs. Connectionless**

[cite_start][cite: 299-303]

| Feature | Connection-Oriented (e.g., TCP, Circuit Switching) | Connectionless (e.g., UDP, Packet Switching) |
| :--- | :--- | :--- |
| **Setup** | Requires handshaking (Setup -\> Data -\> Teardown). | No setup; just send. |
| **Reliability** | High; guarantees delivery and order. | Low; no guarantees (best effort). |
| **Overhead** | High (header size, setup time). | Low. |
| **Analogy** | Phone Call. | Postal Mail / Email. |

### **4. Hub vs. Switch vs. Router**

| Device | Layer | Intelligence | Function |
| :--- | :--- | :--- | :--- |
| **Hub** | Physical (Layer 1) | Dumb | Broadcasts incoming data to **all** ports. High collision. |
| **Switch** | Data Link (Layer 2) | Smart | Reads **MAC Address**. Sends data only to the specific destination. |
| **Router** | Network (Layer 3) | Smartest | Reads **IP Address**. Connects *different* networks (e.g., LAN to WAN). |

-----

## **Part 3: Important Formulas & Numericals**

### **1. Topology Links (Mesh)**

For $n$ devices in a **Mesh** topology:

  * [cite_start]**Total Cables/Links:** $\frac{n(n-1)}{2}$ [cite: 207]
  * [cite_start]**Ports per Device:** $n-1$ [cite: 208]

### **2. Subnetting (IPv4)**

If you borrow $n$ bits for the network (subnet):

  * [cite_start]**Number of Subnets:** $2^n$ [cite: 783]
  * [cite_start]**Number of Hosts per Subnet:** $2^h - 2$ (where $h$ is remaining host bits) [cite: 795]
      * *Subtract 2 for Network ID and Broadcast ID.*

### **3. Data Rate Limits (Physical Layer)**

  * **Nyquist (Noiseless):** Max Bit Rate $= 2 \times \text{Bandwidth} \times \log_2(\text{Levels})$
  * **Shannon (Noisy):** Capacity $= \text{Bandwidth} \times \log_2(1 + \text{SNR})$
      * *Note:* If SNR is in dB, convert: $\text{SNR} = 10^{(\text{dB}/10)}$.

### **4. ALOHA Efficiency**

[cite_start][cite: 1341-1357]

  * **Pure ALOHA Max Efficiency:** $18.4\%$ ($G = 0.5$).
  * **Slotted ALOHA Max Efficiency:** $36.8\%$ ($G = 1.0$).

### **5. Window Sizes (Flow Control)**

If $N$ is the number of bits for sequence numbering:

  * **Stop-and-Wait:** Sender = 1, Receiver = 1.
  * **Go-Back-N (GBN):** Sender $= 2^N - 1$, Receiver = 1.
  * **Selective Repeat (SR):** Sender $= 2^{N-1}$, Receiver $= 2^{N-1}$.

-----

## **Part 4: Protocols & Layers Cheat Sheet**

### **Layer Functions**

1.  **Physical:** Transmits raw bits (0s and 1s) over media. [cite_start]Hubs, Cables[cite: 312].
2.  **Data Link:** Framing, Physical Addressing (MAC), Error Detection. [cite_start]Switches[cite: 315].
3.  **Network:** Logical Addressing (IP), Routing (Path selection). [cite_start]Routers [cite: 319-320].
4.  **Transport:** End-to-end delivery, Flow control (TCP/UDP), Segmentation[cite: 324].
5.  **Session:** Dialog control, Synchronization[cite: 326].
6.  **Presentation:** Encryption, Compression, Translation (Syntax)[cite: 328].
7.  **Application:** User interface, Email, File transfer (HTTP, FTP)[cite: 333].

### **Key Protocols**

  * **ARP (Address Resolution Protocol):** IP Address $\rightarrow$ MAC Address.
  * **RARP (Reverse ARP):** MAC Address $\rightarrow$ IP Address.
  * **DNS (Domain Name System):** URL (https://www.google.com/search?q=google.com) $\rightarrow$ IP Address.
  * **TCP (Transmission Control Protocol):** Reliable, Connection-oriented.
  * **UDP (User Datagram Protocol):** Unreliable, Connectionless, Fast (Streaming).
  * **DHCP:** Automatically assigns IP addresses to devices.

-----

## **Part 5: Hardware & Encoding**

### **Cabling**

  * **Twisted Pair:** UTP/STP. Cheap, flexible. Uses **RJ-45**. [cite_start]Cancels noise by twisting[cite: 72, 84].
  * **Coaxial:** Copper core, metal shield. High bandwidth but signal weakens. [cite_start]Uses **BNC**[cite: 90, 106].
  * **Fiber Optic:** Glass core, uses light (Total Internal Reflection). Fastest, secure, expensive. [cite_start]Uses **MT-RJ**[cite: 112, 135].

### **Encoding Schemes**

  * [cite_start]**NRZ-L:** Voltage level determines bit (High=0, Low=1 or vice versa)[cite: 625].
  * [cite_start]**NRZ-I:** Invert voltage on `1`, stay same on `0`[cite: 607].
  * **Manchester:** Transition in the **middle** of the bit. (Low-to-High or High-to-Low) [cite_start][cite: 593].
  * **Differential Manchester:** Transition at the **start** of the bit interval for `0`. No transition for `1`. [cite_start]Always transitions in middle [cite: 556-561].