
docker rm -f trust-node
docker rm -f generic-node1
docker rm -f generic-node2

docker build -t pful/logchain-s-trust-node:0.1 -f trust_peer.dockerfile .
docker build -t pful/logchain-s-generic-node:0.1 -f generic_peer.dockerfile .

docker run --name trust-node -d -v P:/logchain-s/confs/trust:/conf --net logchainnet --ip 10.50.0.10 pful/logchain-s-trust-node:0.1
docker run --name generic-node1 -d -v P:/logchain-s/confs/generic1:/conf --net logchainnet --ip 10.50.0.30 -p 5000:5000 pful/logchain-s-generic-node:0.1
docker run --name generic-node2 -d -v P:/logchain-s/confs/generic2:/conf --net logchainnet --ip 10.50.0.31 -p 5001:5000 pful/logchain-s-generic-node:0.1
