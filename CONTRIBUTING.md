# CONTRIBUTING 

## HOW TO RUN DOCKERFILE LOCALLY

### Build Docker Image

```
docker build -t IMAGE_NAME .
```

### Run Docker Image

```
docker run -dp 5000:5000 -v "${pwd}:/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"
```
