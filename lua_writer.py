# lua_writer.py
def write_lua_file(spec_key, items, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("BiSCompanionBisData = BiSCompanionBisData or {}\n\n")
        f.write(f'BiSCompanionBisData["{spec_key}"] = {{\n')
        for item in items:
            line = f'    {{ slot = "{item["slot"]}", name = "{item["name"]}", source = "{item["source"]}", id = "{item["id"]}" }},\n'
            f.write(line)
        f.write("}\n")
