REPO=sacon
NAME := ml
VERSION := latest
USERID := $(shell id -u)
GROUPID := $(shell id -g)

run:
	docker run \
                --detach=false --interactive --tty --rm \
                -u ${USERID}:${GROUPID} -p 8888:8888  -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix                 \
                --name=${REPO}_${NAME} ${REPO}/${NAME}:${VERSION} bash

run-dev:
	docker run \
		--detach=false --interactive --tty --rm \
		--volume=`pwd`:/app/workspace \
		-p 8888:8888  -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix 		\
		--name=${REPO}_${NAME} ${REPO}/${NAME}:${VERSION} bash
