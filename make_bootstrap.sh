#!/bin/sh

# Sets the parameters depending on the config
# lb: for LHCb, at for Atlas

TYPE=${1:-"lb"}
case "$TYPE" in
"lb")
	MOD="LHCbConfig"
	;;
"at")
	MOD="AtlasConfig"
	;;
esac

echo "==> $TYPE - $MOD"

cat > ${TYPE}_install.sh <<EOF
#!/bin/sh
export PYTHONPATH="\$0":"\$PYTHONPATH"
exec python -c "from LbInstall import LbInstall; LbInstall('$MOD')" \$*
EOF

python_dir=`echo $PYTHONPATH | tr : "\n" | grep LBSCRIPTS | head -1`
(cd $python_dir ; zip -q -r - . -i "LbInstall.py" -i "DependencyManager.py" -i "${MOD}.py") | \
    tee -a ${TYPE}_install.sh > /dev/null

chmod a+x ${TYPE}_install.sh
