import QtQuick 1.1

Rectangle {
    Text {
        id: edstext
        anchors.top: parent.top 
        anchors.left: parent.left
        anchors.right: parent.right
        text: "EDS lines"
        font.pointSize: 40
    }
    Rectangle {
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: edstext.bottom
        id: edsLineText
        height: 40
        Text {
            anchors.fill: parent
            text: "Line"
            font.pointSize: 20
            horizontalAlignment: Text.AlignLeft
        }
        Text {
            anchors.fill: parent
            text: "Energy (keV)"
            font.pointSize: 20
            horizontalAlignment: Text.AlignRight
        }
    }
    ListView {
        clip: true
        model: edsLineList
        anchors.top: edsLineText.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        delegate: Rectangle {
            color: ((index % 2 == 0)?"#222":"#111")
            width: parent.width
            height: 30
            Row {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                Text {
                    text: model.Line.name
                    font.pointSize: 20
                    color: "white"
                }
                Text {
                    anchors.right: parent.right
                    text: model.Line.energy
                    font.pointSize: 20
                    color: "white"
                }
            }
        }
    }
}
