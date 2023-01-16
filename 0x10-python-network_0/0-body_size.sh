#!/bin/bash
# Get byte size of HTTP response header for a given URL
curl -Is "$1" | grep Content-Length | cut -d ' ' -f2
