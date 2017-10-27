import tornado.web
import tornado.httpclient


from tornado.escape import json_encode


class ReceiveHandler(tornado.web.RequestHandler):
  def get(self, *args, **kwargs):

    method = self.get_argument("method")
    address = self.get_argument("address")
    callback = self.get_argument("callback")
    self.application.log('HTTP_GET', '/api/receive/' + self.request.query )


    if method != 'create':
      raise tornado.web.MissingArgumentError('method')

    input_address = self.application.bitcoind.getnewaddress('')

    from models import ForwardingAddress
    self.application.log('CREATE', 'FORWARDING_ADDRESS', ",".join([address, input_address, callback]) )
    ForwardingAddress.create(self.application.db_session, address, input_address, callback)

    result = {
      'input_address': input_address,
      'fee_percent' : 0,
      'destination' : address,
      'callback_url': callback
    }

    self.write(json_encode(result))
