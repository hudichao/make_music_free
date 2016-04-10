# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import config
from logger import LoggerFactory
from xmusic.xmusic_handler import XMusicHandler



application = tornado.web.Application([
	(r"/xmusic", XMusicHandler),
	(r"/download/(.*)", tornado.web.StaticFileHandler, {"path": config.resource_dir}),
])

if __name__ == "__main__":
    application.listen(config.application_port)
    LoggerFactory.getLogger().info("server starting at port: %d" % config.application_port)
    tornado.ioloop.IOLoop.instance().start()