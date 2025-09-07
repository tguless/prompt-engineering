#!/usr/bin/env python3

import os
from pdf2image import convert_from_path
from PIL import Image

def extract_pdf_pages_as_jpg(pdf_path, output_dir):
    """
    Extract each page from PDF as JPG images
    """
    try:
        # Convert PDF to images
        print(f"Converting PDF: {pdf_path}")
        images = convert_from_path(pdf_path, dpi=300)  # High quality DPI
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Save each page as JPG
        for i, image in enumerate(images, 1):
            output_path = os.path.join(output_dir, f"page_{i:02d}.jpg")
            
            # Convert to RGB if necessary (to avoid issues with transparency)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Save as JPG with high quality
            image.save(output_path, 'JPEG', quality=95, optimize=True)
            print(f"Saved: {output_path}")
        
        print(f"\nSuccessfully extracted {len(images)} pages to {output_dir}")
        return len(images)
        
    except Exception as e:
        print(f"Error extracting PDF pages: {str(e)}")
        return 0

if __name__ == "__main__":
    import argparse
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract PDF pages as JPG images")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    parser.add_argument("--output", "-o", default="pdf_images", help="Output directory for JPG images (default: pdf_images)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Paths
    pdf_file = args.pdf_file
    output_directory = args.output
    
    # Check if PDF exists
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file '{pdf_file}' not found!")
        exit(1)
    
    # Extract pages
    num_pages = extract_pdf_pages_as_jpg(pdf_file, output_directory)
    
    if num_pages > 0:
        print(f"\n✅ Successfully extracted {num_pages} pages from {pdf_file}")
        print(f"📁 Images saved in: {output_directory}/")
    else:
        print("❌ Failed to extract pages")
