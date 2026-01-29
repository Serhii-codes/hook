**Standard Streams**
- **stdin** — keyboard / input file
- **stdout** — terminal
- **stderr** — error output

**Redirection**
```python
cmd < input.txt         # use file as input
cmd > output.txt        # write output to file
cmd 2> errors.txt       # write errors only
cmd > all.txt 2>&1      # merge stdout + stderr
cmd >& all.txt          # shorthand
```

**Pipes**
```nginx
cmd1 | cmd2 | cmd3
```
Send output of one command as input for another.
