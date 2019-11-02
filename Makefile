TAG=$(shell git describe --tags --always)
VERSION=$(TAG:v%=%)
REPO=shawntoffel/vader-server

.PHONY: all docker-build docker-save docker-deploy

docker-build:
	docker build -t $(REPO):$(VERSION) .

docker-save:
	mkdir -p bin && docker save -o bin/image.tar $(REPO):$(VERSION)

docker-deploy:
	docker push $(REPO):$(VERSION)