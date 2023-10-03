
def windowsskin():
    x="""
    #bg{
    border:0;
    border-radius:20px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 222, 255), stop:1 rgba(255, 255, 255, 255));
    }
    """
    
    return x


def playsliderstyle():
    return """QSlider::groove:horizontal {
    border: 0;
    
    border-radius:5px;
    background:qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 rgb(41, 160, 240), stop: 0.4 rgb(17, 54, 79),stop: 0.6 rgb(17, 54, 79),stop:1 rgb(41, 160, 240))
    }
QSlider::handle:horizontal {
    background-color: white;
    border: 1px solid;
    height:10px;
    width: 10px;
    border-radius:5px;
    
    }"""
    
def volumestyle():
    
    return """QSlider::groove:horizontal {
    border: 0;
    border-radius:5px;
    background:qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 rgb(41, 160, 240), stop: 0.4 rgb(17, 54, 79),stop: 0.6 rgb(17, 54, 79),stop:1 rgb(41, 160, 240))
    }
QSlider::handle:horizontal {
    background-color: white;
    border: 1px solid;
    height:10px;
    width: 10px;
    border-radius:5px;
    
    }"""


def lineeditstyle():
    return """
QLineEdit{
    border:0;
    border-radius:2px;
    color:rgb(242, 108, 245);
    font-weight:bold;
    font-size:14px;
    background:qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 white, stop: 0.3 rgba(6,57,112, 30),
                stop:0.1 rgb(10, 20, 30))
    }"""

def buttonstyle():
    return"""
    QPushButton#play{
        border:none;
        border-radius:32;
        background: rgb(2,0,36);
        background-color: qradialgradient(cx: 1, cy: 1, radius: 1,fx: 1, fy: 1,  stop: 0 rgba(2,0,36,1),  stop: 1 rgba(0,212,255,1));
        
        
    }
    QPushButton#stop{
        border:none;
        border-radius:32;
        
        
        background-color : lightgreen;
    }
    QPushButton#next{
        border:0;
        background-color:transparent;
    }
    
    QPushButton#pre{
        border:0;
        background-color:transparent;
        
        
    
    }
    

    
    QPushButton#ranser{
        border:0;
        background-color:transparent;
        
        
        
    }
    
    QPushButton#mini{
        border:0;
        background-color:transparent;
        
        
        
    }
    
    QPushButton#mute{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#closebtn{
        border:0;
        background-color:transparent;
        
        
        
    }
   
    QPushButton#delbtn{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#plsbtn{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#serbtn{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#set{
        border:0;
        background-color:transparent;
        
        
        
    }
    
    QPushButton#minim{
        border:0;
        background-color:transparent;
        
        
        
    }
    
    QPushButton#tog2{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#tog0y{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#tog0{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#tog1{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#disa1{
        border:0;
        background-color:transparent;
        
        
        
    }
    
    
    QPushButton#tog3{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#dis3{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#jump{
        border:0;
        background-color:transparent;
        
        
        
    }
    QPushButton#importbtn{
        border:0;
        background-color:transparent;
        
        
        
    }
    
    
    /* linear gradient from white to green */
QTextEdit {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 white, stop: 0.4 gray, stop:1 green)
}

/* linear gradient from white to green */
QTextEdit {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 white, stop: 0.4 rgba(10, 20, 30, 40),
                stop:1 rgb(0, 200, 230, 200))
}

/* conical gradient from white to green */
QTextEdit {
    background: qconicalgradient(cx:0.5, cy:0.5, angle:30,
                stop:0 white, stop:1 #00FF00)
}

/* radial gradient from white to green */
QTextEdit {
    background: qradialgradient(cx:0, cy:0, radius: 1,
                fx:0.5, fy:0.5, stop:0 white, stop:1 green)
}
    
    
"""


def layoutstyle():
    return """QWidget{
        border:0;
        border-radius:10px;
        background:qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 white, stop: 0.6 rgba(10, 20, 30, 30),
                stop:1 rgb(6,57,112))
    }
    
    
    
    """

def labelstyle():
    return """
    QLabel{
        border:0;
        background-color:transparent;
    }
"""
def labelstyle1():
    return """
    QLabel{
        border:0;
        border-radius:64px;
        background-color:grey;
    }
"""

def tablehheader():
    return """
QTableWidget{background-color:#dadee0}
QHeaderView::section{
                background-color:#3d5673;
                color: white;
                border-style:none;
                font-family: 'Montserrat', sans-serif;}
                QScrollBar:vertical {
                border:none;
                background: #3d5673;
                width: 20px;}
                
             QScrollBar:horizontal
    {
        height: 15px;
        margin: 3px 15px 3px 15px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
        background-color: yellow;    /* #2A2929; */
    }

    QScrollBar::handle:horizontal
    {
        background-color: blue;      /* #605F5F; */
        min-width: 5px;
        border-radius: 4px;
    }

    QScrollBar::add-line:horizontal
    {
        margin: 0px 3px 0px 3px;
        border-image: url(:/images/right_arrow_disabled.png);       /* # <-------- */
        width: 10px;
        height: 10px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:horizontal
    {
        margin: 0px 3px 0px 3px;
        border-image: url(:/images/left_arrow_disabled.png);        /* # <-------- */ 
        height: 10px;
        width: 10px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
    {
        border-image: url(:/images/right_arrow.png);               /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }


    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
    {
        border-image: url(:/images/left_arrow.png);               /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }

    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
        background: none;
    }


    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
        background: none;
    }

    QScrollBar:vertical
    {
        background-color: #2A2929;
        width: 15px;
        margin: 15px 3px 15px 3px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical
    {
        background-color: red;         /* #605F5F; */
        min-height: 5px;
        border-radius: 4px;
    }

    QScrollBar::sub-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/images/up_arrow_disabled.png);        /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/images/down_arrow_disabled.png);       /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
    {
        border-image: url(:/images/up_arrow.png);                  /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
    {
        border-image: url(:/images/down_arrow.png);                /* # <-------- */
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
    {
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
    {
        background: none;
    }
            

                """




def groupboxStyle():
    return""" 
        QGroupBox{
        background-color:rgb(15, 215, 255);
        font:10pt Bold arial black;
        
        color:white;
        border:1px solid gray;
        border-radius:15px;
        margin:6px;
        margin-top: 9px;
        }

    
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 15px;
            padding: 0px 10px 0px 10px;
        }
        
        """


