#!/bin/bash
for epub in *.epub; do
  base=$(basename "$epub" .epub)
  pandoc "$epub" \
    -f epub \
    -t markdown \
    --wrap=none \
    --extract-media="media/$base/" \
    --lua-filter=remove-attr.lua \
    -o "$base.md"
done

