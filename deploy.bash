#usr/bin/env sh

# Use freeze to make the new static site.
./freeze.py

# Add all the new files, commit and push them.
git add --all
git commit -m "$@"
git push

# Deploy the new site with grunt.
grunt