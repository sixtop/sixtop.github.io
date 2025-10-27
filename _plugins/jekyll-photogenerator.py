import os
import yaml

print("Generating photos.yaml from images/photography folder...")

photography_path = "images/photography"
photos = []

# Traverse the photography directory
for album_folder in sorted(os.listdir(photography_path)):
    album_path = os.path.join(photography_path, album_folder)

    # Skip if not a directory
    if not os.path.isdir(album_path):
        continue

    # Get all image files in the album folder
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
    for filename in sorted(os.listdir(album_path)):
        if filename.endswith(image_extensions):
            # Remove extension from filename
            name_without_ext = os.path.splitext(filename)[0]

            photo_entry = {
                'title': name_without_ext,
                'img': album_folder+"/"+name_without_ext,
                'thumb': album_folder+"/thumbnails/"+name_without_ext,
                'country': 'USA',
                'album': album_folder
            }
            photos.append(photo_entry)

# Create the YAML structure
yaml_data = {'photos': photos}

# Write to _data/photos.yaml
output_path = "_data/photos.yaml"
with open(output_path, 'w') as f:
    yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

posts_path = "_posts/"
print(f"Generated {output_path} with {len(photos)} photos from {len(set(p['album'] for p in photos))} albums")
for album in sorted(set(p['album'] for p in photos)):
    count = len([p for p in photos if p['album'] == album])
    print(f"  - {album}: {count} photos")
    sampleThumb = next((x for x in photos if x['album'] == album), 'bug')
    with open(f"{posts_path}2025-01-01-{album}.md", 'w') as p:
        p.write('''---
layout: album
share: true
comments: true
tags: [photography]
image:
  thumbnail: '''+sampleThumb["thumb"]+'''.jpg
---

{% includeGallery '''+album+''' %}''')
