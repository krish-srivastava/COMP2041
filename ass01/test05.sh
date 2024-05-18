#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

expected_output="usage: pigs-show <commit>:<filename>"
current_output=$(./pigs-show) >/dev/null

if [ "$expected_output"="$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi