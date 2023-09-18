local_image="adiamb_test"
vol_mounts=-v ${CURDIR}/data:/app/data

requirements.txt: requirements.in
	pip-compile --strip-extras requirements.in > requirements.txt

build: requirements.txt
	docker build -t ${local_image} .

bash:
	docker run -it ${vol_mounts} ${local_image} /bin/bash

jupyter:
	docker run -it -p 8888:8888 ${vol_mounts} ${local_image} \
	jupyter lab --ip=0.0.0.0 --allow-root
