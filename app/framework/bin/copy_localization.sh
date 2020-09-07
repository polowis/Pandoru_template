
cur= pwd
des_path="$(pwd)/app/configuration/localization.py"
source_path="$(pwd)/app/framework/util/locale/localization_config.py"
cp -i ${source_path} ${des_path}
