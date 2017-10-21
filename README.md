# Bitex Crypto Exchange

## Joining the blockchain

 1. Install [Docker](https://www.docker.com/)
 2. Install [Docker-Compose](https://docs.docker.com/compose/)
 3. `docker-compose up`
 4. tun run as deamon
 5. `docker-compose up -d`

Setup will spin of next services:
- http://localhost:8080/  -- Demo Exchange
- http://localhost:61208/ -- Exchange Status and Monitoring

Stop all containers: `docker ps -aq | xargs docker stop`
