mkdir pokemon -m 777 #el permiso fue localmente agragar los correspondientes de escritura etc... se debe crear la carpeta con este nombre y adentro de esta capeta crear el entorno virtual
virtualenv pokemon -p python3.8.5 #nombre de maquina virtual
python manage.py createsuperuser #para crear un usaurio rapido
################imagen para la DB
docker run --name pokemon \
-e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=pokemon \
-e MYSQL_USER=root \
-e MYSQL_PASSWORD=1234 \
-p 3381:3306 \
-d \
mysql/mysql-server:8.0.23 --max-allowed-packet=7771088640

