# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Instalação do WebDriver do Microsoft Edge
RUN wget https://msedgedriver.azureedge.net/121.0.2277.113/edgedriver_linux64.zip \
    && unzip edgedriver_linux64.zip \
    && mv msedgedriver /usr/local/bin/ \
    && rm edgedriver_linux64.zip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org selenium

# Run app.py when the container launches
CMD ["python", "questao6.py"]
