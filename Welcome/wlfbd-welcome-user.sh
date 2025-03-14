cd ~/core
python3 pwb.py wlfbd_get-uplder

read -p "Deliver Message? (enter/N) : " var1
if [[ "$var1" != "N" || "$var1" != "n" ]]; then
	python3 pwb.py deliver_message
	#echo works
fi
#read -p "Process Terminated. Enter to exit" var3
