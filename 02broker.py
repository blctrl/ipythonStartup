from databroker import Broker
db = Broker.named('hdf5')
RE.subscribe(db.insert)
