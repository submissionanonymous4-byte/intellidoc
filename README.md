# IntelliDoc - AI-Powered Document Processing and Agent Orchestration Platform

IntelliDoc is a comprehensive platform for document processing, vector search, and AI agent orchestration. It enables users to create projects, upload documents, process them with AI, and build complex agent workflows with drag-and-drop orchestration.

## Features

- **Document Processing**: Upload and process documents with AI-powered vector search
- **Agent Orchestration**: Drag-and-drop interface for building AI agent workflows
- **Project Management**: Create and manage multiple independent projects
- **Evaluation Tools**: Evaluate workflows with datasets and similarity scoring
- **Deployment**: Deploy workflows with rate limiting and CORS configuration
- **Activity Tracking**: Monitor conversation history and user interactions

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (version 20.10 or later)
- **Docker Compose** (version 2.0 or later)
- **Git** (for cloning the repository)

To verify your installations:

```bash
docker --version
docker compose version
git --version
```

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd intellidoc
```

### 2. Environment Configuration

Create a `.env` file in the root directory. You can copy from the template:

```bash
cp .env.template .env
```

Then edit the `.env` file and replace all placeholder values with your actual configuration. The following variables are required:

```bash
# Database Configuration
DB_NAME=ai_catalogue_db
DB_USER=ai_catalogue_user
DB_PASSWORD=your_secure_password
DB_PORT=5432

# Milvus Vector Database
MILVUS_ROOT_USER=milvusadmin
MILVUS_ROOT_PASSWORD=your_secure_milvus_password
MILVUS_PORT=19530

# MinIO Object Storage
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=your_secure_minio_password

# Django Configuration
DJANGO_SECRET_KEY=your-super-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# API Keys (Optional - can be configured later in the UI)
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# Project API Key Encryption (Required)
PROJECT_API_KEY_ENCRYPTION_KEY=your-32-character-encryption-key

# PgAdmin (Optional)
PGADMIN_EMAIL=admin@example.com
PGADMIN_PASSWORD=admin123
```

**Important**: Replace all placeholder values with secure passwords and keys. The `PROJECT_API_KEY_ENCRYPTION_KEY` should be a 32-character string used for encrypting project-specific API keys.

### 3. Start the Application

Run the development startup script:

```bash
./scripts/start-dev.sh
```

This script will:
- Check for Docker and Docker Compose
- Validate your `.env` file
- Start all required services (PostgreSQL, Milvus, MinIO, etcd, ChromaDB)
- Build and start the backend and frontend containers
- Display access URLs and login information

The startup process may take 2-3 minutes, especially on first run as it downloads Docker images and initializes databases.

### 4. Verify Services

Once the script completes, verify all services are running:

```bash
docker compose ps
```

You should see all services in "Up" or "healthy" status.

## Creating a Superuser

To access the Django admin panel and the frontend application, you need to create a superuser account.

### Method 1: Using Docker Exec (Recommended)

After the services are running, execute the following command:

```bash
docker compose exec backend python manage.py createsuperuser
```

You will be prompted to enter:
- **Email**: Your email address (e.g., `admin@example.com`)
- **Password**: A secure password (you'll be asked to enter it twice)
- **First Name** (optional)
- **Last Name** (optional)

### Method 2: Using Django Shell

Alternatively, you can create a superuser programmatically:

```bash
docker compose exec backend python manage.py shell
```

Then in the Python shell:

```python
from users.models import User
User.objects.create_superuser(
    email='admin@example.com',
    password='your_secure_password',
    first_name='Admin',
    last_name='User'
)
exit()
```

### Method 3: Using Management Command

If you have a setup script that creates a default superuser, you can run:

```bash
docker compose exec backend python manage.py setup_container_data
```

## Accessing the Application

Once the services are running and you've created a superuser, you can access:

### Frontend Application
- **URL**: http://localhost:5173
- **Login**: Use the email and password you created for the superuser

### Backend API
- **URL**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/

### Django Admin Panel
- **URL**: http://localhost:8000/admin/
- **Login**: Use your superuser credentials

### Additional Services
- **PgAdmin** (Database Management): http://localhost:8080
  - Email: `admin@example.com` (or as configured in `.env`)
  - Password: `admin123` (or as configured in `.env`)
- **Attu** (Milvus UI): http://localhost:3001
  - Milvus Address: `milvus:19530`
  - Username: As configured in `MILVUS_ROOT_USER` in `.env`
  - Password: As configured in `MILVUS_ROOT_PASSWORD` in `.env`
- **ChromaDB API**: http://localhost:8001

## Project Structure

```
intellidoc/
├── backend/              # Django backend application
│   ├── agent_orchestration/  # Agent workflow orchestration
│   ├── api/             # REST API endpoints
│   ├── core/            # Django core settings
│   ├── templates/       # Project templates
│   ├── users/           # User management
│   ├── vector_search/   # Document processing and vector search
│   └── manage.py        # Django management script
├── frontend/            # SvelteKit frontend application
│   └── my-sveltekit-app/
├── scripts/             # Utility scripts
│   └── start-dev.sh     # Development startup script
├── nginx/               # Nginx configuration
├── docker-compose.yml   # Docker Compose configuration
└── .env                 # Environment variables (create this)
```

## Common Commands

### View Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f frontend-dev
docker compose logs -f milvus
```

### Restart Services

```bash
# Restart all services
docker compose restart

# Restart specific service
docker compose restart backend
docker compose restart frontend-dev
```

### Stop Services

```bash
# Stop all services
docker compose down

# Stop and remove volumes (⚠️ This will delete data)
docker compose down -v
```

### Database Migrations

```bash
# Run migrations
docker compose exec backend python manage.py migrate

# Create new migrations
docker compose exec backend python manage.py makemigrations
```

### Access Django Shell

```bash
docker compose exec backend python manage.py shell
```

## First Steps After Setup

1. **Login to the Application**
   - Navigate to http://localhost:5173
   - Login with your superuser credentials

2. **Create a Project**
   - Click on "AICC-IntelliDoc" from the dashboard
   - Click "Create New Project"
   - Enter project name, description, and select "Aicc Intellidoc V2" template

3. **Configure API Keys**
   - In your project, go to "Overview" section
   - Click "API Key Management"
   - Add your LLM provider API keys (OpenAI, Anthropic, Google, etc.)

4. **Upload Documents**
   - In the "Overview" section, upload documents using:
     - Select Files
     - Select Folder
     - Upload Zip
   - Click "Start Processing" to begin document processing

5. **Build Agent Workflows**
   - Navigate to "Agent Orchestration"
   - Use the drag-and-drop interface to create agent workflows
   - Configure agents with DocAware toggle and LLM settings

## Troubleshooting

### Services Not Starting

If services fail to start:

1. Check Docker is running: `docker ps`
2. Check logs: `docker compose logs`
3. Verify `.env` file exists and has all required variables
4. Ensure ports are not already in use

### Database Connection Issues

If you see database connection errors:

1. Verify PostgreSQL container is running: `docker compose ps postgres`
2. Check database credentials in `.env` file
3. View PostgreSQL logs: `docker compose logs postgres`

### Milvus Not Ready

Milvus may take 2-3 minutes to initialize:

1. Check Milvus health: `curl http://localhost:9091/healthz`
2. View Milvus logs: `docker compose logs milvus`
3. Wait a few minutes and check again

### Frontend Not Loading

If the frontend doesn't load:

1. Check frontend container: `docker compose ps frontend-dev`
2. View frontend logs: `docker compose logs frontend-dev`
3. Try accessing directly: http://localhost:5173

## Development

### Hot Reload

Both frontend and backend support hot reload in development mode:
- **Frontend**: Edit files in `frontend/my-sveltekit-app/src/` - changes reflect immediately
- **Backend**: Edit files in `backend/` - Django will auto-reload on changes

### Running Tests

```bash
# Run backend tests
docker compose exec backend python manage.py test

# Run specific test
docker compose exec backend python manage.py test users.tests
```

## Production Deployment

For production deployment, use:

```bash
./scripts/start.sh
```

Make sure to:
- Set `DEBUG=False` in `.env`
- Use strong, unique passwords
- Configure proper `ALLOWED_HOSTS`
- Set up SSL/TLS certificates
- Configure proper backup strategies

## Support

For issues or questions:
- Check the logs: `docker compose logs -f`
- Review service status: `docker compose ps`
- Verify environment configuration in `.env`

## License

[Add your license information here]

