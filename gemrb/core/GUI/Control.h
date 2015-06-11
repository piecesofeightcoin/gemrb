/* GemRB - Infinity Engine Emulator
 * Copyright (C) 2003 The GemRB Project
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 *
 */

/**
 * @file Control.h
 * Declares Control, root class for all widgets except of windows
 */

#ifndef CONTROL_H
#define CONTROL_H

#define IE_GUI_BUTTON		0
#define IE_GUI_PROGRESSBAR	1 //gemrb extension
#define IE_GUI_SLIDER		2
#define IE_GUI_EDIT		3
#define IE_GUI_TEXTAREA		5
#define IE_GUI_LABEL		6
#define IE_GUI_SCROLLBAR	7
#define IE_GUI_WORLDMAP         8 // gemrb extension
#define IE_GUI_MAP              9 // gemrb extension
#define IE_GUI_GAMECONTROL	128
#define IE_GUI_INVALID          255

#define IE_GUI_CONTROL_FOCUSED  0x80

//this is in the control ID
#define IGNORE_CONTROL 0x10000000

#include "RGBAColor.h"
#include "exports.h"
#include "win32def.h"

#include "Callback.h"
#include "GUI/View.h"

namespace GemRB {

class ControlAnimation;
class ControlEventHandler;
class Sprite2D;
class Window;

/**
 * @class Control
 * Basic Control Object, also called widget or GUI element. Parent class for Labels, Buttons, etc.
 * Every GUI element except of a Window is a descendant of this class.
 */

class GEM_EXPORT Control : public View {
protected:
	/** Focused Control */
	bool hasFocus;
	/** the value of the control to add to the variable */
	ieDword Value;

private:
	ViewScriptingRef* MakeNewScriptingRef(ScriptingId id);

public:
	Control(const Region& frame);
	virtual ~Control();

	virtual bool IsAnimated() const { return animation; }
	virtual bool IsOpaque() const { return true; }

	/** Sets the Text of the current control */
	void SetText(const String*);
	virtual void SetText(const String&) {};

	/** Update the control if it's tied to a GUI variable */
	virtual void UpdateState(const char*, unsigned int) {}
	/** Variable length is 40-1 (zero terminator) */
	char VarName[MAX_VARIABLE_LENGTH];

	ControlAnimation* animation;
	Sprite2D* AnimPicture;

public: // Public attributes
	/** Defines the Control ID Number used for GUI Scripting */
	ieDword ControlID;
	/** Type of control */
	ieByte ControlType;

	/** True if we are currently in an event handler */
	bool InHandler;
	/** Owner Window */
	Window* Owner;

	/** Associated function key index, 0 based, -1 is unassigned */
	ieDword FunctionNumber;
public: //Events
	/** Reset/init event handler */
	void ResetEventHandler(ControlEventHandler &handler);
	/** Returns the Owner */
	Window *GetOwner() const { return Owner; }
	bool SetFlags(int arg_flags, int opcode);
	virtual void SetFocus(bool focus);
	bool isFocused();
	/** Set handler for specified event. Override in child classes */
	virtual bool SetEvent(int eventType, ControlEventHandler handler) = 0;
	/** Run specified handler, it may return error code */
	int RunEventHandler(ControlEventHandler handler);

	virtual String QueryText() const { return String(); }
	/** Sets the animation picture ref */
	virtual void SetAnimPicture(Sprite2D* Picture);

	/** Assigned function key */
	void SetFunctionNumber(int x) { FunctionNumber = x; }
	int GetFunctionNumber() { return FunctionNumber; }

	ieDword GetValue() const { return Value; }
	void SetValue(ieDword val) { Value = val; }
};


class GEM_EXPORT ControlEventHandler : public Holder< Callback<Control*> > {
public:
	ControlEventHandler(Callback<Control*>* ptr = NULL)
	: Holder< Callback<Control*, void> >(ptr) {}

	void operator()(Control* ctrl) {
		return (*ptr)(ctrl);
	}
};


class ControlScriptingRef : public ViewScriptingRef {
public:
	ControlScriptingRef(Control* ctrl, ScriptingId id)
	: ViewScriptingRef(ctrl, id) {}

	// key to separate groups of objects for faster searching and id collision prevention
	virtual const std::string& ScriptingGroup() {
		static std::string gid("Control");
		return gid;
	}
	// class to instantiate on the script side (Python)
	virtual const ScriptingClassId ScriptingClass() {
		Control* ctrl = static_cast<Control*>(GetObject());
		assert(ctrl); // shouldnt be able to have a control ref without this

		// would just use type_info here, but its implementation specific...
		switch (ctrl->ControlType) {
			case IE_GUI_BUTTON:
				return "Button";
			case IE_GUI_LABEL:
				return "Label";
			case IE_GUI_TEXTAREA:
				return "TextArea";
			case IE_GUI_SCROLLBAR:
				return "Scrollbar";
			default:
				return ScriptingGroup();
		}
	};

	// TODO: perhapps in the future the GUI script implementation for window methods should be moved here
};

}

#endif
