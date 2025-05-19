#!/bin/sh

if [ -z "$PASSWORD" ]; then
  echo "Error: Missing PASSWORD environment variable."
  exit 1
fi

exec "$@"
