iptables -I INPUT -p tcp --dport 1714:1764 -j ACCEPT
iptables -I INPUT -p udp --dport 1714:1764 -j ACCEPT