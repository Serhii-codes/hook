**Navigation**
### **pwd**
Show current directory.
### **cd**
- `cd ~` — go to home directory
- `cd ..` — go one level up
- `cd -` — go back to previous directory
- `cd /path/to/dir` — absolute path
- `cd ../../dir` — relative path

### **pushd /path**
Save current directory in stack and move to new one.
### **popd**
Return to last saved directory.
### **dirs**
Show directory stack.

## **Paths**
- Multiple slashes are treated as one:  
    `////usr//bin` → `/usr/bin`
## ** Directory Tree**
- `tree` — show full directory tree
- `tree -d` — directories only
- `tree /path` — starting at path
