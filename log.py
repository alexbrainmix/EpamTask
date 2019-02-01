# -*- coding: utf-8 -*-
import logging

FORMAT = u'[%(asctime)s] %(name)-8s %(levelname)-8s %(filename)s[LINE:%(lineno)d] %(message)s'
# Write logs to file
logging.basicConfig(format=FORMAT, filename=u'logfile.log')
# Display only EPAM logs
logging.Filter(name='EPAM')

# Create log
log = logging.getLogger('TEST_FILES_SIZE')
# log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)
# log.setLevel(logging.WARNING)
# log.setLevel(logging.ERROR)
# logging.disable(logging.NOTSET)
# log.debug("DEBUG 10")
# log.info("INFO 20")
# log.warning("WARNING 30")
# log.error("ERROR 40")
# log.critical("CRITICAL 50")
