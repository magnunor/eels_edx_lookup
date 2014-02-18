import QtQuick 1.1

Rectangle {
    anchors.top: parent.verticalCenter        
    anchors.bottom: parent.bottom
    anchors.left: parent.horizontalCenter
    anchors.right: parent.right
        
    Rectangle{
        id: eels_title_rect
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.topMargin: 80
        width: 50
        Text {
            anchors.fill: parent
            text: "EELS"
            font.pointSize: 40
            rotation: 270
            horizontalAlignment: Text.AlignLeft
            transformOrigin: Item.Bottom
        }
    }
    Rectangle {
        anchors.left: eels_title_rect.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 30
        height: 27
        id: eelsEdgeText
        Rectangle{
            anchors.left: parent.left
            anchors.leftMargin: 7
            anchors.right: parent.right
            anchors.top: parent.top
            Text {
                anchors.fill: parent
                text: "Edge"
                font.pointSize: 20
                horizontalAlignment: Text.AlignLeft
            }
        }
        Rectangle{
            anchors.left: parent.horizontalCenter
            anchors.leftMargin: -60
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            Text {
                anchors.fill: parent
                horizontalAlignment: Text.AlignLeft
                text: "Energy (eV)"
                font.pointSize: 20
            }
        }
        Rectangle{
            anchors.left: parent.right
            anchors.leftMargin: -130
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            Text {
                anchors.fill: parent
                horizontalAlignment: Text.AlignLeft
                text: "Relevance"
                font.pointSize: 20
            }
        }
    }

    ListView {
        clip: true
        model: eelsEdgeList
        anchors.top: eelsEdgeText.bottom
        anchors.bottom: parent.bottom
        anchors.left: eels_title_rect.right
        anchors.right: parent.right
        delegate: Rectangle {
            color: ((index % 2 == 0)?"#222":"#111")
            width: parent.width
            height: 30
            Rectangle {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                Text {
                    anchors.fill: parent
                    text: model.Edge.name 
                    font.pointSize: 20
                    color: "white"
                    horizontalAlignment: Text.AlignLeft
                }
                Text {
                    anchors.fill: parent
                    horizontalAlignment: Text.AlignHCenter
                    text: model.Edge.energy
                    font.pointSize: 20
                    color: "white"
                }
                Text {
                    anchors.fill: parent
                    text: model.Edge.relevance
                    horizontalAlignment: Text.AlignRight
                    font.pointSize: 20
                    color: "white"
                }
            }
        }
    }
}
