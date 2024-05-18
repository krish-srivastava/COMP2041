#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

touch a

expected_output=$(exec 2041 pigs-commit -m "a") >/dev/null
current_output=$(./pigs-commit -m "a") >/dev/null

if [ "$expected_output" = "$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi