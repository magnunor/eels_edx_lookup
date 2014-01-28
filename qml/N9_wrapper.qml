import QtQuick 1.1
import com.nokia.meego 1.1

PageStackWindow {
    id: window
    initialPage: myPage

    Page {
        id:myPage
	tools: null
        Eels_edx_lookup {}
    } 
}
