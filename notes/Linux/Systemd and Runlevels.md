Systemd / Runlevels

Stop GUI (GDM example):
```arduino
sudo systemctl stop gdm
sudo telinit 3
```

Start GUI:
```powershell
sudo systemctl start gdm
sudo telinit 5
```

Shutdown:
```arduino
sudo shutdown -h 10:00 "Maintenance"
```

**Prompt Customization (PS1)**
```bash
echo $PS1
PS1="\u@\h \$ "
```

## **Network / VPN**

Stop WireGuard:
```nginx
sudo systemctl stop wg-quick@wg0
```
Show active connections:
```sql
sudo wg show
```
