REPO=sacon
NAME := ml
VERSION := $(shell cat VERSION)
USERID := $(shell id -u)
GROUPID := $(shell id -g)

setup:
	mkvirtualenv -a ./ -r ./requirements.txt ${NAME}

build: 
	docker build \
		--file=./Dockerfile \
		--tag=${REPO}/${NAME}:${VERSION} .

build_latest:
	docker tag ${REPO}/${NAME}:${VERSION} ${REPO}/${NAME}:latest 

push_latest: build_latest
	docker push ${REPO}/${NAME}:latest 

push: build
	docker push ${REPO}/${NAME}:${VERSION}


run:
	docker run \
		--detach=false --interactive --tty --rm \
		--name=${NAME} ${REPO}/${NAME}:${VERSION}

run-dev:
	docker run \
		--detach=false --interactive --tty --rm \
		--volume=`pwd`:/app \
		-u ${USERID}:${GROUPID} -p 8888:8888  -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix 		\
		--name=${REPO}_${NAME} ${REPO}/${NAME}:${VERSION} bash
