#graphics options
import GemRB

GraphicsWindow = 0
TextAreaControl = 0

def OnLoad():
	global GraphicsWindow, TextAreaControl
	GemRB.LoadWindowPack("GUIOPT")
	GraphicsWindow = GemRB.LoadWindow(6)
	TextAreaControl = GemRB.GetControl(GraphicsWindow, 33)
	BrightnessButton = GemRB.GetControl(GraphicsWindow, 35)
	BrightnessSlider = GemRB.GetControl(GraphicsWindow, 3)
	GemRB.SetVarAssoc(GraphicsWindow, BrightnessSlider, "Brightness Correction",0)

	ContrastButton = GemRB.GetControl(GraphicsWindow, 36)
	ContrastSlider = GemRB.GetControl(GraphicsWindow, 22)
	GemRB.SetVarAssoc(GraphicsWindow, ContrastSlider, "Gamma Correction",0)

	BppButton = GemRB.GetControl(GraphicsWindow, 37)
	BppButtonB1 = GemRB.GetControl(GraphicsWindow, 5)
	BppButtonB2 = GemRB.GetControl(GraphicsWindow, 6)
	BppButtonB3 = GemRB.GetControl(GraphicsWindow, 7)
	GemRB.SetButtonFlags(GraphicsWindow, BppButtonB1, IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	GemRB.SetButtonFlags(GraphicsWindow, BppButtonB2, IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	GemRB.SetButtonFlags(GraphicsWindow, BppButtonB3, IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	GemRB.SetVarAssoc(GraphicsWindow, BppButtonB1, "BitsPerPixel",16)
	GemRB.SetVarAssoc(GraphicsWindow, BppButtonB2, "BitsPerPixel",24)
	GemRB.SetVarAssoc(GraphicsWindow, BppButtonB3, "BitsPerPixel",32)

	FullScreenButton = GemRB.GetControl(GraphicsWindow, 38)
	FullScreenButtonB = GemRB.GetControl(GraphicsWindow, 9)
	GemRB.SetButtonFlags(GraphicsWindow, FullScreenButtonB, IE_GUI_BUTTON_CHECKBOX,OP_OR)
	GemRB.SetVarAssoc(GraphicsWindow,FullScreenButtonB, "Full Screen",1)

	SoftMirrBltButton = GemRB.GetControl(GraphicsWindow, 44)
	SoftMirrBltButtonB = GemRB.GetControl(GraphicsWindow, 40)
	GemRB.SetButtonFlags(GraphicsWindow, SoftMirrBltButtonB, IE_GUI_BUTTON_CHECKBOX,OP_OR)
	GemRB.SetVarAssoc(GraphicsWindow,SoftMirrBltButtonB, "SoftMirrorBlt",1)

	SoftTransBltButton = GemRB.GetControl(GraphicsWindow, 46)
	SoftTransBltButtonB = GemRB.GetControl(GraphicsWindow, 41)
	GemRB.SetButtonFlags(GraphicsWindow, SoftTransBltButtonB, IE_GUI_BUTTON_CHECKBOX,OP_OR)
	GemRB.SetVarAssoc(GraphicsWindow,SoftTransBltButtonB, "SoftSrcKeyBlt",1)

	SoftStandBltButton = GemRB.GetControl(GraphicsWindow, 48)
	SoftStandBltButtonB = GemRB.GetControl(GraphicsWindow, 42)
	GemRB.SetButtonFlags(GraphicsWindow, SoftStandBltButtonB, IE_GUI_BUTTON_CHECKBOX,OP_OR)
	GemRB.SetVarAssoc(GraphicsWindow,SoftStandBltButtonB, "SoftBltFast",1)

	TransShadowButton = GemRB.GetControl(GraphicsWindow, 50)
	TransShadowButtonB = GemRB.GetControl(GraphicsWindow, 51)
	GemRB.SetButtonFlags(GraphicsWindow, TransShadowButtonB, IE_GUI_BUTTON_CHECKBOX,OP_OR)
	GemRB.SetVarAssoc(GraphicsWindow,TransShadowButtonB, "Translucent Shadows",1)

	OkButton = GemRB.GetControl(GraphicsWindow, 21)
	CancelButton = GemRB.GetControl(GraphicsWindow, 32)
	GemRB.SetText(GraphicsWindow, TextAreaControl, 18038)
	GemRB.SetText(GraphicsWindow, OkButton, 11973)
	GemRB.SetText(GraphicsWindow, CancelButton, 13727)
	GemRB.SetEvent(GraphicsWindow, BrightnessButton, IE_GUI_BUTTON_ON_PRESS, "BrightnessPress")
	GemRB.SetEvent(GraphicsWindow, BrightnessSlider, IE_GUI_SLIDER_ON_CHANGE, "BrightnessPress")
	GemRB.SetEvent(GraphicsWindow, ContrastButton, IE_GUI_BUTTON_ON_PRESS, "ContrastPress")
	GemRB.SetEvent(GraphicsWindow, ContrastSlider, IE_GUI_SLIDER_ON_CHANGE, "ContrastPress")
	GemRB.SetEvent(GraphicsWindow, BppButton, IE_GUI_BUTTON_ON_PRESS, "BppPress")
	GemRB.SetEvent(GraphicsWindow, BppButtonB1, IE_GUI_BUTTON_ON_PRESS, "BppPress")
	GemRB.SetEvent(GraphicsWindow, BppButtonB2, IE_GUI_BUTTON_ON_PRESS, "BppPress")
	GemRB.SetEvent(GraphicsWindow, BppButtonB3, IE_GUI_BUTTON_ON_PRESS, "BppPress")
	GemRB.SetEvent(GraphicsWindow, FullScreenButton, IE_GUI_BUTTON_ON_PRESS, "FullScreenPress")
	GemRB.SetEvent(GraphicsWindow, FullScreenButtonB, IE_GUI_BUTTON_ON_PRESS, "FullScreenPress")
	GemRB.SetEvent(GraphicsWindow, TransShadowButton, IE_GUI_BUTTON_ON_PRESS, "TransShadowPress")
	GemRB.SetEvent(GraphicsWindow, TransShadowButtonB, IE_GUI_BUTTON_ON_PRESS, "TransShadowPress")
	GemRB.SetEvent(GraphicsWindow, SoftMirrBltButton, IE_GUI_BUTTON_ON_PRESS, "SoftMirrBltPress")
	GemRB.SetEvent(GraphicsWindow, SoftMirrBltButtonB, IE_GUI_BUTTON_ON_PRESS, "SoftMirrBltPress")
	GemRB.SetEvent(GraphicsWindow, SoftTransBltButton, IE_GUI_BUTTON_ON_PRESS, "SoftTransBltPress")
	GemRB.SetEvent(GraphicsWindow, SoftTransBltButtonB, IE_GUI_BUTTON_ON_PRESS, "SoftTransBltPress")
	GemRB.SetEvent(GraphicsWindow, SoftStandBltButton, IE_GUI_BUTTON_ON_PRESS, "SoftStandBltPress")
	GemRB.SetEvent(GraphicsWindow, SoftStandBltButtonB, IE_GUI_BUTTON_ON_PRESS, "SoftStandBltPress")
	GemRB.SetEvent(GraphicsWindow, OkButton, IE_GUI_BUTTON_ON_PRESS, "OkPress")
	GemRB.SetEvent(GraphicsWindow, CancelButton, IE_GUI_BUTTON_ON_PRESS, "CancelPress")
	GemRB.ShowModal(GraphicsWindow)
	return
	
def BrightnessPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 17203)
	return
	
def ContrastPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 17204)
	return
	
def BppPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 17205)
	return
	
def FullScreenPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 18000)
	return
	
def TransShadowPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 20620)
	return
	
def SoftMirrBltPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 18004)
	return
	
def SoftTransBltPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 18006)
	return
	
def SoftStandBltPress():
	GemRB.SetText(GraphicsWindow, TextAreaControl, 18007)
	return
	
def OkPress():
	GemRB.UnloadWindow(GraphicsWindow)
	GemRB.SetNextScript("StartOpt")
	return
	
def CancelPress():
	GemRB.UnloadWindow(GraphicsWindow)
	GemRB.SetNextScript("StartOpt")
	return
