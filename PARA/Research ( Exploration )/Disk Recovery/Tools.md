
Alright, here’s the breakdown in plain language, no fluff:

---

## **TestDisk vs PhotoRec**

They’re siblings from the same dev (Christophe Grenier), but with totally different mindsets.

### **TestDisk** – _Filesystem surgeon_ 🩺

- **When to use**:
    
    - Partition table got nuked (accidental `fdisk`/`parted`/`gparted` ops).
        
    - Filesystem is intact but _unreachable_ because the partition entry is gone or damaged.
        
    - Boot sectors or superblocks are broken but can be rebuilt.
        
    - Example: You deleted your Arch partition in GParted, but didn’t format over it.
        
- **Goal**: Restore partitions, boot sectors, and sometimes undelete files (on FAT/NTFS/ext).
    
- **Good at**: _Logical_ recovery (reconnecting existing file structures).
    
- **Bad at**: Overwritten or heavily corrupted data — it won’t “guess” file contents.
    

---

### **PhotoRec** – _Data scavenger_ 🦅

- **When to use**:
    
    - Filesystem is dead / unreadable / overwritten.
        
    - You don’t care about folders or original filenames, just want the file _contents_.
        
    - Works even if partition table is gone.
        
- **Goal**: Carve files by signature (JPEG header, MP4 magic bytes, PDF start sequence, etc.).
    
- **Good at**: Pulling raw files from chaos.
    
- **Bad at**: Preserving filenames, timestamps, or directory tree.
    

---

## **Other Forensics / Recovery Tools** (and when to use)

Here’s the “tier list” for recovery folks use:

1. **R-Studio** _(Paid, Windows/Linux/Mac)_
    
    - Very powerful for complex recoveries, RAID recon, partial overwrites.
        
    - Use when: You need advanced filesystem reconstruction and can pay.
        
2. **UFS Explorer** _(Paid, similar to R-Studio)_
    
    - Good for EXT, Btrfs, and virtual disk recoveries.
        
3. **DMDE** _(Free/Paid)_
    
    - Can do deep disk edits, recover files, rebuild structures.
        
    - Use when: You need to _manually_ piece together a filesystem.
        
4. **extundelete / ext4magic** _(Linux EXT-specific)_
    
    - Use when: You deleted files on EXT and haven’t overwritten data.
        
    - Works only if the filesystem metadata still exists.
        
5. **foremost / scalpel**
    
    - Signature-based carving like PhotoRec but allows custom configs.
        
    - Use when: You want more control over which file types to extract.
        
6. **Autopsy / Sleuth Kit**
    
    - For full-blown forensic investigation (timelines, metadata, deleted files).
        
    - Use when: You’re doing forensics, not just recovery.
        
7. **ddrescue**
    
    - Not for recovery _per se_, but to image failing disks **without killing them further**.
        
    - Use when: Drive is dying — clone it first, then recover from the image.
        

---

### **Quick Decision Flow**

- **Partition gone but data likely intact →** TestDisk first.
    
- **Drive physically dying →** ddrescue → TestDisk/PhotoRec.
    
- **Filesystem hopeless or partially overwritten →** PhotoRec/foremost/scalpel.
    
- **Deleted files on EXT with minimal changes →** extundelete/ext4magic.
    
- **Need pro-grade UI & features →** R-Studio/UFS Explorer.
    

---

If you want, I can make you a **cheat sheet table** with “Symptom → Best Tool → Why” so you can instantly know which tool to reach for. That’ll save you hours next time.