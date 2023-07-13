#!/bin/bash

#Some infor from: https://github.com/ralish/bash-script-template/blob/stable/script.sh

# Handling arguments, taken from (goodmami)
# https://gist.github.com/goodmami/f16bf95c894ff28548e31dc7ab9ce27b

netName="onos-cluster-net"

# Handling arguments, taken from (goodmami)
# https://gist.github.com/goodmami/f16bf95c894ff28548e31dc7ab9ce27b
die() { echo "$1"; exit 1; }

usage() {
  cat <<EOF
    Options:
      -h, --help                  display this help message
      -oi, --onosIpPostfix        allocated ipaddress for ONOS: e.g. 172.20.0.3
      -i, --id                    the id for ONOS: e.g 1,2,3,4...
      # -ai, --atomixIp             allocated ipaddress of Atomix: e.g. 172.20.0.2
EOF
}

parse_params() {
# Option parsing
  while [ $# -gt 0 ]; do
      case "$1" in
          --*=*)                a="${1#*=}"; o="${1#*=}"; shift; set -- "$a" "$o" "$@" ;;
          -h|--help)            usage; exit 0; shift ;;
          -oi|--onosIpPostfix)  onosIpPostfix="$2"; shift 2 ;;
          -i|--id)              id="$2"; shift 2 ;;
          # -ai|--atomixIp)      atomixIp="$2"; shift 2 ;;
          --)                   shift; break ;;
          -*)                   usage; die "Invalid option: $1" ;;
          *)                    break ;;
      esac
  done
  echo "onos name: onos$id"
#   echo "onos-version: $onosVersion"
  allocatedONOSIp="172.20.0.$onosIpPostfix"
  echo "onos ip: $allocatedONOSIp"
}


containsElement () {
  local e match="$1"
  shift
  for e; do [[ $e == "$match" ]] && return 0; done
  return 1
}

add_new_onos() {
    echo "Starting onos$id container with IP: $allocatedONOSIp"
    
    # allocatedAtomixIps=("172.20.0.2", "172.20.0.3")
    atomixIp_1="172.20.0.2"
    atomixIp_2="172.20.0.3"
    allocatedAtomixIps+=($atomixIp_1)
    allocatedAtomixIps+=($atomixIp_2)
    echo "${allocatedAtomixIps[*]}"
    
    sudo docker run -t -d \
        --name onos$id \
        --hostname onos$id \
        --net $netName \
        --ip $allocatedONOSIp \
        -e ONOS_APPS="drivers,openflow-base,netcfghostprovider,lldpprovider,gui2" \
        onosproject/onos:2.7.0 >/dev/null
    cd
    ./onos/tools/test/bin/onos-gen-config "$allocatedONOSIp" /tmp/cluster-$id.json -n "${allocatedAtomixIps[*]}" >/dev/null
    sudo docker exec onos$id mkdir /root/onos/config
    echo "Copying configuration to onos$id"
    sudo docker cp /tmp/cluster-$id.json onos$id:/root/onos/config/cluster.json
    echo "Restarting container onos$id"
    sudo docker restart onos$id >/dev/null
}

function main() {

    parse_params "$@"
    
    add_new_onos
}



# Make it rain
main "$@"

# docker run -t -d \
#         --name onos3 \
#         --hostname onos3 \
#         --net onos-cluster-net \
#         --ip 172.20.0.5 \
#         -e ONOS_APPS="drivers,openflow-base,netcfghostprovider,lldpprovider,gui2" \
#         onosproject/onos:2.3.0

# ./onos/tools/test/bin/onos-gen-config 172.20.0.5 /tmp/cluster-3.json -n 172.20.0.2
# docker exec onos3 mkdir /root/onos/config
# docker cp /tmp/cluster-3.json onos3:/root/onos/config/cluster.json
# docker restart onos3