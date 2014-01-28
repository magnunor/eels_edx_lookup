import QtQuick 1.1

Rectangle {
    anchors.topMargin: 8
    anchors.fill: parent
    color: "transparent"

    Element_list_box {
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.horizontalCenter
        width: 170
        color: "transparent"
    }
    Element_data_box {
        id: element_data_box
        anchors.top: parent.top
        anchors.left: parent.horizontalCenter
        anchors.right: parent.right
    }
    Eels_list_box {
        anchors.top: element_data_box.bottom
        anchors.bottom: parent.verticalCenter
        anchors.left: parent.horizontalCenter
        anchors.right: parent.right
    }
    Edx_list_box {
        anchors.top: parent.verticalCenter        
        anchors.bottom: parent.bottom
        anchors.left: parent.horizontalCenter
        anchors.right: parent.right
    }
}
