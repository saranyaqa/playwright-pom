# **Playwright-POM Project**

## 1️⃣ Local Setup (Optional)

### **Install virtual environment**

    bash 

    python3.12 -m venv .venv_playwright
    
### Activate / Deactivate Virtual Environment :
    
    bash 
    
    cd playwright-pom
    source .venv_playwright/bin/activate    # activate
    deactivate                              # deactivate

### PyCharm Setup
    
*  add `.venv_playwright/bin/python` as the Project Interpreter

### Install Dependencies and libraries after activating virtual env : 

    bash 

    pip3 install -r requirements.txt

### Run Tests Locally :
    
    bash 

    cd playwright-pom
    pytest test_sample.py --headed


## 2️⃣ Docker Setup (Recommended)

The project is fully Dockerized—no need to install Python, dependencies, or browsers on your host.

### Build Docker Image :

    bash
    
    docker-compose build

### Run Tests:
    
    bash

    docker-compose up


**OR** use the helper script for convenience:

    ./run-tests.sh


The script will:

1.Build the Docker image if needed.

2.Automatically install Playwright browsers.

3.Run all tests with pytest -v.


#### **Notes**

* The project folder is mounted inside the container, so any changes to tests are reflected immediately without rebuilding.

* By default, tests run in headless mode (no UI). To see the browser UI for debugging, set the environment variable in docker-compose.yml:


    yaml

    environment:

        HEADLESS: "false"


* If you change dependencies (requirements.txt) or Dockerfile, rebuild the image:
    

    bash

        docker-compose build --no-cache


✅ With this setup, Docker handles all dependencies and Playwright browsers, making it easier to run tests consistently across machines or CI/CD pipelines.
