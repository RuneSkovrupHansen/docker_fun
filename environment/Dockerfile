FROM ubuntu

# Specify environment variable
ENV FILENAME="foo"
ENV CONTENT="bar"

# Specify RUN instruction using envrionment variables since they persist to the container
RUN /bin/bash -c 'touch "$FILENAME"; echo "$CONTENT" > "$FILENAME"'

# Specify RUN instruction with non-persistent environment variable which will persist to the container
RUN DIRNAME="foobar" /bin/bash -c 'mkdir "$DIRNAME"; mv "$FILENAME" "$DIRNAME"'

CMD /bin/bash -c 'echo filename: "$FILENAME", content: "$CONTENT", dirname: "$DIRNAME"' 

# Output of building the Dockerfile is:

# filename: foo, content: bar, dirname:

# Since $DIRNAME has not persisted into the container
