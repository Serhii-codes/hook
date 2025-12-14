Links (Hard & Soft)

**Hard link**
```bash
ln file1 file2
```
- Same inode
- Both behave as the same file

**Soft (symbolic) link**
```bash
ln -s target link_name
```
- Points to original
- Different inode