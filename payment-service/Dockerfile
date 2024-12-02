# Step 1: Use Python base image
FROM python:3.9-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy the requirements.txt file
COPY requirement.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Step 5: Copy the application code into the container
COPY . .

# Step 6: Expose the port the app will run on
EXPOSE 5000

# Step 7: Command to run the application
CMD ["python", "app.py"]

