# Project README

## Cloning the Project
To clone the project repository from GitHub, follow these steps:

1. Open a terminal on your system.
2. Run the following command:
   ```bash
   git clone https://github.com/abhinavnaik2003/fsd.git
   ```

3. Navigate to the project directory:
   ```bash
   cd fsd
   ```

---

## Installing Docker
If Docker is not already installed on your system, follow these steps to install it:

### For Debian/Ubuntu-based Systems
1. Update your package list:
   ```bash
   sudo apt update
   ```

2. Install Docker:
   ```bash
   sudo apt install docker.io 
   ```
   or
   ```bash
   sudo snap install docker
   ```

3. Start and enable the Docker service:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

4. Verify the installation:
   ```bash
   docker --version
   ```
5. Troubleshoot is "Permisson denied":
   ```bash
   sudo chmod 666 /var/run/docker.sock
    ```
    and
    ```bash
    docker ps
    ```

### For Windows
1. Download Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop/).

2. Run the installer and follow the installation instructions.

3. During installation, ensure the option to enable WSL 2 (Windows Subsystem for Linux) is checked.

4. Once installed, start Docker Desktop and ensure it is running.

5. Verify the installation by opening a Command Prompt or PowerShell and running:
   ```bash
   docker --version
   ```

---

## Running the Project with Docker

### Building the Docker Image
1. Ensure you are in the project directory where the `Dockerfile` is located.

2. Build the Docker image:
   ```bash
   docker build -t <image-name> .
   ```
   Replace `<image-name>` with your desired name for the Docker image (e.g., `django-app`).

### Running the Docker Container
1. Run the container from the built image:
   ```bash
   docker run -p 8000:8000 <image-name>
   ```
   Replace `<image-name>` with the name of your Docker image.

2. Open your browser and visit:
   ```
   http://localhost:8000
   ```
   or 
   ```
   http://0.0.0.0:8000
   ```
   This will display the running application.

### Stopping the Container
To stop the running container, use:
```bash
docker ps
```
This will list all running containers. Identify the container ID or name and stop it:
```bash
docker stop <container-id-or-name>
```

---

## Troubleshooting

1. **Permission Denied Error (Linux)**
   - If you encounter a "permission denied" error when running Docker commands, add your user to the `docker` group:
     ```bash
     sudo usermod -aG docker $USER
     ```
     Then log out and log back in.

2. **Port Already in Use**
   - If port 8000 is already in use, specify a different port when running the container:
     ```bash
     docker run -p 8080:8000 <image-name>
     ```
     Then visit `http://localhost:8080` in your browser.

3. **Docker Not Running**
   - Ensure the Docker service is running:
     ```bash
     sudo systemctl start docker
     ```

4. **Windows-Specific Issues**
   - Ensure WSL 2 is properly installed and running. Follow [Microsoft's WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/) for setup guidance.
   - Restart Docker Desktop if you encounter issues.

---

## Additional Notes
- Make sure to install project dependencies using `requirements.txt` if your project setup requires it.
- For production deployments, replace the Django development server with a production-ready server like Gunicorn, and configure a reverse proxy like Nginx.

For further assistance, refer to the project documentation or contact the project maintainers.

