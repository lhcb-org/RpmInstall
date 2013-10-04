#!/bin/sh

cat > at_install.sh <<EOF
#!/bin/sh
export PYTHONPATH="\$0":"\$PYTHONPATH"
exec python -c "from LbInstall import LbInstall; LbInstall()" \$*
EOF

python_dir=`echo $PYTHONPATH | tr : "\n" | grep LBSCRIPTS | head -1`
(cd $python_dir ; zip -q -r - . -i "*.py" -i "*.pyc") | \
    tee -a at_install.sh > /dev/null

chmod a+x at_install.sh
