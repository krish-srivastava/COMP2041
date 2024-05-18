#!/bin/dash

# Creates a temporary directory
TEMP_DIR=$(mktemp -d)
# Copy the pigs file into the temporary directory
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

expected_output=$(exec 2041 pigs-init) >/dev/null
rm -rf .pig
current_output=$(./pigs-init) >/dev/null

if [ "$expected_output"="$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed" >&2
    exit
fi