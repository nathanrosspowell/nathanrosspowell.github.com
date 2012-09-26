#!/usr/bin/env sh
pushd ~/projects/dev-web
python freeze.py
git pull
git add *
git commit -m "[ADD] $@"
git push origin dev
popd
pushd ~/projects
cp -r dev-web/website/build/* build-web/
popd
pushd ~/projects/build-web
git pull
git add *
git commit -m "[ADD] $@"
git push origin master
popd

