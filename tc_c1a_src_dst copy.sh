sudo ip link add ifb0001 type ifb
sudo ip link set dev ifb0001 up
sudo tc qdisc add dev vethaa3ae62 ingress
sudo tc filter add dev vethaa3ae62 parent ffff: protocol ip u32 match u32 0 0 flowid 1: action mirred egress redirect dev ifb0001
sudo tc qdisc add dev ifb0001 root handle 1: htb default 1
sudo tc class add dev ifb0001 parent 1: classid 1:1 htb rate 32000000.0kbit
sudo tc class add dev ifb0001 parent 1: classid 1:2 htb rate 32000000.0Kbit ceil 32000000.0Kbit
sudo tc qdisc add dev ifb0001 parent 1:2 handle 2: netem delay 22.0ms
sudo tc filter add dev ifb0001 protocol ip parent 1: prio 5 u32 match ip dst 172.20.0.1/32 match ip src 0.0.0.0/0 match ip dport 32770 0xffff flowid 1:2

sudo ip link add ifb0002 type ifb
sudo ip link set dev ifb0002 up
sudo tc qdisc add dev vethaa3ae62 ingress
sudo tc filter add dev vethaa3ae62 parent ffff: protocol ip u32 match u32 0 0 flowid 1366: action mirred egress redirect dev ifb0002
sudo tc qdisc add dev ifb0002 root handle 1366: htb default 1
sudo tc class add dev ifb0002 parent 1366: classid 1366:1 htb rate 32000000.0kbit
sudo tc class add dev ifb0002 parent 1366: classid 1366:76 htb rate 32000000.0Kbit ceil 32000000.0Kbit
sudo tc qdisc add dev ifb0002 parent 1366:76 handle 2117: netem delay 66.0ms
sudo tc filter add dev ifb0002 protocol ip parent 1366: prio 5 u32 match ip dst 172.20.0.1/32 match ip src 0.0.0.0/0 match ip dport 32784 0xffff flowid 1366:76

# sudo ip link add ifb0001 type ifb
# sudo ip link set dev ifb0001 up
# sudo tc qdisc add dev vethaa3ae62 ingress
# sudo tc filter add dev vethaa3ae62 parent ffff: protocol ip u32 match u32 0 0 flowid 1366: action mirred egress redirect dev ifb0001
# sudo tc qdisc add dev ifb0001 root handle 1366: htb default 1
# sudo tc class add dev ifb0001 parent 1366: classid 1366:1 htb rate 32000000.0kbit
# sudo tc class add dev ifb0001 parent 1366: classid 1366:76 htb rate 32000000.0Kbit ceil 32000000.0Kbit
# sudo tc qdisc add dev ifb0001 parent 1366:76 handle 2117: netem delay 22.0ms
# sudo tc filter add dev ifb0001 protocol ip parent 1366: prio 5 u32 match ip dst 172.20.0.1/32 match ip src 0.0.0.0/0 match ip dport 32784 0xffff flowid 1366:76