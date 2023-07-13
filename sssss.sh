docker pull atomix/atomix:3.1.5
docker run -t -d --name atomix-1 --ip 0.0.0.0 atomix/atomix:3.1.5
# docker inspect atomix-1 | grep -i ipaddress
git clone https://gerrit.onosproject.org/onos
export OC1=0.0.0.0
cd /path/to/your/onos/source/root
./tools/test/bin/atomix-gen-config 172.17.0.2 ~/atomix-1.conf 172.17.0.2 172.17.0.3 172.17.0.4

docker cp ~/atomix-1.conf atomix-1:/opt/atomix/conf/atomix.conf
docker restart atomix-1
docker pull onosproject/onos:2.2.2
docker run -t -d --name onos1 onosproject/onos:2.2.2
docker inspect onos1 | grep -i ipaddress

cd /path/to/your/onos/source/root
./tools/test/bin/onos-gen-config 172.17.0.5 ~/cluster-1.json -n 172.17.0.2 172.17.0.3 172.17.0.4

docker exec onos1 mkdir /root/onos/config
docker cp ~/cluster-1.json onos1:/root/onos/config/cluster.json
docker restart onos1

sudo tcset veth03a5e1e --direction incoming --delay 222ms --network 172.20.0.1 --port 33294
sudo tcset veth03a5e1e --delay 333ms --network 172.20.0.2/32

sudo tcset veth03a5e1e --direction incoming --delay 333ms --network 172.20.0.2/32
sudo tcset veth03a5e1e --delay 222ms --network 172.20.0.1 --port 33294