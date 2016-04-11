from app.app import create_app

PORT = 3000

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=PORT)
