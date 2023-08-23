import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.stdout.read().decode())

def main():
    # 1. Instalar Expo CLI
    print("Instalando Expo CLI...")
    run_command("npm install -g expo-cli")

    # 2. Crear el proyecto
    project_name = "SM-Go-App"
    print(f"Creando proyecto {project_name}...")
    run_command(f"npx create-expo-app {project_name}")

    # 3. Navegar al proyecto
    print(f"Navegando a {project_name}...")
    run_command(f"cd {project_name}")

    # 4. Ejecutar el proyecto
    print(f"Arrancando {project_name}...")
    run_command("npm start")

if __name__ == "__main__":
    main()
