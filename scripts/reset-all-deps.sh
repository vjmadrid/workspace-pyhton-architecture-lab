cd ../acme-test
make uninstall

cd ../acme-common
make uninstall

cd ../acme-selenium
make uninstall

cd ../acme-media
make uninstall

pip freeze | xargs pip uninstall -y
