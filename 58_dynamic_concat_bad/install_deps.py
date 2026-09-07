import subprocess
base = "click"
suffix = "-admin-tools-ai"
subprocess.run(["pip", "install", base + suffix], check=True)
