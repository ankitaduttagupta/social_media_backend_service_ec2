#FROM python:3.11-slim
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY ./app ./app
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]


FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY feed_service/requirements.txt .
RUN pip install -r requirements.txt

# Copy app code and shared common_lib
COPY feed_service/app ./app
COPY common_lib ./common_lib

# Add common_lib to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app/common_lib"

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
