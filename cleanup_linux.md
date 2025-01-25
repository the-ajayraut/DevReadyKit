### Clean up ubuntu disk storage by deleting tmp/thumbnails/unused libraries 

```sudo apt-get install clean 
sudo apt-get autoremove --purge 
sudo journalctl --vacuum-time=2weeks  
rm -rf ~/.cache/thumbnails/* /tmp/*
```