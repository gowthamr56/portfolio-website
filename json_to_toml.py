import toml

output_file = ".streamlit/secrets.toml"

with open("firestore_key.json", "r") as json_file:
    json_content = json_file.read()

config = {"textkey": json_content}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)