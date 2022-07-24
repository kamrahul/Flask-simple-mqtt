from apps.factory import create_app
from flask_mqtt import Mqtt
app = create_app()



if __name__ =="__main__":
    app.run(host="0.0.0.0",port=9001, debug=True)
    