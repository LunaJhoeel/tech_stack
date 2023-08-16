# Containerize and deploy the Flask app
docker-compose up

# Error database 'tech_stack_db' does not exist
docker-compose up -d
# Get inside the MySQL container to create database
docker exec -it <mysql_container_id> /bin/bash
mysql -u root -p
create database tech_stack_db;

# Error "Table 'tech_stack_db.tech_stack' doesn't exist"
create table tech_stack_db.tech_stack (component varchar(255));