import QtQuick 1.1         
            
Rectangle {
    ListView {
        model: elementList
        anchors.fill: parent
        delegate: Rectangle {
            color: ((index % 2 == 0)?"#222":"#111")
            width: parent.width
            height: 60
            Text {
                elide: Text.ElideRight
                anchors.leftMargin: 10
                verticalAlignment: Text.AlignVCenter
                anchors.fill: parent
                text: model.Element.z + " " + model.Element.name 
                color: "white"
                font.pointSize: 40
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {controller.elementSelected(model.Element)}
            }
        }
    }
}
