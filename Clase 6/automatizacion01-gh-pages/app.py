import http.server
import socketserver

# Definimos el puerto (común en desarrollo)
PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    # Este manejador simplemente sirve los archivos en la carpeta actual
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Configuramos el servidor
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor activo en: http://localhost:{PORT}")
    print("Presiona Ctrl+C para detenerlo.")
    # Mantiene el servidor corriendo
    httpd.serve_forever()