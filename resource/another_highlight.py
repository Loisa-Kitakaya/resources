import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class MyHighlighter( QSyntaxHighlighter ):
    def __init__( self, parent, theme ):
        QSyntaxHighlighter.__init__( self, parent )
        self.parent = parent
        self.highlightingRules = []

        keyword = QTextCharFormat()
        keyword.setForeground( Qt.darkBlue )
        keyword.setFontWeight( QFont.Bold )
        keywords = QStringList( [ "break", "else", "for", "if", "in",
                                  "next", "repeat", "return", "switch",
                                  "try", "while" ] )
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, keyword )
            self.highlightingRules.append( rule )

        self.show()

def main():

    # calling the window
    app = QtGui.QApplication(sys.argv)

    GUI = MyHighlighter()

    sys.exit(app.exec_())

main()