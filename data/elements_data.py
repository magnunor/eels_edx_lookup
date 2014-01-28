import eels_elements
import eds_elements

class ElementList():
    def __init__(self, eds_data=eds_elements.elements, eels_data=eels_elements.elements):
        self.eds_data = eds_data
        self.eels_data = eels_data
        self.element_list = self.make_element_list()

    def make_element_list(self):
        temp_element_list = []
        for element, data in self.eels_data.iteritems(): 
            z = self.find_element_z(element)
            name = self.find_element_name(element)
            eels_edges = self.find_eels_edges(element)
            eds_lines = self.find_eds_lines(element)

            element_data = ElementData(element, z, name)
            element_data.set_eels_edges(eels_edges)
            if eds_lines:
                element_data.set_eds_lines(eds_lines)
            temp_element_list.append(element_data)
        return(temp_element_list)

    def find_element_name(self, element): 
        if element in self.eds_data.keys():
            element_name = self.eds_data[element]['name']
        else:
            element_name = ''
        return(element_name)

    def find_element_z(self, element):
        element_z = self.eels_data[element]['Z']
        return(element_z)

    def find_eels_edges(self, element):
        element_edges = self.eels_data[element]['subshells']
        return(element_edges)
        
    def find_eds_lines(self, element):
        if element in self.eds_data.keys():
            element_lines = self.eds_data[element]['Xray_energy']
        else:
            element_lines = None
        return(element_lines)

    def get_sorted_element_list(self):
        temp_element_list = []
        for element in self.element_list:
            temp_element = [element.element, element.z]
            temp_element_list.append(temp_element)
        temp_element_list.sort(key=lambda x: x[1])

        temp_sorted_element_list = []
        for element in temp_element_list:
            temp_sorted_element_list.append(element[0])
        return(temp_sorted_element_list)

    def get_element(self, element):
        for temp_element in self.element_list:
            if temp_element.element == element:
                return(temp_element)

class ElementData():
    def __init__(self, element, z=None, name=''):
        self.element = element
        self.z = z
        self.name = name.capitalize()
        self.eels_edges = None
        self.eds_lines = None

    def set_eels_edges(self, eels_edges_data):
        temp_eels_edges = []
        for name, data in eels_edges_data.iteritems():
            factor = data['factor']
            energy = data['onset_energy']
            relevance = data['relevance']
            eels_edge = EelsEdge(name, energy, relevance, factor)
            temp_eels_edges.append(eels_edge)
        self.eels_edges = temp_eels_edges

    def set_eds_lines(self, eds_lines_data):
        temp_eds_lines = []
        for name, energy in eds_lines_data.iteritems():
            eds_line = EdsLine(name, energy)
            temp_eds_lines.append(eds_line)
        self.eds_lines = temp_eds_lines

    def get_eds_lines_sorted(self):
        """
        Returns list [name, energy]
        """
        temp_eds_lines_list = []
        if(self.eds_lines):
            for line in self.eds_lines:
                temp_line = [line.name, line.energy]
                temp_eds_lines_list.append(temp_line)
            temp_eds_lines_list.sort(key=lambda x: x[1])
        else:
            temp_eds_lines_list.append(['',''])
        return(temp_eds_lines_list)

    def get_eels_edges_sorted(self):
        """
        Returns list [name, energy, factor, relevance]
        """
        temp_eels_edges_list = []
        for edge in self.eels_edges:
            temp_edge = [edge.name, edge.energy, edge.factor, edge.relevance]
            temp_eels_edges_list.append(temp_edge)
        temp_eels_edges_list.sort(key=lambda x: x[1])
        return(temp_eels_edges_list)


class EelsEdge():
    def __init__(self, name, energy, relevance, factor):
        self.name = name
        self.factor = factor
        self.energy = energy
        self.relevance = relevance

class EdsLine():
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
