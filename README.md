# Bitex Crypto Exchange

## Joining the blockchain

 1. Install [Docker](https://www.docker.com/)
 2. Install [Terraform](https://www.terraform.io/)
 3. `cd terraform/demo`
 4. (Mac only) Change `volume_path` to your docker persistent folder
 5. `terraform get`
 6. `terraform apply`
 7. Type a name for your node.

Setup will spin of next services:
- http://localhost:8080/  -- Demo Exchange
- http://localhost:61208/ -- Exchange Status and Monitoring

Stop all containers: `docker ps -aq | xargs docker stop`
