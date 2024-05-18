#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

expected_output=$(exec 2041 pigs-log) >/dev/null
current_output=$(./pigs-log) >/dev/null

if [ "$expected_output" = "$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi