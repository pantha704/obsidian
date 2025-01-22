
### **TL;DR of SSH**  
SSH (Secure Shell) is a cryptographic protocol that:  
🔐 **Encrypts** all data (logins, commands, files) between devices  
🔑 Uses **key-based authentication** (more secure than passwords)  
🌐 Works over insecure networks (public Wi-Fi, internet)  
🚀 Enables secure remote access (servers, IoT devices, Git, etc.)  

---

### **Key Benefits for You**  
1. **No More Passwords**  
   - SSH keys replace password prompts (ideal for Obsidian-Git automation).  
2. **Git Security**  
   - Encrypts all Git operations (`push`, `pull`, `clone`).  
3. **Tamper-Proof**  
   - Prevents "man-in-the-middle" attacks when using public networks.  
4. **Port Forwarding**  
   - Securely access services behind firewalls (e.g., localhost dev servers).  

---

### **Common Uses**  
- **Git Operations** (GitHub/GitLab/Bitbucket)  
- **Remote Server Access** (AWS, DigitalOcean, Raspberry Pi)  
- **Secure File Transfers** (`scp`, `sftp`)  
- **Tunneling** (access databases, web servers securely)  

---

### **Why SSH > HTTPS for Git**  
| **SSH**                     | **HTTPS**                     |  
|------------------------------|-------------------------------|  
| No password prompts          | Requires PAT (Personal Access Token) |  
| Key-based auth               | Token/cookie-based auth       |  
| Works behind strict firewalls| Blocked by some corporate proxies |  

---

### **SSH Key Anatomy**  
- **Private Key** (`id_ed25519`): Stays **only** on your machine.  
- **Public Key** (`id_ed25519.pub`): Added to services (GitHub, servers).  

*Pro Tip:* Use `ed25519` keys (modern, secure, shorter than RSA).  

Bookmark this as your **SSH cheat sheet**! 🔐