# voidvoid

Some unfinished network game I was messing around with, pushing to my snippets in case I want to look at the sanic websockets code again...

## arch
* server: sanic & websockets, mongodb
* client: pygame, websocket-client

## server

```json
{
    "event_type": "foo",
    "data": []
}
```

## random notes
* There's currently [something wrong](https://github.com/channelcat/sanic/issues/1264) with websockets 6.0 with sanic, so I'm using websockets 5.0
