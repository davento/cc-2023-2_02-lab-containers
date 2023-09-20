# Lab 2 - Hello Containers

## Task instructions
1. Write a Dockerfile with support to Apache Spark >=1.0.0 and <=1.5.2
2. Use the WordCount program as an example of the dataflow
3. Verify that the WordCount saves the output in decreasing order
4. Include the WordCount in the Dockerfile
5. Prepare the container so that once it's executed, it uses a volume containing the input to be passed to the Wordcount and also saves the output in the same volume
6. Test the program with the input file provided, saving the output file and using cAdvisor to monitor the resource usage

## Derivables
- Video commenting the homework
- Dockerfile and output file
- Link of the Docker image uploaded in Docker Hub

## Running Instructions

Build Spark container:
```
docker build -t spark-wordcount:1.0 .
```

Run cAdvisor container:
```
docker run --volume=/:/rootfs:ro --volume=/var/run:/var/run:ro --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --volume=/dev/disk/:/dev/disk:ro --publish=8080:8080 -detach=true --name=cadvisor google/cadvisor:latest
```

Run Spark container:
```
docker run --rm -v ${PWD}/data:/data spark-wordcount:1.0
```

Remove cAdvisor container:
```
docker stop cadvisor
docker rm cadvisor
```

Publish image:
```
docker login
docker tag spark-wordcount:1.0 <user>/spark-wordcount:latest
docker push <user>/spark-wordcount:latest
```

## Additional Resources

- [Spark image used](https://hub.docker.com/r/gettyimages/spark/)
- [cAdvisor Repository](https://github.com/google/cadvisor)