File & Directory Operations

**Create files**
```bash
touch file.txt
touch -t 12091600 file.txt  # Set custom timestamp (YYMMDDhhmm)
```

**Create directories**
```bash
mkdir dir
mkdir /usr/newdir
```

**Delete directories**
- `rmdir dir` — only if empty
- `rm -rf dir` — delete recursively ❗ dangerous

**Move / Rename**
```bash
mv old new
mv file /path/newname
```

 **Delete files**
- `rm file`
- `rm -i file` — ask before deleting
- `rm -f file` — force delete

**Copy files**
```bash
cp source dest
```
