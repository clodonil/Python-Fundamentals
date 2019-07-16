#!/bin/bash

docker run --rm --init -v $PWD:/home/marp/app/ -e LANG=en_US.UTF-8 marpteam/marp-cli modulo1.md --allow-local-files  --pdf

mv *pdf pdf/
