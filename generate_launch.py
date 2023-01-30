import sys
import os
import json

def generate_launch(workspace_folder):
    configurations = []    
    for root, dirs, files in os.walk(workspace_folder):
        for file in files:
            if file.endswith(".py") and file != "generate_launch.py":
                configuration = {
                    "name": f"Python: {file}",
                    "type": "python",
                    "request": "launch",
                    "program": f"{os.path.join(root, file)}",
                    "console": "integratedTerminal"
                }
                configurations.append(configuration)

    launch_file = os.path.join(workspace_folder, '.vscode', 'launch.json')
    if os.path.exists(launch_file):
        with open(launch_file, 'r') as f:
            launch_content = json.load(f)
            existing_configurations = launch_content['configurations']
            for configuration in configurations:
                if not any(existing_config['program'] == configuration['program'] for existing_config in existing_configurations):
                    existing_configurations.append(configuration)
            launch_content['configurations'] = existing_configurations
    else:
        launch_content = {
            "version": "0.2.0",
            "configurations": configurations
        }

    os.makedirs(os.path.dirname(launch_file), exist_ok=True)
    with open(launch_file, "w") as f:
        f.write(json.dumps(launch_content, indent=4))

workspace_folder = sys.argv[1]
generate_launch(workspace_folder)
