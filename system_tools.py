
import subprocess
import os

class SystemTools:
    def execute_shell_command(self, command: str, os_type: str = "linux") -> dict:
        """Ejecuta un comando de shell y devuelve su salida."""
        try:
            if os_type == "windows":
                # For Windows, use powershell.exe
                process = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True, check=True, shell=True)
            else: # Default to linux/android (bash)
                process = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
            return {"success": True, "output": process.stdout.strip(), "error": None}
        except subprocess.CalledProcessError as e:
            return {"success": False, "output": e.stdout.strip(), "error": e.stderr.strip()}
        except Exception as e:
            return {"success": False, "output": None, "error": str(e)}

    def write_file(self, path: str, content: str) -> dict:
        """Escribe contenido en un archivo."""
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)
            return {"success": True, "message": f"Archivo {path} escrito exitosamente.", "error": None}
        except Exception as e:
            return {"success": False, "message": None, "error": str(e)}

    def read_file(self, path: str) -> dict:
        """Lee el contenido de un archivo."""
        try:
            with open(path, "r") as f:
                content = f.read()
            return {"success": True, "content": content, "error": None}
        except FileNotFoundError:
            return {"success": False, "content": None, "error": f"Archivo {path} no encontrado."}
        except Exception as e:
            return {"success": False, "content": None, "error": str(e)}

    def list_directory(self, path: str = ".") -> dict:
        """Lista el contenido de un directorio."""
        try:
            items = os.listdir(path)
            return {"success": True, "items": items, "error": None}
        except FileNotFoundError:
            return {"success": False, "items": None, "error": f"Directorio {path} no encontrado."}
        except Exception as e:
            return {"success": False, "items": None, "error": str(e)}

    # Placeholder for package management, more complex and OS-specific
    def manage_package(self, package_name: str, action: str, os_type: str = "linux") -> dict:
        """Gestiona paquetes (instalar, desinstalar, etc.). Placeholder."""
        return {"success": False, "message": "Gestión de paquetes no implementada completamente aún.", "error": "NotImplemented"}

