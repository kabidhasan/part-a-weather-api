apiVersion: apps/v1
kind: Deployment
metadata:
  name: weather-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: weather-api
  template:
    metadata:
      labels:
        app: weather-api
    spec:
      containers:
        - name: weather-api
          image: DOCKER_IMAGE_PLACEHOLDER
          ports:
            - containerPort: 5000
          env:
            - name: WEATHER_API_KEY
              valueFrom:
                secretKeyRef:
                  name: weather-api-key
                  key: WEATHER_API_KEY
