# NOMAD Training Metadata Manager

A highly modular and extensible software system designed to manage, search, and maintain metadata associated with NOMAD training materials. This project aims to be a full-stack application using a modern tech stack, providing a professional-grade example of architecture, UI/UX, and potential GPT integration.

## Core Technologies

*   **Backend:** Python, FastAPI, Pydantic, MongoDB
*   **Frontend:** React, Next.js, TypeScript, Tailwind CSS
*   **DevOps:** Docker, Docker Compose (for local development)
*   **Authentication:** Keycloak

## Project Structure

*   `/backend`: Contains the FastAPI backend application.
*   `/frontend`: Contains the Next.js frontend application.
*   `/shared`: Intended for code/schemas shared between backend and frontend (currently empty).
*   `/infra`: Contains infrastructure configurations (e.g., Docker Compose files, NGINX configs).
*   `/docs`: Contains project documentation.

## Getting Started

### Prerequisites

*   Python 3.12+
*   Node.js (latest LTS version recommended)
*   Docker and Docker Compose (for running services like MongoDB and Keycloak, and for containerizing the application)
*   An instance of MongoDB accessible.
*   An instance of Keycloak accessible.

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd nomad-training-navigator3
    ```

2.  **Set up environment variables:**
    Copy the `.env.example` file to `.env` and update the variables as needed:
    ```bash
    cp .env.example .env
    ```
    You will need to fill in details for `MONGO_URI`, `KEYCLOAK_URL`, `FASTAPI_SECRET_KEY`, and optionally `OPENAI_API_KEY`.

3.  **Backend Setup:**
    Navigate to the backend directory:
    ```bash
    cd backend
    ```
    Create a Python virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    ```
    Install dependencies (initially, this will be FastAPI and Uvicorn, more will be added):
    ```bash
    pip install -r requirements.txt
    # (requirements.txt currently only contains FastAPI, uvicorn, python-dotenv, etc. - will be expanded)
    # For now, you might need to manually install:
    # pip install fastapi uvicorn[standard] python-dotenv pydantic
    ```

4.  **Frontend Setup:**
    Navigate to the frontend directory:
    ```bash
    cd frontend
    ```
    Install dependencies:
    ```bash
    npm install
    # or
    # yarn install
    ```

### Running the Application (Development)

1.  **Run Backend:**
    Navigate to the `backend` directory and run:
    ```bash
    # Ensure your virtual environment is activated
    # Ensure MongoDB and Keycloak are running and configured in .env
    uvicorn main:app --reload --port 8000
    ```
    The API will be available at `http://localhost:8000`.

2.  **Run Frontend:**
    Navigate to the `frontend` directory and run:
    ```bash
    npm run dev
    # or
    # yarn dev
    ```
    The frontend application will be available at `http://localhost:3000`.

## Contributing

Please refer to the documentation in the `/docs` directory for contribution guidelines and development practices (to be added).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
