# ONOS_optimal_placement
## Flow Setup Time
**The delay between Switch and Controller:**

d(s-to-c) = 4 \* (the sum of all switch-to-controller delays along the forwarding path)

dsc=4i=1ndsi-csi

dsc           The total delay from all switches to his own master controller
i               The ith switch along forwarding path
n              The number of switch along forwarding path
dsi-csi    The delay from ith switch to his own master controller
si             The ith switch
csi           The master controller of si

**The delay between Controller and Atomix:**

If the source and destination switch are managed by the **same** controller

- If all switches are managed by the same controller
  - d(c-to-a) = [2 \* (the sum of delays between the master controller to all Atomix nodes)] / the number of Atomix nodes

dca=2i=1, j=1n,mdcsi-ajm

- d(c-to-a) = [(2 \* (the sum of delays between the master controller of the source switch to all Atomix nodes)) + (the sum of delays between the master controller of each middle switch to all Atomix nodes) + (the sum of delays between the master controller of the destination switch to all Atomix nodes)] / the number of Atomix nodes

dca=2j=1mdcss-aj+i=2, j=1n-2,mdcsi-aj+j=1mdcsd-ajm

If the source and destination switch are managed by the **different** controller

- d(c-to-a) = [(2 \* (the sum of delays between the master controller of the source switch to all Atomix nodes)) + (the sum of delays between the master controller of each middle switch to all Atomix nodes) + 2 \* (the sum of delays between the master controller of the destination switch to all Atomix nodes)] / the number of Atomix nodes

dca=2j=1mdcss-aj+i=2, j=1n-2,mdcsi-aj+2j=1mdcsd-ajm

dca          The total delay from master controllers of all switches along forwarding path to all Atomix nodes
i               The ith switch along forwarding path

j               The jth Atomix node
n              The number of switch along forwarding path
m             The number of Atomix node
dcss-aj    The delay from master controller of source switch to jth Atomix node
dcsi-aj    The delay from master controller of ith switch  to jth Atomix node
dcsd-aj    The delay from master controller of destination switch to jth Atomix node
si             The ith switch
csi           The master controller of si

**

**The delay between Atomix and Atomix:**

d(a-to-a) = [(2 \* (the sum of the **minimum** delay between each Atomix node to the other all Atomix nodes))] / the number of Atomix nodes

daa=2j=1mmin⁡(daj-aj')m

daa                        The total delay within Atomix nodes

j                              The jth Atomix node

j'                            The other all Atomix nodes except jth Atomix
m                           The number of Atomix node
mindaj-aj'   The minimum delay from jth Atomix node to other all Atomix nodes




||**(1)**|**(2)**|**(3)**|
| :- | :- | :- | :- |
|FST (Total)|<p>4\*(s1c1+s3c1+s2c1)<br>+</p><p>[2\*(c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3)]/3<br>+</p><p>[2\*(a1a2 + a2a1 +a3a2)]/3</p>|<p>4\*(s1c1+s3c1+s2c2)<br>+</p><p>[2\*(c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3) + 2\*(c2a1 + c2a2 + c2a3)]/3<br>+</p><p>[2\*(a1a2 + a2a1 +a3a2)]/3</p>|<p>4\*(s1c1+s3c2+s2c1)<br>+</p><p>[2\*(c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3)]/3<br>+</p><p>[2\*(a1a2 + a2a1 +a3a2)]/3</p>|
|Switch to Controller|4\*(s1c1+s3c1+s2c1)|4\*(s1c1+s3c1+s2c2)|4\*(s1c1+s3c2+s2c1)|
|Controller to Atomix|[2\*(c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3)]/3|[2\*(c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3) + 2\*(c2a1 + c2a2 + c2a3)]/3|[2\*(c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3) + (c1a1 + c1a2 + c1a3)]/3|
|<p>Atomix to Atomix</p><p></p><p>*If:*</p><p>*a1a2 = 10 = a2a1,*</p><p>*a1a3 = 30 = a3a1,*</p><p>*a2a3 = 20 = a3a2*</p><p><br>*We can get:*</p><p>*For a1: min is a1a2 = 10*</p><p>*For a2: min is a2a1 = 10*</p><p>*For a3: min is a3a2 = 20*</p>|[2\*(a1a2 + a2a1 +a3a2)]/3|[2\*(a1a2 + a2a1 +a3a2)]/3|[2\*(a1a2 + a2a1 +a3a2)]/3|


