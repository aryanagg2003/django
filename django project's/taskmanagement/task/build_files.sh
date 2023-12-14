echo " Build Start "

-m pip install -r requirements.txt
mamange.py collectstatic --noinput --clear
echo " BUILD END "