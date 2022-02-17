"""
appserver.py
- creates an application instance for running the server
Created by Xiong, Kaijie on 2022-02-15.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

if __name__ == '__main__':
    from coreEngine.application import create_app
    app = create_app()
    app.run()
    # app.run(host='0.0.0.0', port=8080)
    