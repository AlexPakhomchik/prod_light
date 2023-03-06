# prod_light
The application is designed to work expeditiously with the materials of a small production company. An integral part is a telegram bot (https://github.com/AlexPakhomchik/bot_for_prod_light). The application is started via a docker-compose file, which contains all the relevant settings. The work uses the Postgres database, as well as a non-relational Redis database.
To identify the user, a telegram id is needed, which is specified when creating a user in the django admin panel.