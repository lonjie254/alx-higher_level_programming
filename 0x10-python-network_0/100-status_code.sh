#!/bin/bash
# script that sends a request to a URL passed as an argument & displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
