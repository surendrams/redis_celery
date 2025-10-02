# Step 1:

### Installing and verifying the Redis using docker
```bash
docker compose up -d
docker ps
```

### Stop all running containers
```bash
docker stop $(docker ps -q)
```
### Remove all containers
```bash
docker rm -f $(docker ps -aq)
```
### Remove all images
```bash
docker rmi -f $(docker images -q)
```
### Full cleanup (containers + networks + images + volumes)
```bash
docker system prune -a --volumes
```
### Stop and remove services - From the same directory as your docker-compose.yml:
```bash
docker compose down
```
### Remove volumes (to reset data completely)
```bash
docker compose down -v
```
### Remove everything (system-wide, across all projects)
### Still the same:
```bash
docker system prune -a --volumes
```
