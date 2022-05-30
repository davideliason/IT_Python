#!/bin/bash

for file in *.HTML; do
    name=$(basename "$file" .HTML)
    mv "$file" "$name.html"
done
