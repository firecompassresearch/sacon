REPO=sacon
NAME := ml
VERSION := latest
USERID := $(shell id -u)
GROUPID := $(shell id -g)

clean: clean-pyc clean-build

clean-pyc:
				find . -name '*.pyc' -exec rm -f {} +
				find . -name '*.pyo' -exec rm -f {} +
				find . -name '*~' -exec rm -f  {} +

clean-build:
				rm -rf build/
				rm -rf dist/
				rm -rf *.egg-info
				rm -rf .pytest_cache/

run:
	docker run \
                --detach=false --interactive --tty --rm \
                -u ${USERID}:${GROUPID} -p 8080:8080  -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix                 \
                --name=${REPO}_${NAME} ${REPO}/${NAME}:${VERSION} bash

run-dev:
	docker run \
		--detach=false --interactive --tty --rm \
		--volume=`pwd`:/app/workspace \
		-p 8080:8080  -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix 		\
		--name=${REPO}_${NAME} ${REPO}/${NAME}:${VERSION} bash
