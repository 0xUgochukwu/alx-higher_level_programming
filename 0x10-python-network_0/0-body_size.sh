#!/bin/bash
# Display the response size
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
