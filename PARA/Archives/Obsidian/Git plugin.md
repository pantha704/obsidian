
Here's a concise **SSH + Obsidian-Git Integration Cheatsheet** to save for future reference:

---

### **1. Generate SSH Key**
```bash
ssh-keygen -t ed25519 -C "your@email.com"
# Press Enter 3x (no passphrase for Obsidian-Git compatibility)
```

### **2. Add Key to GitHub**
```bash
cat ~/.ssh/id_ed25519.pub
```
- Copy output → [GitHub SSH Keys](https://github.com/settings/keys) → **New SSH Key**

### **3. Configure Git Remote**
```bash
git remote set-url origin git@github.com:username/repo.git
```

### **4. SSH Config (For Restricted Networks)**
```bash
nano ~/.ssh/config
```
Add:
```config
Host github.com
  Hostname ssh.github.com
  User git
  Port 443
  IdentityFile ~/.ssh/id_ed25519
```

---

### **Verify Setup**
```bash
ssh -T git@github.com  # Should greet you!
git remote -v          # Should show SSH URLs
```

---

### **Key Points**
- **No Passphrase**: Required for Obsidian-Git auto-push
- **Force Push After Reset**:
  ```bash
  git push --force origin main
  ```
- **Ignore Plugin Files**:
  Add to `.gitignore`:
  ```gitignore
  .obsidian/workspace*
  .obsidian/plugins/**/main.js
  ```

---

Bookmark this as your **Obsidian-Git SSH Master Guide**! 🔐  
*Next time, just `git clone git@github.com:...` and you’re set!* 😊