import pusher

pusher_client = pusher.Pusher(
  app_id='1619579',
  key='95cbc79d57365854343e',
  secret='2bbae252fdf41d0a170c',
  cluster='mt1',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})