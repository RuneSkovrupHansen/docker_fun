docker build -t censor .
# Use --mount to mount directory/ into the container so that it can be watched
docker run -it --mount type=bind,source="$(pwd)"/directory,target=/opt/censor/directory --rm censor python3 censor.py --directory=directory