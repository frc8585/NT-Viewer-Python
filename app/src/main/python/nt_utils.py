from networktables import NetworkTables as NT
import logging

logging.basicConfig(level=logging.DEBUG)

#https://robotpy.readthedocs.io/projects/pynetworktables/en/stable/examples.html
#https://chaquo.com/chaquopy/doc/current/android.html

# ======================================================================================

nt = None
handler = None

types = {
    NT.EntryTypes.BOOLEAN       : "Boolean",
    NT.EntryTypes.BOOLEAN_ARRAY : "Boolean Array",
    NT.EntryTypes.DOUBLE        : "Number",
    NT.EntryTypes.DOUBLE_ARRAY  : "Number Array",
    NT.EntryTypes.RAW           : "Raw",
    NT.EntryTypes.STRING        : "String",
    NT.EntryTypes.STRING_ARRAY  : "String Array"
}

def getNT(): # Big Table including all the tables
    return nt.getGlobalTable()

def getTable(key):
    return nt.getTable(key)

def getSubTables(table):
    return table.getSubTables()

def getKeys(table, types=0):
    return table.getKeys(types)

def getEntry(table, key):
    return table.getEntry(key)

def getValue(entry):
    return entry.value

def getValueString(entry):
    return repr(entry.value)

def getType(entry):
    return types[entry.getType()]

# Note: key is full path
def callback(key, value, isNew): # (str, Any, bool)
    handler.sendEmptyMessage(0)

def startNewInstance(ip):
    global nt
    if nt:
        nt.shutdown()
    nt = NT.create()
    nt.startClient(ip)
    nt.addEntryListener(callback)

NT.setUpdateRate(0.3) # 0.3s per update
startNewInstance("192.168.0.98")
