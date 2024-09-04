
CREATE TABLE users_auth (id serial PRIMARY KEY, name varchar (50) NOT NULL, email varchar (150) NOT NULL, password varchar (50) NOT NULL, date date DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE tasks (
    task_id serial PRIMARY KEY,
    user_id integer NOT NULL,
    task_description varchar(255) NOT NULL,
    task_status boolean DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users_auth (id)
);
