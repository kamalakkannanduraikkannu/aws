#!/bin/bash
docker build -t random:1.0 random/.
docker run random:1.0