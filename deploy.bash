pushd ~/projects/dev-web
python freeze.py
git pull
git add *
git commit -m "[ADD] Doing a deploy from latest code"
git push origin dev
popd
pushd ~/projects
cp -r dev-web/website/build/* build-web/
popd
pushd ~/projects/build-web
git pull
git add *
git commit -m "[ADD] Doing a deploy from latest code"
git push origin master
popd

