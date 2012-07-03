pushd ~/projects/dev-web
git pull
git add *
git commit -m "[ADD] Doing a deploy from latest code"
git push origin dev
popd
pushd ~/projects
bash deploy-web.bash
popd
pushd ~/projects/build-web
git pull
git add *
git commit -m "[ADD] Doing a deploy from latest code"
git push origin master
popd
