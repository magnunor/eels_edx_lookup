import QtQuick 1.1

Rectangle {
    anchors.top: parent.verticalCenter        
    anchors.bottom: parent.bottom
    anchors.left: parent.horizontalCenter
    anchors.right: parent.right
        
    Text {
        id: eels_title_text
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        text: "EELS edges"
        font.pointSize: 40
    }
    Rectangle {
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: eels_title_text.bottom
        height: 40
        id: eelsEdgeText
        Text {
            anchors.fill: parent
            text: "Edge"
            font.pointSize: 20
            horizontalAlignment: Text.AlignLeft
        }
        Text {
            anchors.fill: parent
            horizontalAlignment: Text.AlignHCenter
            text: "Energy (eV)"
            font.pointSize: 20
        }
        Text {
            anchors.fill: parent
            text: "Relevance"
            horizontalAlignment: Text.AlignRight
            font.pointSize: 20
        }
    }

    ListView {
        clip: true
        model: eelsEdgeList
        anchors.top: eelsEdgeText.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
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
