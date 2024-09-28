# PostgreSQL Setup on WSL Docker

This guide provides step-by-step instructions to set up PostgreSQL on your Windows Subsystem for Linux (WSL) using Docker. The guide also covers how to persist data using Docker volumes to ensure data safety even if the container is removed.

## Prerequisites

- Windows with WSL installed
- Docker installed on your WSL instance

## Steps

### 1. Pull the PostgreSQL Docker Image

First, pull the latest PostgreSQL Docker image from Docker Hub:

```bash
docker pull postgres
```

### 2. Run PostgreSQL Container
```bash
docker run --name my-postgres -e POSTGRES_PASSWORD=<password> -p 5432:5432 -d postgres
```

### or Persist Data to a Mounted Volume
```commandline
docker run --name my-postgres -e POSTGRES_PASSWORD=<password> -v my_pgdata:/var/lib/postgresql/data -p 5432:5432 -d postgres
```

### Use following credentials to access postgres 
- username: postgres
- password: <password>
- port: 5432
- host: localhost