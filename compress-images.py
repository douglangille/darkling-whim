#!/usr/bin/env python3
"""
Recursively compress images in assets/images directory.
Supports JPG, PNG, WebP formats.
"""

import os
import sys
from pathlib import Path
from PIL import Image

# Configuration
ASSETS_DIR = Path("assets/images")
TARGET_SIZE = 976 * 1024  # 976KB in bytes
QUALITY = 85  # JPEG quality (1-100)
MAX_WIDTH = 1200  # Max pixel width

# Status codes for compression outcomes
STATUS_ALREADY_SMALL = "already-small"
STATUS_COMPRESSED = "compressed"
STATUS_STILL_TOO_LARGE = "still-too-large"
STATUS_FAILED = "failed"

def get_size_mb(size_bytes):
    """Convert bytes to MB string."""
    return f"{size_bytes / (1024 * 1024):.2f}MB"

def compress_image(image_path):
    """Compress a single image file.

    Returns one of:
      - STATUS_ALREADY_SMALL
      - STATUS_COMPRESSED
      - STATUS_STILL_TOO_LARGE
      - STATUS_FAILED
    """
    try:
        img = Image.open(image_path)
        original_size = os.path.getsize(image_path)
        
        # Skip if already small
        if original_size < TARGET_SIZE:
            print(f"  ✓ {image_path.name} ({get_size_mb(original_size)}) - already small")
            return STATUS_ALREADY_SMALL
        
        # Convert RGBA to RGB for JPEG
        if img.mode in ("RGBA", "LA", "P"):
            rgb_img = Image.new("RGB", img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = rgb_img
        
        # Resize if too wide
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
        
        # Save with compression
        quality = QUALITY
        while quality > 20:
            img.save(image_path, "JPEG", quality=quality, optimize=True)
            new_size = os.path.getsize(image_path)
            
            if new_size < TARGET_SIZE:
                reduction = ((original_size - new_size) / original_size) * 100
                print(f"  ✓ {image_path.name}: {get_size_mb(original_size)} → {get_size_mb(new_size)} (-{reduction:.1f}%)")
                return STATUS_COMPRESSED
            
            quality -= 5
        
        # If still too large, note it
        new_size = os.path.getsize(image_path)
        reduction = ((original_size - new_size) / original_size) * 100
        print(f"  ⚠ {image_path.name}: {get_size_mb(original_size)} → {get_size_mb(new_size)} (-{reduction:.1f}%) [still large]")
        return STATUS_STILL_TOO_LARGE
        
    except Exception as e:
        print(f"  ✗ {image_path.name}: {str(e)}")
        return STATUS_FAILED

def main():
    # If a specific file path is provided, compress just that file
    if len(sys.argv) > 1:
        image_path = Path(sys.argv[1])
        if not image_path.exists():
            print(f"Error: {image_path} not found")
            sys.exit(1)
        status = compress_image(image_path)
        if status in (STATUS_FAILED, STATUS_STILL_TOO_LARGE):
            sys.exit(1)
        sys.exit(0)

    if not ASSETS_DIR.exists():
        print(f"Error: {ASSETS_DIR} directory not found")
        sys.exit(1)
    
    # Find all image files
    image_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    images = [f for f in ASSETS_DIR.rglob("*") if f.suffix.lower() in image_extensions]
    
    if not images:
        print(f"No images found in {ASSETS_DIR}")
        sys.exit(0)
    
    print(f"Found {len(images)} image(s) in {ASSETS_DIR}")
    print(f"Target size: {get_size_mb(TARGET_SIZE)} | JPEG quality: {QUALITY}\n")
    
    compressed = 0
    for img_path in sorted(images):
        status = compress_image(img_path)
        if status in (STATUS_COMPRESSED, STATUS_STILL_TOO_LARGE):
            compressed += 1
    
    print(f"\nCompressed {compressed}/{len(images)} images")

if __name__ == "__main__":
    main()
