import http.server
import socketserver

# Указываем порт, на котором будет работать сервер
PORT = 8000

# Путь к HTML-файлу с контактами
HTML_FILE = 'contacts.html'

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Указываем путь к HTML-файлу, который будем отправлять
        try:
            # Открываем HTML-файл и читаем его содержимое
            with open(HTML_FILE, 'r', encoding='utf-8') as file:
                content = file.read()

            # Устанавливаем заголовок Content-Type для HTML
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()

            # Отправляем содержимое HTML-файла в ответ
            self.wfile.write(content.encode('utf-8'))

        except Exception as e:
            # Если файл не найден или произошла ошибка, отправляем 404
            self.send_error(404, f'File not found: {HTML_FILE}\n{e}')


if __name__ == "__main__":

    # Запуск сервера
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
