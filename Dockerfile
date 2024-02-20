# Base image
FROM python:3.10

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Train the model
RUN python ./code/train.py

# Run the application
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
