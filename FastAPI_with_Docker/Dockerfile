# Python image with python 3.12 as base image
FROM python:3.12 

# Set the working directory inside container to /app 
WORKDIR /app 

# Copy req.txt file from local directory to /app directory in the container
COPY requirements.txt . 

# Install the python dependencies specified in req.txt
# No-cache-dir : Don't cache the installed package to save space
# Upgrade : Upgrade all specified packages to the newest available versions
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory (containing main.py and other files from local dir. to /app dir in container)
COPY ./app /app 

# Set the commands to run the application using uvicorn
# "main:app" tells uvicorn to look for an object called app in a module named main (main.py)
# --host 0.0.0.0: Bind socket to all network interface (makes server accessible from outside the container)
# --port 80: Listen on port 80 inside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]










