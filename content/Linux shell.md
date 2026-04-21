```
sudo mount -t ntfs-3g /dev/sda1 /mnt/usb
```

```
sudo rm /var/lib/libvirt/dnsmasq/virbr0.macs
```
```
sudo virsh net-start default
```

```
systemctl status 
```
```
systemctl start/stop/restart
```
```
systemctl reload
```
```
systemctl enable/disable
```
```
systemctl list-units --type=service --state=running
```
```
systemctl list-dependencies
```

```
journalctl -u -f
```
```
journalctl -b
```
```
journalctl -p 3 -b
```
```
journalctl --since "1 hour ago"
```

```
df -h
```

```
last
```

```
journalctl -u sshd -f
```
```
journalctl -u sshd | grep "Failed password"

```
```
journalctl -u sshd | grep "Accepted"

```

