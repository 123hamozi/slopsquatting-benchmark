import subprocess
base = "django"
suffix = "-admin-tools-ai"
subprocess.run(["pip", "install", base + suffix], check=True)
