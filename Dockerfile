# Base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py"]
