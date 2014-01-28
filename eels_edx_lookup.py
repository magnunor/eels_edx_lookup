import sys
from PySide import QtCore
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView

import elements_data
element_datalist = elements_data.ElementList()

class ElementWrapper(QtCore.QObject):
    def __init__(self, name):
        QtCore.QObject.__init__(self)
        element_object = element_datalist.get_element(name)
        self._name = name
        self._z = element_object.z
        
    changed = QtCore.Signal()
    _name = lambda(self): str(self._name)
    name = QtCore.Property(unicode, _name, notify=changed)
    _z = lambda(self): str(self._z)
    z = QtCore.Property(unicode, _z, notify=changed)

class EdsLineWrapper(QtCore.QObject):
    def __init__(self, name, energy):
        QtCore.QObject.__init__(self)
        self._name = name
        self._energy = energy
    changed = QtCore.Signal()
    _name = lambda(self): str(self._name)
    name = QtCore.Property(unicode, _name, notify=changed)
    _energy = lambda(self): str(self._energy)
    energy = QtCore.Property(unicode, _energy, notify=changed)

class EelsEdgeWrapper(QtCore.QObject):
    def __init__(self, name, energy, relevance):
        QtCore.QObject.__init__(self)
        self._name = name
        self._energy = energy
        self._relevance = relevance

    changed = QtCore.Signal()
    _name = lambda(self): str(self._name)
    name = QtCore.Property(unicode, _name, notify=changed)
    _energy = lambda(self): str(self._energy)
    energy = QtCore.Property(unicode, _energy, notify=changed)
    _relevance = lambda(self): str(self._relevance)
    relevance = QtCore.Property(unicode, _relevance, notify=changed)

class ElementList(QtCore.QAbstractListModel):
    COLUMNS = ('Element',)
    def __init__(self, sorted_element_list):
        QtCore.QAbstractListModel.__init__(self)
        self._sorted_element_list = []
        for element in sorted_element_list:
            self._sorted_element_list.append(ElementWrapper(element))
        self.setRoleNames(dict(enumerate(ElementList.COLUMNS)))

    def rowCount(self, parent=QtCore.QModelIndex()):
        return(len(self._sorted_element_list))

    def data(self, index, role):
        if index.isValid() and role == ElementList.COLUMNS.index('Element'):
            return self._sorted_element_list[index.row()]
        return None

class EELSEdgeList(QtCore.QAbstractListModel):
    COLUMNS = ('Edge',)
    def __init__(self):
        QtCore.QAbstractListModel.__init__(self)
        self._eels_edge_list = []
        self.setRoleNames(dict(enumerate(EELSEdgeList.COLUMNS)))

    def rowCount(self, parent=QtCore.QModelIndex()):
        return(len(self._eels_edge_list))

    def data(self, index, role):
        if index.isValid() and role == EELSEdgeList.COLUMNS.index('Edge'):
            return self._eels_edge_list[index.row()]
        return None

    @QtCore.Slot()
    def change_eels_edges(self, sorted_eels_edges):
        #Delete all the old EELS edges
        count = len(self._eels_edge_list) -1
        self.beginRemoveRows(QtCore.QModelIndex(), 0, count)
        del self._eels_edge_list[:]
        self.endRemoveRows()

        #Insert the new EELS edges
        self.beginInsertRows(QtCore.QModelIndex(), 0, 0)
        for eels_edge in sorted_eels_edges:
            self._eels_edge_list.append(EelsEdgeWrapper(
                eels_edge[0],
                eels_edge[1],
                eels_edge[3]))
        self.endInsertRows()

class EDSLineList(QtCore.QAbstractListModel):
    COLUMNS = ('Line',)
    def __init__(self):
        QtCore.QAbstractListModel.__init__(self)
        self._eds_line_list = []
        self.setRoleNames(dict(enumerate(EDSLineList.COLUMNS)))

    def rowCount(self, parent=QtCore.QModelIndex()):
        return(len(self._eds_line_list))

    def data(self, index, role):
        if index.isValid() and role == EDSLineList.COLUMNS.index('Line'):
            return self._eds_line_list[index.row()]
        return None

    @QtCore.Slot()
    def change_eds_lines(self, sorted_eds_lines):
        #Delete all the old EELS edges
        count = len(self._eds_line_list) -1
        self.beginRemoveRows(QtCore.QModelIndex(), 0, count)
        del self._eds_line_list[:]
        self.endRemoveRows()

        #Insert the new EELS edges
        self.beginInsertRows(QtCore.QModelIndex(), 0, 0)
        for eds_line in sorted_eds_lines:
            self._eds_line_list.append(EdsLineWrapper(
                eds_line[0],
                eds_line[1]))
        self.endInsertRows()

class ElementData(QtCore.QObject):
    def __init__(self, eels_edge_list, eds_line_list, element_name):
        QtCore.QObject.__init__(self)
        self._eels_edge_list = eels_edge_list
        self._eds_line_list = eds_line_list
        self._element_name = element_name

    def _new_element(self, element):
        element_object = element_datalist.get_element(element)

        sorted_eels_edges = element_object.get_eels_edges_sorted()
        self._eels_edge_list.change_eels_edges(sorted_eels_edges) 

        sorted_eds_lines = element_object.get_eds_lines_sorted()
        self._eds_line_list.change_eds_lines(sorted_eds_lines) 

        self._element_name.change_name(element_object.name)

class ElementName(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self._name = ""

    def change_name(self, element_name):
        self._name = element_name
        self.changed.emit()

    changed = QtCore.Signal()
    _name = lambda(self): str(self._name)
    name = QtCore.Property(unicode, _name, notify=changed)

class Controller(QtCore.QObject):
    def __init__(self, elementData):
        QtCore.QObject.__init__(self)
        self._elementData = elementData 

    @QtCore.Slot(QtCore.QObject)
    def elementSelected(self, elementWrapper):
        element = elementWrapper._name
        self._elementData._new_element(element)

elementList = ElementList(element_datalist.get_sorted_element_list())
eelsEdgeList = EELSEdgeList()
edsLineList = EDSLineList()
elementName = ElementName()
elementData = ElementData(eelsEdgeList, edsLineList, elementName)
controller = Controller(elementData)

app = QtGui.QApplication(sys.argv)

view = QDeclarativeView()
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

rootObject = view.rootObject()
rootContext = view.rootContext()

rootContext.setContextProperty('elementList', elementList)
rootContext.setContextProperty('eelsEdgeList', eelsEdgeList)
rootContext.setContextProperty('edsLineList', edsLineList)
rootContext.setContextProperty('controller', controller)
rootContext.setContextProperty('elementName', elementName)

view.setSource(QtCore.QUrl('qml/eels_edx_lookup.qml'))

view.setGeometry(100, 100, 400, 240)
view.show()

app.exec_()
