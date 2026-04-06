# Dockerfile
FROM alpine:3.18

RUN apk add --no-cache python3 py3-pip bash build-base libffi-dev

WORKDIR /app

# Copy only the app folder
COPY app/ /app/

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi

EXPOSE 5000

CMD ["python3", "application.py"]
