#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

current_output=$(./pigs-log -m) >/dev/null

if [ "Usage: ./pigs-log"="$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi