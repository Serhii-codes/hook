Search Tools
### **locate**
- Uses prebuilt database → fast
- Update database:
```nginx
sudo updatedb
```
Example:
```perl
locate zip | grep app
```
### **grep**

Filter lines by pattern.
### **find**
Search by name, type, size, time.
Examples:
```arduino
find /usr -name gcc
find /usr -type d -name gcc
find . -name "*.log"
find / -size +10M
find / -mtime -3
```

**Execute commands on found files**
```bash
find . -name "*.swp" -exec rm {} ';'
find . -name "*.swp" -ok rm {} ';'   # ask before each
```
## **Wildcards**
- `?` — any single character
- `*` — any sequence
- `[abc]` — one of the set
- `[!abc]` — anything except set
Examples:
```bash
ls ba?.out
ls *.out
```
