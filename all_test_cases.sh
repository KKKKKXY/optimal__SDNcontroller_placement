#   NO.     c1a1	c1a2	c1a3	c2a1	c2a2	c2a3	a1a2	a1a3	a2a3
#   1       100     0	    0	    0	    0	    0	    44	    55	    66
#   2       100	    111	    0	    0	    0	    0	    44	    55	    66
#   3       100	    111	    166	    0	    0	    0	    44	    55	    66
#   4       100	    111	    166	    188	    0	    0	    44	    55	    66
#   5       100	    111	    166	    188	    199	    0	    44	    55	    66
#   6       100	    111	    166	    188	    199	    222	    44	    55	    66
#   7       0	    111	    166	    188	    199	    222	    44	    55	    66
#   8       0	    0	    166	    188	    199	    222	    44	    55	    66
#   9       0	    0	    0	    188	    199	    222	    44	    55	    66
#   10      0	    0	    0	    0	    199	    222	    44	    55	    66
#   11      0	    0	    0	    0	    0	    222	    44	    55	    66
#   12      0	    0	    0	    0	    0	    0	    44	    55	    66


# ONOS1=vethe81505c
# ONOS2=vethd7d673c
# Atomix1=veth882a5d8
# Atomix2=vethc638faf
# Atomix3=vethfdbf734

# ONOS1=vethea8c45b
# ONOS2=veth864c27f
# Atomix1=vetha5f1a7b
# Atomix2=veth44d10f2
# Atomix3=veth1a1e62c
ONOS1=veth20669b7
ONOS2=veth42997c8
Atomix1=veth39a7377
Atomix2=veth7abb6eb
Atomix3=vetha4b093c
Atomix1_ip=172.20.0.2
Atomix2_ip=172.20.0.3
Atomix3_ip=172.20.0.4
S1=
S2=

# No.1
# C1
sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# C2
sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# Atomix
sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip


# # No.1
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
# # sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# # sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# # sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# # sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# # sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.2
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
# sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# # C2
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.3
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
# sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.4
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
# sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.5
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
# sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.6
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 100ms --network $Atomix1_ip
# sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.7
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 111ms --network $Atomix2_ip
# sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.8
# # C1
# sudo tcset $ONOS1 --direction incoming --delay 166ms --network $Atomix3_ip
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.9
# # C1
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 188ms --network $Atomix1_ip
# sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.10
# # C1
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 199ms --network $Atomix2_ip
# sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.11
# # C1
# # C2
# sudo tcset $ONOS2 --direction incoming --delay 222ms --network $Atomix3_ip
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip

# # No.12
# # C1
# # C2
# # Atomix
# sudo tcset $Atomix1 --direction incoming --delay 44ms --network $Atomix2_ip
# sudo tcset $Atomix1 --direction incoming --delay 55ms --network $Atomix3_ip
# sudo tcset $Atomix2 --direction incoming --delay 66ms --network $Atomix3_ip




# #       NO.     s1c1    s1c2    s2c1    s2c2
# #       1       287     0       0       0
# #       2       287     444     0       0
# #       3       287     444     666     0
# #       4       287     444     666     345
# #       5       0       444     0       0
# #       6       0       444     666     0
# #       7       0       444     666     345
# #       8       0       0       666     0
# #       9       0       0       666     345
# #       20      0       0       0       345

# ONOS1=veth03a5e1e
# ONOS2=veth89d419f
# S1=
# S2=

# # No.1
# # s1c1
# sudo tcset $ONOS1 --direction incoming --delay 287ms --network 172.20.0.1 --port $S1

# # # No.2
# # # s1c1
# # sudo tcset $ONOS1 --direction incoming --delay 287ms --network 172.20.0.1 --port $S1
# # # s1c2
# # sudo tcset $ONOS2 --direction incoming --delay 444ms --network 172.20.0.1 --port $S1

# # # No.3
# # # s1c1
# # sudo tcset $ONOS1 --direction incoming --delay 287ms --network 172.20.0.1 --port $S1
# # # s1c2
# # sudo tcset $ONOS2 --direction incoming --delay 444ms --network 172.20.0.1 --port $S1
# # # s2c1
# # sudo tcset $ONOS1 --direction incoming --delay 666ms --network 172.20.0.1 --port $S2

# # # No.4
# # # s1c1
# # sudo tcset $ONOS1 --direction incoming --delay 287ms --network 172.20.0.1 --port $S1
# # # s1c2
# # sudo tcset $ONOS2 --direction incoming --delay 444ms --network 172.20.0.1 --port $S1
# # # s2c1
# # sudo tcset $ONOS1 --direction incoming --delay 666ms --network 172.20.0.1 --port $S2
# # # s2c2
# # sudo tcset $ONOS2 --direction incoming --delay 345ms --network 172.20.0.1 --port $S2

# # # No.5
# # # s1c2
# # sudo tcset $ONOS2 --direction incoming --delay 444ms --network 172.20.0.1 --port $S1

# # # No.6
# # # s1c2
# # sudo tcset $ONOS2 --direction incoming --delay 444ms --network 172.20.0.1 --port $S1
# # # s2c1
# # sudo tcset $ONOS1 --direction incoming --delay 666ms --network 172.20.0.1 --port $S2

# # # No.7
# # # s1c2
# # sudo tcset $ONOS2 --direction incoming --delay 444ms --network 172.20.0.1 --port $S1
# # # s2c1
# # sudo tcset $ONOS1 --direction incoming --delay 666ms --network 172.20.0.1 --port $S2
# # # s2c2
# # sudo tcset $ONOS2 --direction incoming --delay 345ms --network 172.20.0.1 --port $S2

# # # No.8
# # # s2c1
# # sudo tcset $ONOS1 --direction incoming --delay 666ms --network 172.20.0.1 --port $S2

# # # No.9
# # # s2c1
# # sudo tcset $ONOS1 --direction incoming --delay 666ms --network 172.20.0.1 --port $S2
# # # s2c2
# # sudo tcset $ONOS2 --direction incoming --delay 345ms --network 172.20.0.1 --port $S2

# # # No.10
# # # s2c2
# # sudo tcset $ONOS2 --direction incoming --delay 345ms --network 172.20.0.1 --port $S2