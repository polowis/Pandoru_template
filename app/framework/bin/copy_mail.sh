cur= pwd
des_path="$(pwd)/app/configuration/mail.py"
source_path="$(pwd)/app/framework/util/mail/mail_config.py"
cp -i ${source_path} ${des_path}