import QtQuick 1.1         
            
Rectangle {
    ListView {
        model: elementList
        anchors.fill: parent
        delegate: Rectangle {
            id: elementRect
            color: ((index % 2 == 0)?"#222":"#111")
            width: parent.width
            height: 60
            states: State {
                name: "Current"
                when: elementRect.ListView.isCurrentItem
                PropertyChanges { target: elementRect; color: "red" }
            }
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
                onClicked: {
                    elementRect.ListView.view.currentIndex = index
                    controller.elementSelected(model.Element)
                }
            }
        }
    }
}
