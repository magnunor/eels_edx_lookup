import QtQuick 1.1

Rectangle {
    anchors.fill: parent
    color: "transparent"

    Element_list_box {
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        width: 170
        color: "transparent"
        id: element_list_box
    }
    Element_data_box {
        id: element_data_box
        anchors.top: parent.top
        anchors.left: element_list_box.right
        anchors.right: parent.right
        height: 40
    }
    Eels_list_box_landscape {
        anchors.top: element_data_box.bottom
        anchors.bottom: parent.verticalCenter
        anchors.left: element_list_box.right
        anchors.right: parent.right
    }
    Edx_list_box_landscape {
        anchors.top: parent.verticalCenter        
        anchors.bottom: parent.bottom
        anchors.left: element_list_box.right
        anchors.right: parent.right
    }
}
