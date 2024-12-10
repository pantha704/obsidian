


Here's a concise cheatsheet for using Bettercap, a powerful tool for network attacks and monitoring:

### Bettercap Cheatsheet

#### Installation
- **Install via Homebrew (macOS)**:
  ```bash
  brew install bettercap
  ```
- **Install via APT (Linux)**:
  ```bash
  sudo apt-get install bettercap
  ```
- **Install via Go**:
  ```bash
  go get github.com/bettercap/bettercap
  ```

#### Basic Commands
- **Start Bettercap**:
  ```bash
  sudo bettercap -iface eth0
  ```
- **Interactive Mode**:
  ```bash
  sudo bettercap -iface eth0 -eval "caplets.update; ui.update; ui"
  ```

#### Modules and Commands
- **Help**: List all available commands.
  ```bash
  help
  ```
- **Show Modules**: Display all available modules.
  ```bash
  modules
  ```
- **Use Module**: Activate a specific module.
  ```bash
  net.probe on
  ```
- **Show Module Options**: Display options for a module.
  ```bash
  net.show
  ```

#### Network Reconnaissance
- **Network Discovery**:
  ```bash
  net.probe on
  ```
- **Show Devices**:
  ```bash
  net.show
  ```

#### Man-in-the-Middle (MITM) Attacks
- **ARP Spoofing**:
  ```bash
  arp.spoof on
  ```
- **DNS Spoofing**:
  ```bash
  dns.spoof on
  ```

#### HTTPS and SSL
- **HTTPS Downgrade**:
  ```bash
  https.proxy on
  ```
- **SSL Stripping**:
  ```bash
  sslstrip on
  ```

#### Sniffing and Logging
- **Packet Sniffing**:
  ```bash
  net.sniff on
  ```
- **Log to File**:
  ```bash
  set net.sniff.output /path/to/logfile.pcap
  ```

#### Custom Scripts and Caplets
- **Load Caplet**:
  ```bash
  caplets.show
  caplets.load <caplet_name>
  ```
- **Create Custom Caplet**:
  - Write custom commands in a `.cap` file and load it using `caplets.load`.

#### Exiting Bettercap
- **Exit**:
  ```bash
  exit
  ```

### Ethical Considerations
- Use Bettercap responsibly and legally.
- Ensure you have permission to test and monitor networks.

### Resources
- **[Bettercap Documentation](https://www.bettercap.org/docs/)**: Official documentation for detailed usage.
- **[GitHub Repository](https://github.com/bettercap/bettercap)**: Source code and additional resources.

This cheatsheet provides a quick reference to the most common Bettercap commands and techniques. Always ensure your activities comply with legal and ethical standards.
