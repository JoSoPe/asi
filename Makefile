B0=@echo 'LXC_BRIDGE="lxcbr0"'
B1=@echo 'LXC_ADDR="172.20.2.10"'
B2=@echo 'LXC_NETMASK="255.255.0.0"'
B3=@echo 'LXC_NETWORK="172.20.2.0/16"'
B4=@echo 'LXC_DHCP_RANGE="172.20.2.142,172.20.2.198"'

E0=@echo "X-S save X-C close --> must have\r"
E1=@echo "auto lo"
E2=@echo "iface lo inet loopback"
E3=@echo "auto eth0"
E4=@echo "iface eth0 inet static"
E5=@echo "address 172.20.2.XX"
E6=@echo "netmask 255.255.0.0"

install:
	sudo apt-get install lxc
	apt-get install lxc-templates
bridge:
	$(B0)
	$(B1)
	$(B2)
	$(B3)
	$(B4)
	emacs /etc/default/lxc-net
bridge_container:
	$(E0)
	$(E1)
	$(E2)
	$(E3)
	$(E4)
	$(E5)
	$(E6)
	cd /etc/network/
	emacs interfaces
ping:
	apt-get install iputils-ping
maquines:
	lxc-ls -f
newcontainer:
	lxc-create -t debian -n $(n)
	lxc-ls -f 
start:
	lxc-start -n $(n)
	lxc-ls -f 
stop:
	lxc-stop -n $(n)
	lxc-ls -f
	brctl show
destroy:
	lxc-destroy -n $(n)
	lxc-ls -f
open:
	lxc-attach -n $(n)
.PHONY:
	clean
clean:
	\rm -f *~ *.o *.elf *.asm *.gz *#
openvp:
	echo "/usr/sbin/openvpn --config client.txt"
vpopen:
	brctl addif lxcbr0 tap0
	ifconfig tap0 up
	brctl show
	echo "editar resolv afegint:"
	echo "nameserver 172.20.2.4"
	echo "fent  make resolv   ja obre el fitxer"
resolv:
	emacs /etc/resolv.conf
