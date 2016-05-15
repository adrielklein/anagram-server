from app.main import create_app

PORT = 5000

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=PORT)
