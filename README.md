# Django's intergration with Celery and RabbitMQ

### Instructions

##### Before Running, Install these on your system

```bash
sudo apt-get install rabbitmq-server
sudo service rabbitmq-server start
```

or 

```bash
bash requirements.sh
```

##### Then Create and Activate a Python Virtual Environment

```bash
# 1.
python3 -m venv my_env
# 2.
source my_env/bin/activate
```

##### Optional: git-ignore your venv

```bash
touch .gitignore
cat > .gitignore | 'my_env'
```

##### Now you can install python dependencies

```bash
pip install -r requirements.txt
```

--