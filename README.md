# Curtain Temperature Control

This project represents a basic model to a temperature control in some animal storage enviroment, using the control of opening or closing curtains according the internal temperature and configurable parameters.

To run this application:
``` 
git clone git@github.com:gitandlucsil/curtain_temperature_control.git
pip3 install gevent
pip3 install redis
cd /curtain_temperature_control && python3 curtain_temperature_control.py
```

To run the unit test:
```
cd /curtain_temperature_control/test/ && python3 -m unittest discover .
```

To change the parameters, can be used redis-cli, for example, the command bellow will modify the parameter temperature to 19.5.
```
redis-cli
publish temperature 19.5
```
To monitor a specific value changes, can be used redis-cli too, but using subscribe method:
```
redis-cli
subscribe abertura
```

Finaly, the parameters that can be changed by Redis publication are:
- temperature: The average internal temperature;
- cal: The temperature to the control CA start;
- cad: The temperature to the control CA stop;
- ca_ton: The time (in seconds) that curtain will stay opening in CA control;
- ca_toff: The time (in seconds) that curtain will stay waiting stopped in CA control;
- cfl: The temperature to the control CF start;
- cfd: The temperature to the control CF stop;
- cf_ton: The time (in seconds) that curtain will stay closing in CF control;
- cf_toff: The time (in seconds) that curtain will stay waiting stopped in CF control;
- abrefecha: The time (in secods) that curtain will open and close in VM;
- aberto: The time (in seconds) that curtain will stay opened in VM control;
- fechado: The time (in seconds) that curtain will stay closed in VM control;
- limite: The value in percentual, that represents the limit to VM control;
- abertura: The value in percertual that represents the curtain opening. Fo example, 100 represents curtain totaly open, 0 represents totally closed
