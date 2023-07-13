# !/bin/bash

sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)

creatorKey="creator"
creatorValue="onos-cluster-create"

netName="atomix-1"
customSubnet=172.20.0.0/16
customGateway=172.20.0.1

netName_1="atomix-2"
customSubnet_1=172.21.0.0/16
customGateway_1=172.21.0.1

sudo docker network create -d bridge $netName --subnet $customSubnet --gateway $customGateway --label "$creatorKey=$creatorValue"
sudo docker network create -d bridge $netName_1 --subnet $customSubnet_1 --gateway $customGateway_1 --label "$creatorKey=$creatorValue"
sudo docker create -t --name atomix-1 --hostname atomix-1 --net "atomix-1" --ip 172.20.0.2 atomix/atomix:3.1.5
sudo docker create -t --name atomix-2 --hostname atomix-2 --net "atomix-2" --ip 172.21.0.2 atomix/atomix:3.1.5
export OC1=172.20.0.2
export OC1=172.21.0.2

cd
./onos/tools/test/bin/atomix-gen-config 172.20.0.2 /tmp/atomix-1.conf 172.20.0.2 172.21.0.2
./onos/tools/test/bin/atomix-gen-config 172.21.0.2 /tmp/atomix-2.conf 172.20.0.2 172.21.0.2
sudo docker cp /tmp/atomix-1.conf atomix-1:/opt/atomix/conf/atomix.conf
sudo docker cp /tmp/atomix-2.conf atomix-2:/opt/atomix/conf/atomix.conf
sudo docker start atomix-1
sudo docker start atomix-2
# sudo docker inspect atomix-1 | grep -i ipaddress
# sudo docker inspect atomix-2 | grep -i ipaddress


netName_2="onos1"
customSubnet_2=172.22.0.0/16
customGateway_2=172.22.0.1
sudo docker network create -d bridge $netName_2 --subnet $customSubnet_2 --gateway $customGateway_2 --label "$creatorKey=$creatorValue"
sudo docker run -t -d --name onos1 --hostname onos1 --net $netName_2 --ip 172.22.0.2 -e ONOS_APPS="drivers,openflow-base,netcfghostprovider,lldpprovider,gui2" onosproject/onos:2.2.2
sudo docker inspect onos1 | grep -i ipaddress

cd
./onos/tools/test/bin/onos-gen-config 172.22.0.2 /tmp/cluster-1.json -n 172.20.0.2 172.21.0.2
sudo docker exec onos1 mkdir /root/onos/config
sudo docker cp /tmp/cluster-1.json onos1:/root/onos/config/cluster.json
sudo docker restart onos1





# !/bin/bash

# sudo docker stop $(sudo docker ps -a -q)
# sudo docker rm $(sudo docker ps -a -q)
# # 1. Download Atomix docker image:
# # sudo docker pull atomix/atomix:3.1.5
# # netName="onos-cluster-net"
# creatorKey="creator"
# creatorValue="onos-cluster-create"

# # create_net_ine(){
# #   if [[ ! $(sudo docker network ls --format "{{.Name}}" --filter label=$creatorKey=$creatorValue) ]];
# #   then
# #       sudo docker network create -d bridge $netName --subnet $customSubnet --gateway $customGateway --label "$creatorKey=$creatorValue" >/dev/null
# #       echo "Creating Docker network $netName ..."
# #   fi
# # }

# netName="atomix-1"
# customSubnet=172.20.0.0/16
# customGateway=172.20.0.1

# netName_1="atomix-2"
# customSubnet_1=172.21.0.0/16
# customGateway_1=172.21.0.1

# sudo docker network create -d bridge $netName --subnet $customSubnet --gateway $customGateway --label "$creatorKey=$creatorValue"
# sudo docker network create -d bridge $netName_1 --subnet $customSubnet_1 --gateway $customGateway_1 --label "$creatorKey=$creatorValue"
# # sudo docker create -t --name atomix-1 --hostname atomix-1 --net $netName --ip $currentIp atomix/atomix:$atomixVersion >/dev/null
# sudo docker create -t --name atomix-1 --hostname atomix-1 --net "atomix-1" --ip 172.20.0.2 atomix/atomix:3.1.5
# sudo docker create -t --name atomix-2 --hostname atomix-2 --net "atomix-2" --ip 172.21.0.2 atomix/atomix:3.1.5
# export OC1=172.20.0.2
# export OC1=172.21.0.2
# # 2. Run three instacnes of Atomix:
# # sudo docker run -t -d --name atomix-1 --hostname atomix-1 --ip 172.20.0.2 atomix/atomix:3.1.5
# # sudo docker run -t -d --name atomix-2 --ip 172.20.0.3 atomix/atomix:3.1.5
# # sudo docker run -t -d --name atomix-3 --ip 172.20.0.4 atomix/atomix:3.1.5

# # 3. Check docker IP of Atomix instances;
# sudo docker inspect atomix-1 | grep -i ipaddress
# sudo docker inspect atomix-2 | grep -i ipaddress
# # sudo docker inspect atomix-2 | grep -i ipaddress
# # sudo docker inspect atomix-3 | grep -i ipaddress

# # 4. Check out ONOS source code:
# # sudo git clone https://gerrit.onosproject.org/onos

# # 5. Set relevant environment variables to docker IP of Atomix instances obtained above:
# # export OC1=172.20.0.2
# # export OC2=172.20.0.3
# # export OC3=172.20.0.4

# # 6. Generate Atomix configuration files:
# cd
# ./onos/tools/test/bin/atomix-gen-config 172.20.0.2 /tmp/atomix-1.conf 172.20.0.2 172.21.0.2
# ./onos/tools/test/bin/atomix-gen-config 172.21.0.2 /tmp/atomix-2.conf 172.20.0.2 172.21.0.2
# # ./onos/tools/test/bin/atomix-gen-config 172.20.0.3 /tmp/atomix-2.conf 172.20.0.2 172.20.0.3 172.20.0.4
# # ./onos/tools/test/bin/atomix-gen-config 172.20.0.4 /tmp/atomix-3.conf 172.20.0.2 172.20.0.3 172.20.0.4

# # # 7. Copy Atomix configuration to docker instances:
# sudo docker cp /tmp/atomix-1.conf atomix-1:/opt/atomix/conf/atomix.conf
# sudo docker cp /tmp/atomix-2.conf atomix-2:/opt/atomix/conf/atomix.conf
# # sudo docker cp /tmp/atomix-3.conf atomix-3:/opt/atomix/conf/atomix.conf

# # # 8. Restart Atomix docker instances for configuration to take effect:
# sudo docker start atomix-1
# sudo docker start atomix-2
# # sudo docker restart atomix-2
# # sudo docker restart atomix-3

# sudo docker inspect atomix-1 | grep -i ipaddress
# sudo docker inspect atomix-2 | grep -i ipaddress




# netName_2="onos1"
# customSubnet_2=172.22.0.0/16
# customGateway_2=172.22.0.1

# sudo docker network create -d bridge $netName_2 --subnet $customSubnet_2 --gateway $customGateway_2 --label "$creatorKey=$creatorValue"

# # # 9. Download ONOS docker image:
# # # sudo docker pull onosproject/onos:2.2.2

# # # 10. Run three ONOS docker instances:
# sudo docker run -t -d --name onos1 --hostname onos1 --net $netName_2 --ip 172.22.0.2 -e ONOS_APPS="drivers,openflow-base,netcfghostprovider,lldpprovider,gui2" onosproject/onos:2.2.2
# # sudo docker run -t -d --name onos2 onosproject/onos:2.2.2
# # sudo docker run -t -d --name onos3 onosproject/onos:2.2.2

# # # 11. Check docker IP of ONOS instances;
# sudo docker inspect onos1 | grep -i ipaddress
# # sudo docker inspect onos2 | grep -i ipaddress
# # sudo docker inspect onos3 | grep -i ipaddress

# # # 12. Generate ONOS cluster configuration files using docker IP obtained above:
# cd
# ./onos/tools/test/bin/onos-gen-config 172.22.0.2 /tmp/cluster-1.json -n 172.20.0.2 172.21.0.2
# # ./tools/test/bin/onos-gen-config 172.20.0.6 ~/cluster-2.json -n 172.20.0.2 172.20.0.3 172.20.0.4
# # ./tools/test/bin/onos-gen-config 172.20.0.7 ~/cluster-3.json -n 172.20.0.2 172.20.0.3 172.20.0.4

# # # 13. Create config directory for ONOS docker instances:
# sudo docker exec onos1 mkdir /root/onos/config
# # sudo docker exec onos2 mkdir /root/onos/config
# # sudo docker exec onos3 mkdir /root/onos/config

# # # 14. Copy ONOS cluster configuration to docker instances:
# sudo docker cp /tmp/cluster-1.json onos1:/root/onos/config/cluster.json
# # sudo docker cp ~/cluster-2.json onos2:/root/onos/config/cluster.json
# # sudo docker cp ~/cluster-3.json onos3:/root/onos/config/cluster.json

# # # 15. Restart ONOS docker instances for configuration to take effect:
# sudo docker restart onos1
# # sudo docker restart onos2
# # sudo docker restart onos3

# # # 16. Login ONOS Web UI to check cluster formation.