# Contributing
## About
Simple application built with a [Next.js](https://nextjs.org/) frontend and a [FastAPI](https://fastapi.tiangolo.com/) backend.
### Frontend
Uses [pnpm](https://pnpm.io/) as the package manages and [TailwindCSS](https://tailwindcss.com/) and [shadcn/ui](https://ui.shadcn.com/) to simplify styling.
### Backend
Connects to an [Orthanc](https://www.orthanc-server.com/) image database and a [HAPI FHIR](https://hapifhir.io/) server to store patient information.
## Quick Start

### 1. Install necessary tools

Ensure pnpm and Docker are installed (install Docker Compose separately if you aren't using Docker Desktop). 
Instructions to install pnpm can be found [here](https://pnpm.io/installation).

### 2. Set up dependencies

```
# Install dependencies
pnpm i

# Configure environment variables
cp .env.example .env
```

### 3. Set up backend and databases
```
# Enter backend directory
cd backend

# Run docker containers
docker compose up
```

You may need to rebuild if you have existing containers from an older compose config:

```
# Clean rebuild of containers
docker compose up --build
```

### 4. Start Next.js application
```
# Enter frontend directory
cd frontend

# Run app
pnpm dev
```

## Usage

### Backend

Once running, the FastAPI server should be accessible at 0.0.0.0:8000.
